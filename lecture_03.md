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
		
    search =  request.GET.get('search') 
    print(search)
		

=> GET 방식으로 'search'라는 리퀘스트를 request 변수로 설정,		(만약 search가 있다면) search를 프린트		
=> 즉, request.GET 방식으로 보내진 'search' 쿼리를 get 하라는 명령어이다		

 
