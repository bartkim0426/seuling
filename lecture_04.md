# 4강 views.py 리펙토링		 

## 01. views.py 파일로 views 모듈로 리펙토링		


여러가지 문제들이 있어서 좋은 코드로 리펙토링
- 예외 처리가 안되어있다.
- 홈페이지 주소를 바꾸고싶을 때?: 현재는 urls.py, header.html을 변경해야함.		
- 이것을 해결하기 위해서 장고 템플릿에서 별칭(name)을 주고, header.html에서 장고 템플릿으로 {% url %}을 통해 알려줄 수 있다. 
	
*urls.py 에서*		

```
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name="home"),
    url(r'^rooms/(?P<room_id>\d+)/$', room, name="room"),
    url(r'^news/$', name, name = "news"),
]
```

*header.html*을 다음처럼 바꾼다.
	 

	<h1> Header </h1>

	<ul>
		<li><a href="{% url "home" %}"> HOME </a></li>
		<li><a href="{% "news"  %}"> NEWS PAGE </a></li>
	</ul>


> `/{% url "url_name" %}`이라는 미리 만들어진 장고 템플릿의 기능을 활용함

		
이렇게 되면 무슨 문제가 있을까?		
만약 views에 함수가 300개 넘게 많이 있다면? 		
- `import *`이라고 쓰는것: 안 좋은 코드, PEP 8에 위반
- 파일을 나누는 방법을 사용: 파일이 너무 많아져서 안 좋다.
- 관련성이 있는 파일을 묶어서 하나의 모듈로 사용: views라는 폴더를 만들고 `__init__.py`를 만들어서 `views.py`의 내용을 넣어서 `from wpsblog.views`로 불러옴 (이렇게 불러오면 파이썬은 구분을 못함)
- 그리고 home.py, room.py, neews.py로 넣어주면 됨. 
- `from wpsblog.views` 명령어는 views 폴더 안에 `__init__.py`를 부르기 때문에 동작이 안됨 => `from wpsblog.views.home import home`과 같이 변경해주면 동작함
- 번거로움을 피하기 위해서 `__init__.py`에서 `from .home import home`, `from .room import room`과 같은 방식으로 불러주고 `urls.py`에서 `from wpsblog.views import *`로 불러도 됨: 그럼 필요한 것들만 불러 올 수 있음. 


**tip** vim에서 swp 파일 git에 add 안되게 하기		
> 1. gitignore global setting
> 2. vim setting => swp file 생성 X 



## 02. urls.py 리펙토링: include 이용해서 관련된 url을 관리하기     


**페이지 추가하기**		
###  about page (.../about , .../about/us , .../about-us/)		

1. 가장 먼저 HttpResponse

```
from django.http import HttpResponse

def about(request):
    return HttpResponse("about")
```

2. loader로 사용

```
from django.template import loader
from django.http import HttpResponse

def about(request):
   # 1. template 객체 생성
   template = loader.get_template("about.html")
   # 2. HttpResponse로 template.render를 받음
   # render가 뭐를 받는지? 알고 싶으면 embed를 걸고
   # template.render? 물어보면 됨: context, request를 받는다
   return HttpResponse(
           template.render(
               {} , 
              request, 
               )
           ) # 이러면 about.html을 뿌려준다.
```

3. 이걸 한번에 해주는 shortcuts의 render 사용		
- render 함수는 (request, template_name, context) 세가지를 받음 		
- 위의 loader, HttpResponse를 축약 시켜준 것! 
```
from django.shortcuts import render

def about(request):
    return render(
           request,
           "about.html",
           {},
            )
```

### 정책 페이지 만들기
- 이용약관 page ( /terms/ )
- 개인정보 취급방침 페이지 (... /privacy/)
- 법적 고지와 책임의 한계 (... /disclaimer/)

> 비슷한 페이지: `urls.py`에서 정규식으로 받을 수 있다.		
> `url(r'^policy/(?P<policy_name>\w+)/$', policy, name='policy' )`		

- 이러면 `policy.py`에서 policy라는 함수에서 request, policy_name을 받아줄 수 있다. (room 함수와 거의 비슷) 	
- 여기에서 발전 시키려면 ?
```
from django.shortcut import render

def policy(request, policy_name):
	policy_dict = {
		"terms" : {
			"title": "서비스 이용 약관",
			"description": "서비스를 이용하기 위한 약관 정보입니다.",
			}, 
		"privacy" : {
			"title": "개인 정보 보호 정책",
			"description": "개인 정보 보호 정책 정보입니다.",
			}, 
		"disclaimer" : {
			"title": "책임의 한계와 법적 고지",
			"description": "책임의 한계와 법적 고지 정보입니다.",
			}, 
		}
		return render(
			request,
			"policy.html",
			policy_dict.get(policy_name)	
		)
```
이런 식으로 해주면 context 값으로 policy_dict의 title, description 값들을 `policy.html`에서 사용하여, url에 들어온 policy_id 값을 토대로 해당 값에 해당하는 value를 dict에서 찾아서 넣어줄 수 있다.		

- policy.html 에서

```
{% extend "base.html" %}
{% block content %}
<h1> Policy- {{ title }} </h1>
<p> {{ description }} </p>

{% endblock %}
```
이렇게 사용하면 바로 사용가능하다. 		

- 근데 이렇게 안하고 각각의 모듈을 만드는 방법도 있따.
terms, privacy, disclaimer를 각각으로 만들어서 urls.py에 각각을 등록, html도 각각을 만들어 주는 방법		

- 이것을 효과적으로 refactoring 하는 방법은?
- `urls.py`에서 policy들을 묶어주고 싶다?
> django.conf.url 안에 include라는 함수가 있다! 		
> policy는 include(포함)한다: policy로 시작하는 url 리스트를 인자로 받음		
```
url(r'^policy', include([
    url(r'terms/$', terms, name="terms"),
    url(r'privacy/$', privacy, name="privacy"),
    url(r'disclaimer/$', disclaimer, name='disclaimer'),
]))
```
즉, include를 받는 policy를 바꾸게 되면 다 바뀐다. (footer에서 url template tag를 수정했기 때문에-name으로 받는걸로!)		

- 이것보다 좀 더 낫게 수정하는 법: 어짜피 policy로 묶여 있기 때문에 이름도 공통적이면 어떨까? 		
> include라는 함수가 제공하는 기능: namespace
> url을 굉장히 구조화 시킬 수 있다
```
url(r'^policy', include([
    url(r'terms/$', terms, name="terms"),
    url(r'privacy/$', privacy, name="privacy"), url(r'disclaimer/$', disclaimer, name='disclaimer'),
], namespace="policy")) #policy라는 namespace 추가
```
그리고 추가적으로 html에서 url을 불러올 때 `{% url "policy:terms" %}`라는 방식으로 불러오면 된다. 즉, {% url "namespace:name" %}		

**tips: django 코드 찾는법**	
- django.conf.url의 include 찾는 법
> [github django 사이트](https://github.com/django/django/tree/master/django) 
> conf 폴더 안의 urls 폴더(모듈)의 `__init__.py`를 읽고 있는 것		
> 이 안의 include 함수를 찾을 수 있다.		
> 코드를 읽어보고 이해가 안되도 어떤 흐름으로 동작하는지 아는 것이 중요하다!!		

###다시 구조화된 형태로 리펙토링 하기	

1. 변수로 빼기 		
- urls.py에서 policy와 관련된 urlpatterns를 리스트로 빼주기(어짜피 include 함수는 리스트를 인자로 받기 때문이다.)		

```
	policy_urlpatterns = [
		url(r'terms/$', terms, name="terms"),
		url(r'privacy/$', privacy, name="privacy"), url(r'disclaimer/$', disclaimer, name='disclaimer'),
	] 
	urlpatterns = url(r'^policy', include(policy_urlpatterns, namespace="policy")) #policy라는 namespace 추가		
```

2. 파일로 뺀다. 		
- 그렇다면 이것을 다른 파일로 빼줄 수 있다: `policy_urls` 파일을 만들어서
```
# url을 쓰니깐\		
from django.conf.urls import url		
from wpsblog.views import *		
urlpatterns = [		
	url(r'terms/$', terms, name="terms"),		
	url(r'privacy/$', privacy, name="privacy"), url(r'disclaimer/$', disclaimer, name='disclaimer'),		
] 		
``` 

- 그리고 이것을 `urls.py`에서 그대로 받아서 쓰면 된다.		
`from wpsblog.policy_urls import urlpatterns as policy_urlpatterns`	

3. 모듈로 뺀다. 
- 얘를 또 줄여줄 수 있음: incude 내부 기능
> `from wpsblog.policy_urls imprt urlpatterns` 대신 내부적으로 읽는 기능		
> include()에다가 list가 아니라 str으로 		
```
include("wpsblog.policy_urls", namespace="policy")
```
이렇게 스트링으로 뺴 줄 수 있따는 말!		

4. ulrs/라는 모듈을 만들어서 전체를 리펙토링		
가능한 이유: include가 리스트 외에도 python 패키지의 이름을 받고, 그 안에 있는 urlpatterns라는 변수를 받도록 되어있기 때문에 쉽게 리펙토링이 가능하다.		

- urls.py 파일 또한 views 폴더로 만든 것처럼 urls 디렉토리로 만들고 폴더 안에 `__init__.py`로 불러올 수 있다.		
> 그렇게 되면 `policy_urls.py`도 urls 폴더 안에 policy.py로 빼서 불러올 수 이씀.



