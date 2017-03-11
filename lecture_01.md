***

## 01. HTTP Method(GET, POST) & RESTful API
API: API 서버와 클라이언트를 연결해서, 특정 기능을 수행해주는 녀석

requests.get(..) => get(가져온다)  

HTTP Method Name ()
- GET (requests.get)
- POST
- HEAD ...

http://  
- 정보: item_ids = 123... 이런식으로 api
- 네이버 검색: https://search.naver.com/search.naver?ie=UTF-8&query=%EC%95%84%EC%9D%B4%EC%98%A4%EC%95%84%EC%9D%B4  
정보:
- query = 아이오아이
- where = nexearch
- sm = top_hty
- HTTP Method => GET => URL parameter를 통해서 정보를 넘기는 방식    

URL에 안 넘는 방식
- HTTP Method => POST => HTTP Body 안에 정보를 담아서 보내는 방식
- (암호화랑 상관 없음, 데이터를 보내는 방식을 얘기함)
	
어떤 방식으로 정보를 보낼건지, 어떻게 API를 구성할 건지를 생각해야 한다.	
	
HTTP Method, Body, URL ( Endpoint ), => HTTP Response, status_code, body	
이런걸 제대로 정의하는 방법을 : RESTful 한 설계 (RESTful API)	
> Representational State Transfer


정확한 API : 좋은 구현과 안좋은 구현의 차이를 알아볼것이다.		

### 각각의 방식들이 언제 쓰이는지?
- GET => 가져온다 => 조회, 검색 ( 데이터의 상태가 바뀌지 않으면서, 정보를 가져올 때) ( Retrieve/ Read )
- POST => 추가 ( 생성 ) => 웹 상의 리소스가 생길 때 ( Created ) 
- PUT / PATCH => 데이터가 업데이트 될 때 ( Update ) 
- DELETE => 데이터가 삭제 될 때 ( Destroy )

###  API에 요청할 때, status_code, body
- POST => Successful(201), Failed
- GET => Successful(200), Failed
- Patch ...
- Delete ...

***

## 02. Slack API		

requests, json 사용해서 slack에 자동 메세지 보내기(slack api)

1. 우선 slack api 중 incoming WebHooks을 채널에 추가한다.
2. 추가한 뒤 나와있는 내용에 따라 json 형식의 데이터를 post 방식으로 보낸다. (postman, jupyter 활용 가능)


*jupyter code*

	```
	import requests
	import json
	data = {
		"text": "hello world!",
		"username":"slackbot", # default
		"channel":"#text", #default
	}

	response = requests.post(
	"https://hooks.slack.com/services/..." # 본인의 API에 있는 코드 사용
	data = json.dumps(data)
	)
	```
    

*json.dums(data)를 해준 이유*		
JSON: JavaScript Object Notation		

data는 dict 형태이기 때문에 json 형태의 데이터(str)으로 만들어 주기 위해서		
- json.loads(): str => dict
- json.dumps(): dict => str


---

## 04. Slack + Github		

github를 폴더와 연동시켜 커밋하는 방법과, 커밋시 슬랙에 자동으로 메세지를 보내는 API를 활용해보았다.		

*git 사용하기*		
- blog 폴더 만들기: github과 연동할 폴더		
- git init
	```
	git init # git 초기화하기: ls -al로 .git 폴더가 생긴 것을 알 수 있다.		
	vim README.md # README markdown 문서 생성	
	git status # 깃 상태 확인해보기
	```

Git 사용은 크게 세단계로 나눌 수 있다.
1. add (upstage)
2. commit (stage)
3. push (push): 기록되는 상태		

다음은 실제로 README.md 파일을 수정하여 깃에 등록하는 순서를 보겠다		

	
	git add README.md # README.md 파일을 커밋할 사항에 포함
	git commit -v # commit 실행, 후에 뜬 nano 파일에 커밋할 내용적기
				  # 본인에게 맞게 적으면 됨. 나는 init, add 등의 명령어를 사용하여 적음
	git remote add origin https://github.com/bartkim0426/test_blog.git 
	git push -u origin master # 깃에 올리는 과정
	


*github 변동 시 slack 메세지 받기*		

github에서 제공하는 hooks를 활용하여 만들 수 있다.		
> hook: 특정 이벤트가 발생하는 시점에 발생되는 기능, 이벤트 		

slack app에서 GitHub를 검색한 후 추가하고 원하는 채널을 설정해 놓으면 된다.		

[slack github 페이지](https://suwonseul.slack.com/apps/A0F7YS2SX-github)		








