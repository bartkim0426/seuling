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

	url(r'^policy', include([
		url(r'terms/$', terms, name="terms"),
		url(r'privacy/$', privacy, name="privacy"), url(r'disclaimer/$', disclaimer, name='disclaimer'),
	], namespace="policy")) #policy라는 namespace 추가

그리고 추가적으로 html에서 url을 불러올 때 `{% url "policy:terms" %}`라는 방식으로 불러오면 된다. 즉, {% url "namespace:name" %}		

**tips: django 코드 찾는법**	
- django.conf.url의 include 찾는 법
> [github django 사이트](https://github.com/django/django/tree/master/django) 
> conf 폴더 안의 urls 폴더(모듈)의 `__init__.py`를 읽고 있는 것		
> 이 안의 include 함수를 찾을 수 있다.		
> 코드를 읽어보고 이해가 안되도 어떤 흐름으로 동작하는지 아는 것이 중요하다!!		

###	다시 구조화된 형태로 리펙토링 하기	

1. 변수로 빼기 		
- urls.py에서 policy와 관련된 urlpatterns를 리스트로 빼주기(어짜피 include 함수는 리스트를 인자로 받기 때문이다.)		
	policy_urlpatterns = [
		url(r'terms/$', terms, name="terms"),
		url(r'privacy/$', privacy, name="privacy"), url(r'disclaimer/$', disclaimer, name='disclaimer'),
	] 
	urlpatterns = url(r'^policy', include(policy_urlpatterns, namespace="policy")) #policy라는 namespace 추가		


2. 파일로 뺀다. 		
- 그렇다면 이것을 다른 파일로 빼줄 수 있다: `policy_urls` 파일을 만들어서

# url을 쓰니깐		
	from django.conf.urls import url		
	from wpsblog.views import *		
	urlpatterns = [		
		url(r'terms/$', terms, name="terms"),		
		url(r'privacy/$', privacy, name="privacy"), url(r'disclaimer/$', disclaimer, name='disclaimer'),		
	] 		
 

- 그리고 이것을 `urls.py`에서 그대로 받아서 쓰면 된다.		
`from wpsblog.policy_urls import urlpatterns as policy_urlpatterns`	

3. 모듈로 뺀다. 
- 얘를 또 줄여줄 수 있음: incude 내부 기능
> `from wpsblog.policy_urls imprt urlpatterns` 대신 내부적으로 읽는 기능		
> include()에다가 list가 아니라 str으로 		

`include("wpsblog.policy_urls", namespace="policy")`

이렇게 스트링으로 뺴 줄 수 있따는 말!		

4. ulrs/라는 모듈을 만들어서 전체를 리펙토링		
가능한 이유: include가 리스트 외에도 python 패키지의 이름을 받고, 그 안에 있는 urlpatterns라는 변수를 받도록 되어있기 때문에 쉽게 리펙토링이 가능하다.		

- urls.py 파일 또한 views 폴더로 만든 것처럼 urls 디렉토리로 만들고 폴더 안에 `__init__.py`로 불러올 수 있다.		
> 그렇게 되면 `policy_urls.py`도 urls 폴더 안에 policy.py로 빼서 불러올 수 이씀.



## 03. settings.py 리펙토링-배포환경, 개발환경 구분하기

* 비개발자가 수정/변경할 수 있는 컨텐츠를 운용하는 방법?
django flatpages: 정적인 페이지를 쉽게 서버에서 불러올 수 있는 기능을 가진 앱, (https://docs.djangoproject.com/en/1.10/ref/contrib/flatpages/)		

* 설치할 라이브러리
1. django-debug-toolbar		
현재 문제: installed app에 debug_toolbar를 추가시키면 
`TypeError: '_TokenType' object is not callable`		
이라고 에러가 뜬다.		

2. settings.py 리펙토링
- 리펙토링 하지 않으면 `debug_toolbar`도 모든 사람이 볼 수 있기 때문에... 

- settings dir를 만들고, 그 안에 partials 폴더를 만든 후 settings.py의 내용들을 base, auth, database, static, internationalization의 5가지 기능별로 나누어 넣는다. partials 폴더의 각각의 `.py`의 세팅을 불러올 수 있게 `__init__.py`를 만들어 `from .base import *`와 같은 명령어로 다 불러온다.

- settings 폴더 안에 development, production을 만든다. production level에서 사용 할 것들을 불러준다. 

	from .partials import *		
	debug = False		

- development 파일에서는 production을 불러준 뒤 dev level에서 사용할 세팅을 지정한다.

	from .partials import *
	INSTALLED_APPS += ['debug_toolbar',]

- 마지막으로 settings 폴더를 `settings.py`처럼 기능할 수 있는 `__init__.py` 파일을 만들고, production level에서 작동할 수 있게 `from .production import *`를 적어준다. 그러면 기본적인 runserver에서는 이 세팅을 적용시킨다.

- dev level에서 작동시키기 위해서는 다음 명령어로 runserver를 작동시키면 된다. 		

	python manage.py runserver --settings=wpsblog.settings.development 		



## 04. git pre-commit hook을 이용한 PEP8 자동 체크하기		
[pep8](https://www.python.org/dev/peps/pep-0008/): 파이썬 스타일 가이드. 

- development 에다가 pep8을 설치하고 
> 설치하는 방법: development.txt에 pep8을 추가 하고 		
> `pip install -r development.txt`로 설치: development.txt를 읽어서 설치해라라는 뜻		
- pep8 . 으로 검사하면 된다. 
- 고쳐주는 것: autopep8이지만 쓰지 말아라. 		
> autopep8 -i . 쓰면 다 수정된다		
> tab vs space4? 정석적으로는 space 4칸이다.		

- 나는 거의 20~30개 나온다...
- pep8을 수정할 수 있음: 현재는 거의 쓸모 없는 기능들도 있다. -> 예를들면 79자 (모니터가 작아서..ㅋㅋ) 그래서 관례적으로 119글자를 사용하다. (max-120으로) 	
> 맨 상위 폴더에 `.pep8`이라는 파일을 만들어서 옵션을 줄 수 있다. 		

	[pep8] 		
	max-line-length = 119 		


* Git hooks: commit 할 때 pep8을 확인하게 만드는 것		
명령어를 똑같이 쳐보기		
`cp ./.git/hooks/pre-commit.sample ./.git/hooks/pre-commit`		
그리고 안에 내용을 지우고 `echo "Hello world"`를 하면 git-commit을 했을 때 hello world가 나온다. 그리고 커밋을 하면 pep8이 맞지 않으면 넘어가지 않게 된다. 

과제
1. 오늘까지 했던 settings를 정확하게 적용: (urls, views, settings 모듈로 분리하고 `--settings` 옵션으로 `runsderver`가 정상적으로 뜨는지 확인하기: dev level로 진행은 되지만, `_Tokentpye` error가 발생 		
2. `PEP8`을 제대로 맞춰서 코드 전체 수정
3. `django-debug-toolbar`가 어떤 기능이 제공되논지 살펴보기
4. `django-extentions`라는 패키지를 설치, 어떤 기능이 있는지 살펴보기..

[django-extensions github](https://github.com/django-extensions/django-extensions) 		
[django-extensions documentation](https://django-extensions.readthedocs.io/en/latest/)		  
