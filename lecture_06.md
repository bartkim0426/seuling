# 6강

## 01. 네이버 크롤링 명령어 구현

**tips**
> cowsay, lolcat    
> std 한 명령어를 stand in 해 주는데 특이한 효과를 줌   
> `echo "hello world" | cowsay | lolcat`    
> 설치는 `brew install cowsay', 'gen install lolcat`   
1. 커맨드 만들고
2. 모델 만들고
3. migrate 하고
4. 만들어서 뿌려주기
---

### **1. 커맨드 만들기:**    
`managements/commands/`에 `django.core.management.base`의 BaseCommand를 받아서 다음 코드를 실행.

- **add_arguments**로 query를 받을 수 있음
- query = options.get('query')로 받은 쿼리 사용 가능


```
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('query', type=str)

    def handle(self, *args, **options):
        query = options.get('query')

        url = "https://search.naver.com/search.naver?where=post&query={qurey}".format(query=query,)

        response = requests.get(url)
        dom = BeautifulSoup(response.text, "html.parser")
        
        post_elements = dom.select(".sh_blog_top")

        for post_element in post_elements:
           title_element = post_element.select_one(".sh_blog_title")
           title = title_element.text
           url = title_element.get('href')

           content_element = post_element.select_one('.sh_blog_passage')
           content = content_element.text

           thumbnail_image_element = post_element.select_one('.sh_blog_thumbnail')
           thumbnail_image_url = thumbnail_image_element.get('src')

        self.stdout.write("네이버에서 {query} 블로그 포스팅을 크롤링합니다.".format(query=query))
```
이 코드를 보면 `add_arguments`라고 지정된 방식으로 쓰는 것을 볼수 있다. 그리고 


**tip**   
코드 복사할 때 [gist](https://gist.github.com) 사이트에 들어가서 복붙하면 됨.. 
wget, curl로 해당 코드를 받으면 바로 사용 가능하다!!     


### 2. **모델 생성하기 (NaverPost)**    

- models.field를 확인하여 맞는 필드값을 사용하면 된다.
```
class Crawlnaver(models.Model):
    
    title = models.CharField(
            max_length=256
    )
    content = models.TextField()
    original_url = models.URLField()
    thumbnail_image_element= models.URLField()

    def __str__(self):
        return self.title
```   
- 다양한 modelsfield들을 알아둬야한다.


### **3. migrate 하기**
models.py를 하고 할 것   
1. makemigrations => 변동사항
2. migrate => migration files를 바탕으로 실제 데이터베이스에 기록하는 과정    

### 4. view 만들어서 뿌려주기   
- 뷰단에서는 다음과 같이 만들어준다. 모델에 모든 내용이 있기 때문에 아주 간결한 함수 뷰다
```
from django.shortcuts import render

from wpsblog.models import Crawlnaver


def naver_posts_list(request):
    return render(
           request,
           "naver_posts/list.html",
           {
               "naver_posts": Crawlnaver.objects.all(),
            },
    ) 
```   
- html에서는 그냥 for문만 돌리면 된다.    
```
{% extends "base.html" %}

{% block content %}
<h1> Naver Posts_with An </h1>
<ul>
{% for naver_post in naver_posts %}
<p>
	<li>
		<img src="{{ naver_post.thumbnail_image_element }}" alt="{{ naver_post.title }}"/>
		<h3>{{ naver_post.title }}</h3>
		<p> {{ naver_post.content }} </p>
		<a href="{{ naver_post.original_url }}"> 원문 바로가기 </a>
	</li></br>
{% endfor %} 
</p>
</ul>
{% endblock content %}
```   


> **tip**
> click_ : 파이썬에서 자주 쓰는 자신만의 커맨드를 만들 수 있다!   


+추가할것   
- 무슨 키워드로 크롤링했는지 데이터베이스에 저장   
- 특정 키워드로 크롤링 된 애들만 보여주는 뷰 (search)
- 제목에 특정 단어가 포함된 애들 보여주는 뷰 (search)


## 02 Model Filtering 을 활용한 검색 기능 구현하기

**웹 개발 접근방법**
- 장고 -> 내부적으로 어떻게 돌아가는지 알려면 코드를 다 봐야함: 웹 개발을 공부 할 때 모든걸 이해하려고 하면 안됨...    

- 지금은 add_arguments, command 등이 무슨 역할을 하고 어떤걸 쓰기 위해서 (argument를 받기 위해서) 어떻게 쓰는건지 알기만 하면 됨.    
    
- 큰그림을 그리는게 중요하다!   

### **+네이버 포스트 기능에추가할것**
### - 무슨 키워드로 크롤링했는지 데이터베이스에 저장     
1. 아주 쉬움. models에서 keyword라는 칼럼을 생성하고
2. commands의 crawl_naver에서  `keyword=query`로 입력값을 받아주면 됨
3. 이후에 makemigrations가 중요하다: 기존에 keyword가 없었기 때문에 물어볼 것
> 새롭게 keyword 칼럼이 생겼는데 이미 존재하는 low에 키워드를 뭘로 넣을것인지?    
> migrations 파일에 정한 값으로 써진다   


### - 특정 키워드로 크롤링 된 애들만 보여주는 뷰 (search)
- `/naver_posts_list/?keyword=python/` 이런 식으로 키워드 검색을 하면 해당 키워드로 크롤링 된 결과물만 볼 수 있도록   
- 우선 view에 `keyword = request.GET.get('keyword')`로 keyword로 받은 결과를 받아온다.    
- 그리고 특정 결과물만 검색하도록 한다.(정확한 검색)

```
...
def naver_posts_list(request):
    keyword = request.GET.get('keyword')
     
#     if keyword:
#         naver_posts = Crawlnaver.objects.filter(keyword=keyword)
#     else:
#         naver_posts = Crawlnaver.objects.all()
    naver_posts = Crawlnaver.objects.all()

    if keyword:
        naver_posts = [
                naver_post
                for naver_post
                in naver_posts
                if naver_post.keyword == keyword
                ]

    return render(
           request,
           "naver_posts/list.html",
           {
               "naver_posts": naver_posts,
               "keyword": keyword,
            },
    )

```     
주석 처리된 부분이 내가 만든것, 아래가 훨씬 깔끔한 것을 볼 수 있다.    

> 사실 장고에서 편하게 쓸 수 있도록 filter라는 기능을 제공함 
=> refactoring 해보자

```
...
naver_posts = Crawlnaver.objects.all()
    
if keyword:
    naver_posts = naver_posts.filter(keyword=keyword)
...
```   


### - 제목에 특정 단어가 포함된 애들 보여주는 뷰 (search)
이번에는 검색어가 포함되도록 하는것   
- 위와 똑같이 구현 가능한데 filter에서 `__icontains`를 쓰면 된다 (`__startswith`도 된다.)    
```
if search:
    naver_posts = naver_posts.filter(content__icontains=search)
```   
처럼 구현 가능

## 03. Post CRUD 구현   

### **1. form 만들기**
- posts를 가지고 할 것... `/posts/new/`를 만들거다   
- `/posts/new.html`에 POST method로 fomr 만들기
```
<form action="/posts/create/" method="POST">
<input type="text" name="title">
<input type="content" name="content">
<input type="submit" value="제출">
</form>
```
- 여기서 쓰면 list 페이지로 넘어가면서 리스트에 정보를 주도록 할 것... 근데 그냥 하면 CSRF 검증이 되면서 Forbidden이 됨. 왜그럴까?
> CSRF: POST방식을 굉장히 많이 보낼수 있음 (reqeust=POST, postman으로도 보낼 수 있음...) 
> 예를들면 은행 => csrf 토큰이 없으면 허가되지 않은 사용자가 여러 방식으로 보낼 수 있음
> 그래서 검증된 방식으로 요청되었는지를 체크함 : CSRF 쿠키와 CSRF 토큰으로!    

`{% csrf_token %}`을 추가    
=> 사이트에서 폼을 넘길때: form에 hiddentype으로 csrf token 암호키가 생겨서 폼을 넘길 때 이를 체크,    
=> 그러면 postman같은데서 하면 안된다. (장고의 약속이다.)    
근데 api 요청 등에는 csrf_token을 뺌 (웹사이트에서만 추가하는게 아니기 때문에) => 추후에 장고에서 다 설정이 가능,   
그래도 web site에서 폼을 보낼때는 항상 필요... 

### **2. 이후 `create.py`를 만들어서 create하는 뷰를 만들어 보기**    

POST 방식의 request는 `request.POST.get` 으로 받을 수 있다. 다음과 같이   
```
def create(requests):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    post = Post.objects.create(
        title=title,
        content=content
    )
```     
#### **redirect()**: 얘를 돌려주는 방법
=> 특정 페이지로 다시 돌려주는 것이다.     
`redirect(post.get_absolute_url())`   
=> 이건 약속이 되어있음: 모델의 객체가 들어오면 get_absolute_url로 간다고 되어있어서    
`redirect(post)`    
로 사용해도 된다. 

자.... create 이해한 내용을 차근차근... ㅠㅠ 
  1) url: `posts/new/`로 접속한다.     
  `url(r'^new/$', new, name = 'post-new')`    
  2) => `new.py`의 `new`함수 실행 (단순히 new.html을 불러오는 render 함수)   
  3) => `new.html`을 불러온다: 여기에 form 문이 들어있다.   
  `<form action="/posts/create/" method="POST">`

  4) => 위의 action은 posts/create.py를 불러온다. 실질적으로 db에 기록하는 역할을 하는 create.py     
  ```
  def create(requets):
      title = request.POST.get('title')
      content = request.POST.get('content')
      
      post = Post.objects.create(
             title = title,
             content = content,
      )
      return redirect(post)
  ```     
  5) 위의 redircet 함수가 실행되면서 `post.get_absolute_url`을 실행시킨다 (models.py에 있는) => 그래서 결국 `/posts/detail/5` (post_id) url로 가게 된다!!!       
  ```
  def get_absolute_url(self):
      return reverse(
             'posts:post-detail',
             kwargs = {'post_id':self.id},
      )
  ```     
  **posts:post-detail과 같은 형식으로 적어줘야한다: posts 폴더 아래 있는 post-detail이라는 name을 가진 url이라는뜻**
  
  

**edit, update**: new, create와 거의 동일하게 만듦   
(`edit.html`에서 `/posts/{{ post.id }}/update/`를 사용했더니 오류가 나서 settings/base.py에다가 ??SLASH=False를 해주었다. 추후에 수정할것)    

### 3. Edit, update 만들기

  1) url: `posts/1/edit`으로 구현할것.    
  `url(r'^(?P<post_id>\d+/edit/$', edit, name='post-edit')`   
  2) => 여기서 edit.py 함수를 불러온다. 거의 new.py 함수와 동일하다.   
  ```
  from django.shortcuts import render
  from wpsblog.models import Post


  def edit(request, post_id):
      return render(
             request,
             "posts/edit.html",
             {"post": Post.objects.get(id=post_id)},
             )
  ```   
  위 코드를 보면 거의 동일하지만 post_id만 받는 것을 볼 수 있다. 또한 context 변수로 나중에 post_id를 가진 post 객체를 db에서 찾아낼 수 있게 post를 추가해준다.   
  3) => 함수에서 `posts/edit.html`을 불러줌. new.html과 거의 동일한 코드이다.   
  ```
  {% extends "base.html" %}

  {% block content %}
  <h2> Edit post  </h2>

  <form action="/posts/{{ post.id }}/update/" method="POST">

    {% csrf_token %}
    <input type="text", name="title" placeholder="제목" value="{{ post.title }}">
    <input type="text", name="content" placeholder="내용" value="{{ post.content }}">
    <input type="submit", value="publish">
  </form>
  {% endblock %}
  ```   
  new와 거의 동일하지만 action 부분에서 `posts/1/update`와 같은 형식을 사용하기 위해서 저렇게 post.id를 넣어줬다. (여기서 쓰기 위해서 위에서 컨텍스트로 불렀다.)    
  또한 input의 value 값을 지정하여 수정시 이전 텍스트가 나오게 해준다. 
  > 참고로 지금은 절대 url을 사용했기 때문에 문제가 많을 수 있는데 추후에 리팩토링함   
  
  4) => 이제 posts/1/update 절대 경로로 update 함수를 불러온다.     
  ```
  from django.shortcuts import redirect, render
  from wpsblog.models import Post


  def update(request, post_id):
      post = Post.objects.get(id=post_id)

      title = request.POST.get("title")
      content = request.POST.get('content')
  #     post = Post.objects.get(id=post_id).update(
  #             title=title,
  #             content=content,
  #             )
      post.title = title
      post.content = content

      post.save()

      return redirect(post)
  ```   
  위의 코드를 보면 post_id를 가진 값을 찾은 다음에 해당 값을 수정하는 것. update()를 쓰지 않고 직접 바꿔주었다.     
  5) 이제 redirect된 url이 `post.get_absolute_url`을 따라서 detail/1/ (수정된 결과)가 나오게 된다! 
  
### 4. delete    
delete는 아주 간단하게 가능하다.

```
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from wpsblog.models import Post



def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()

    return redirect(
            reverse(
                "posts:post-list",
                )
            )
    # redirect("/posts/")
```   
보면 post.delete()로 저장...


  
### 7가지: [list, detail / new, create / edit, update / delete] 

이 7가지 기능만 완벽하게 알면 다 할 수 있다! 

**이후 refactoring 하기**
1. url: posts.py에 inclued로 url 받기     

2. {% url %} 방식으로 바꾸기: posts.py로 뺐기 때문에 `{% url "posts:detail" post_id=post.id %}`와 같은 형식으로 바꿔준다.   

3. `form.html`: new, edit.html이 너무 비슷해서 합칠 수 있다.    

하지만 action에 넣을 페이지가 겹침 
=> django template include variables    

`{% include 'posts:html' with action="/posts/create/" %}` 라고 사용하면 됨   



