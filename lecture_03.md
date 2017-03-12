## 03강

### 01. Django에서의 HTML 템플릿 렌더링(1): 직접 코드에서 HTML 파일 만들기

*왓차 정보 가져오기*

	news_dict = json.loads(response.content) #json 형태에서 dict 형태로 가져오기
	# news_dict = response.json() 도 똑같은 형태이다.		

> 디버깅 하는 벙법: IPython embed
> `from IPython import embed; embed()`
> 실행하는 중에 멈추고 embed가 실행된다.    

*왓차 이미지 표시하기*		
왓챠 dict 형태가 news:[{...imang:""...},{}] 형태이므로		

	news_items_list = news_dict.get("news")
	
*왓챠에 search 기능 추가*		
/?search=sth 을 추가하여 search 기능 붙여보기(방법이 많음)
1. if문 사용하기		
		

2. lambda를 통해 list 새로 만들기 

    if search:
        news_list = list(filter(
            lambda news: search in news.get('content'), 
            news_list,
            ))


*tip*
> dictionry에서 key값으로 value 조회할 때 		
> `student['name']` 보다 `student.get('address')`가 더 좋다.		
> `student.get('adress', '주소 없음')` 이런 식으로 기본 값으로 설정해 줄 수도 있다. 		

3. list comprehension으로 만들기

	news_list = [
			news for news in news_list.get('content')
			if search in news
	]


*request.GET*

    search =  request.GET.get('search') 
    print(search)
		

=> GET 방식으로 'search'라는 리퀘스트를 request 변수로 설정,		(만약 search가 있다면) search를 프린트		
=> 즉, request.GET 방식으로 보내진 'search' 쿼리를 get 하라는 명령어이다	
=> 장고 내부에서 쓰는 딕셔너리 형태. 		
=> 만약 query에서 /?search=곡성&where=seoul&hello=world 라고 썼다면 주소창의 GET 파라미터를 `request.GET.get('')`으로 찾을 수 있음			



### *form으로 search box 만들기*		


    form_html = """
    <form method="GET", action="/news/">
        <input type="text" name="search">
        <input type="submit" value="검색">

    </form>

    """		
input 박스에 검색어를 적으면 GET 방식으로 /news/ 뒤로 가게 된다  


## 02. Django에서의 HTML 템플릿 렌더링 (2)-HTML 파일을 읽어서 치환하기 		

그동안의 코드가 난잡해서 HTML 파일을 만들어서 불러와서 쓰자! 라는 생각을 하게 됨
- templates dir 만들기
- 기존에 views에서 하던걸 news.html으로 구현한 것  

	
    with open(settings.BASE_DIR+"/templates/news.html", "r") as template:
        content = template.read()		

> `open("../../templates")` 형식은 장고에서 쓸 수 없으므로 settings.BASE_DIR에 스트링 형식으로 정확한 주소를 찍어줌
> BASE_DIR을 아는 방법: `python manage.py shell`에 들어가서 
> 		import django.conf import settings		
> 		settings.BASE_DIR				

> 을 찍어보면 알 수 있다 (장고에서 그렇게 쓰기로 약속한 것)


*git으로 복구하기*
> commit을 안했다면 git으로 다시 복구 할 수 있다.
> 어떻게?		

*HTML에서 ## sth ##*   
HTMl에서 지정해 놓은 특정 변수 (##으로 임의로 하였다)에 count, content, site_name 등을 넣고 views.py에서 replace() 함수를 활용하여 내용을 추가해 줄 수 있다.	
	
        content = template.read()
        site_name = "seulchan's blog"
        content = content.replace("## site_name ##", site_name)		


*중복되는 코드 없애기*		
- wpsblog/ 하위에 `renderer.py` 파일을 만들고
- render 함수를 정의하여 중복을 최대한 줄였다.
- header, footer도 html로 만들어서 링크를 걸었다.
	```
	def render(template_name, context): # template_name에서는 사용하는 템플릿 명을, context에는 ##으로 받아줄 내용을 딕셔너리로 넣었다.
		header_content = open(settings.BASE_DIR + "/templates/header.html", "r").read()
		footer_content = open(settings.BASE_DIR + "/templates/footer.html", "r").read()
			
		with open(settings.BASE_DIR + "/templates/"+ template_name + ".html", "r") as template:
			content = template.read()
			content = content.replace("## header ##", header_content)
			content = content.replace("## footer ##", footer_content)
			for key, value in context.items():
				content = content.replace(
					   "## " + key + " ##", value 
						)
		return HttpResponse(content)
	```

- 이렇게 하고 실제 views에서는 코드를 간략하게 바꾸었다.

	```	 
	def home(request):
		return render("home", {"site_name":"seul's blog"}) # 템플릿 명으로 home을, home.html의 site_name에 맞는 내용을 딕셔너리로 넣어주었다.
	```
**tip? how to write comment inside markdown code**
> just write 3 \`\`\` (beside num 1)
> if not, you can't see #(comment in python) comment 

<<<<<<< HEAD
---

## 03. Django에서의 HTML 템플릿 렌더링 (3) - 장고 내장 함수로 구현하기		

이런 걸 하는 이유: 장고에서 기본적으로 템플릿 렌더링을 해줌. 그냥 쓰면 의미가 없고 그 원리를 알아야함!		

- renderer.py를 지우는 것부터 시작.
- templates/ dir 지움. (마지막에 다시 구현 해볼것!)
- INSTALLED_APPS에 app_name 추가해줌: 장고 템플릿 사용 뿐 아니라 다양한 이유가 있음, -> 장고 템플릿 사용할 준비 완료		
- 장고에서 직접 템플릿 로더를 불러서 사용 가능


  	from django.template import loader
			 
	def home(request):
		template = loader.get_template("home.html")
		return HttpResponse(
				template.render(
					{"site_name":"seul's blog"},
					request,
					)
				)

- 장고 안에서 이미 구현되어 있는 render 함수를 써서 표현 가능하다. (html 파일에서는 {{ }} 장고 템플릿을 쓰면 된다.)

- 장고 템플릿의 많은 기능; `count`와 같은 애들을 쉽게 쓸 수 있다.		
> [built-in django templatetag]() 참고

- 이제 news_list의 기능들을 장고 템플릿으로 만들어주기
검색에 대한 부분을 빼고 HTML 기능들을 넘기기
=> news_list를 넘겨주고 장고 템플릿에서 {% %}와 같은 장고 템플릿 엔진을 사용		

	<p> {{ news_list|length }} 개의 영화 정보가 있습니다. </p>

	{% for news in news_list %}
	<li>
		<h2> {{ news.title }} </h2>
		<p> {{ news.content }} </p>
		<img src="{{ news.image }}"/>
	</li>
	{% endfor %}


	def news(request):

		search =  request.GET.get('search') 

		url = "https://watcha.net/home/news.json?page=1&per=50"
		response = requests.get(url)
		
		news_dict = json.loads(response.content)
		news_list =  news_dict.get('news')

		template = loader.get_template("news.html")
		if search:
			news_list = list(filter(
				lambda news: search in news.get('content'), 
				news_list,
				))
		
		return HttpResponse(template.render(
			   {
				   "news_list": news_list,
				   },
			   request,
			   ))

> 그 외에 mustache, jinja2(python에서 많이 쓰임), JADE(태그 이름을 적으면 바뀜, javascript 계열에서 많이 쓰임) 등의 템플릿 엔진이 있음
> 위에서 쓴건 장고 템플릿 엔진


**header, footer 추가하기**
- 기존에 장고 템플릿에서 지원하는 {% include %} 형식을 사용해서 해주면 됨
- 더 나은 방법은? 
> 거의 모든 홈페이지에서 header, footer는 사용함		
> 그래서 상속의 형태로 사용 가능하게 함.
- `{% block name %}` 형태로 만들어서 상속
- `{% extends "base.html" %}` 으로 확장 후, {% block content %}에 내용을 넣어 주면 됨.


 




  
=======
>>>>>>> 9a69d5aa52d8db5ca1d6b20599c4975925bc8b54
