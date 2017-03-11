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


