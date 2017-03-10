## 01. Django 개발 환경 설정하기- pyenv, vertualenv, autoenv, gitignore

*blog 폴더에 가상환경 설치*		
	$pyenv virtualenv 3.6.0b1 blog # 가상환경 생성하기, 파이썬 버전은 맘대로		
								   # pyenv versions로 파이썬 버전 확인 후 설치		
	$pyenv activate blog #blog 가상환경 활성화하기				
	$pip freeze # 가상환경을 초기화했기 때문에 패키지가 없어야한다.	


> 파이썬의 모든 패키지는 pypi에 있는 걸 쓴다.		

autoenv => .env라는 파일을 만들어야한다.

	`touch .env # .env 파일 생성
	`vim .env # .env 파일 수정

	---- .env ----- 
	echo "Activate blog virtualenv" 
	pyenv activate blov # 이제 blog 폴더에 접근할 때 이 명령어가 실행됨
	


> *Q).env를 github에 올려야하나 말아야하나?*	> pyenv, virtualenv가 아닌 다른 버전관리를 사용할 수 있기 때문에 개인화된 설정은 깃허브에 올리지 않는다.  > `git status`시 계속 .env가 뜨니깐 .gitignore에 추가해주면 됨
> 더 좋은 방법: 이미 gitignore 템플릿이 존재함 		
> [git ignore](https://github.com/github/gitignore)

깃허브에서 특정 파일을 받고 싶을 때는 Raw를 누르면 나오는 주소 복사, 그리고 wget 명령어로 다운로드		


	wget https://github.com/github/gitignore/blob/master/Python.gitignore
	mv Python.gitignore .gitignore # gitignore 파일로 쓰기		



.gitignore 파일에 이미 .env를 제외시키는 설정이 되어 있으므로 이를 깃에 그대로 커밋			
	
	git add .gitignore
	git commit -v
	git push origin master

\# **작업 전에 이렇게 환경을 설정해주는 것이 중요! 습관을 들이자!!**


remote는 가장 완벽한 상태에서 올려야한다			  
	
	
	git add . #절대로 쓰지 마라! 모두 올리는건 좋지 않다.		
	git status #  Changes to be commitred 라고 뜨면 커밋 전 상태, 이를 내리려면			
	git reset HEAD file_name #이렇게 하면 다시 내려진다.		

*장고 설치하기*		

	`pip install Django`		   
	`pip freeze`    
- python 명령어에서 	
	`import django`# 오류가 없으면 잘 설치된 것				
	`django`  			
	`<module 'django' from '/home/seul/.pyenv/versions/blog/lib/python3.6/site-packages/django/__init__.py'>` # .pyenv 안에 장고가 설치된 것!

- 팀원은 어떤 패키지를 설치한지 모름... 이를 해결하는 법? 다음에서!

---
## 02. 파이썬 패키지 의존성 관리: requirements.txt		
- 설치할 패키지를 README.md 에 적는 방법 => 패키지가 많아지면 비효율적		
- `python_package.sh` 파일을 만들어서 `$source python_package.sh`
> 위 파일을 chmod를 활용해서 실행할 수 있게
> `$ls -la python_packages.sh`를 통해 r, w 권한을 확인하기		
> `chmod` 명령어(change mod)를 활용해서 바꾸기		
```
$chmod 744 python_packages.sh # 744 권한으로 변경
$chmod +w python_packages.sh # 쓰기 권한 추가, 보통 이렇게 사용함
```

*ipython 깔기*		
`python_packages.sh`에 `pip install ipython` 추가 한 후 파일 실행 	

> `sh` 명령어: shell script 명령어	
> 실행할 때 `$./file_name.sh`로 실행시키기만 하면 됨		
> 이를 바로 실행 가능 한 형태로 바꾸기 위해서 `chmod +w` 명령어 사용함  
> source: 파일을 읽어서 한 줄로 실행시키는 명령어, 즉 'r' 권한  
> ./filename.sh => 그 파일 자체를 실행하는 것, 즉 'w' 권한  
> ./ (slash)는 현재 폴더를 명시함, 관례적으로 사용하는 것   	

curl | source 뜻
> `curl http://dobest.io/scr/python_packages.sh|source`		
> 프로그램을 설치할 때 파일을 받아 소스를 실행하고 제거시키기 		
> `curl`: 해당 페이지를 보여주고 바로 사라짐  
		

그럼 이것은 좋은 방법인가? 
> 만약 패키지가 계속 늘어나면, 일일히 써야 하기 때문에 
> pip 내장 기능을 제공해줌
> requirements.txt: 파이썬 패키지를 pip 내장 기능으로 설치시켜주는 텍스트 파일을 관례적으로 이렇게 부름
> `pip install -r requirments.txt`		

이 requirements.txt는 완벽한 방법?
> `pip freeze`의 결과와 동일하다 => 가장 완벽한 방법으로 바꾸자   
> 그래서 `pip freeze`의 결과를 => requirements.txt로 바꾸게		
> `pip freeze > requirement.txt` => 좋은 방법? no, 쓰고 있는 패키지 말고 다른 패키지들도 포함, 순서도 섞여있음.    

> 실제 배포할 때는 메모리를 줄여야 하기 때문에, 모두 다 설치하면 안 좋음		
> 그래서 나누는 것: 개발버전,(development.txt) 배포버전(requirements.txt) => 관리하기가 까다로움... 		
>> `pip install -r`을 활용하기:   
- 배포버전(기능별로- crawling.txt, documentation.txt 등...)별로 나눠서 production.txt에 배포용 패키지를 넣고  
- 개발버전(development.txt)에는 개발용을 넣어주면 됨
- 처음부터 완벽하게 해 놓고 관리해야 나중에도 관리가 된다!!!		

#### *package 의존성 관리 정리*
- requirements/ dir 안에 `development.txt`, `production.txt`를 추가
- `development.txt`는 개발용(모든 패키지) 패키지를 넣고, 		
	-r production.txt	# production 패키지를 읽는다는...
- `production.txt`는 배포용 패키지를 넣는다.그리고 추가적으로 상위 폴더에  `requirements.txt`를 만들고 `-r requirements/production.txt` 내용을 넣는다. (추후 자동화를 위해서)		


*Django 시작*
- Django => Full Stack Backend Framework: 각각에 맞춰서 초기 세팅을 모두 해 줘야함: "scaffolding"
- Flask => Micro Framework





## 03. Django 프로젝트 초기화하기 - 간단한 뷰		

* Project => 우리가 개발하고 있는 최종 큰 프로젝트
* Application => 프로젝트에 포함된 작은 소스 (MVC Framework ...)		

ex) project 'Facebook'
- application 'users'
- applicateion 'posts' => users에 대한 의존성
- application 'messages' => users 의존성 
- application 'page' ... # 다양한 어플리케이션으로 프로젝트 구성		
>  각각의 applicataion들이 의존성을 가짐  	

	$django-admin startproject wpsblog # wpsblog 프로젝트 생성			
	
이후 db.sqlite3 파일은 .gitignore에 등록,

urls.py, settings.py, manage.py 등이 처음에 생김		

> MCV
> M: Model(DB): Data & Business Logic
> V: View: Template/Client
> C: Controller: View, Model... 
> Model => 더 무겁게
> Controller => 더 가볍게 (즉, 기능이 Controller => Model ...)		

MVC 외에도		
MVVM => Model View View Model		
MVW => Model View Whatever ... 와 같은 다양한 방법론이 있음			

*Hello World* 출력하기		
MVC 중 Controller: 		

	from django.http.response import HttpResponse 	
	def home(request):		
		return("Hello world")	

\# 장고에 이미 만들어져 있음 (response) 		
[django github](https://github.com/django/django)		

### *urls.py* 안에 컨트롤러를 넣어도 됨.
- 정규표현식을 사용해야함: 		
	`url(r'$', home),`		
	
- runserver 끄기		
	ps aux | grep runserver		
	kill -9 id_value		
(-9는 강제 종료, man kill 하면 명령어 확인 가능)		

> 지금까지 hello world를 출력하는 조그만 기능 만듬. 바로바로 commit 해주기

> commit시 push 할 때 마다 로그인 안되게 하는 법:
	```
	# 메모리에 인증정보를 캐싱 하도록 설정 (15분 기억)			
	git config --global credential.helper cache			

	# 캐시 타임아웃을 1시간으로 설정 (초단위 설정)		
	git config --global credential.helper 'cache --timeout=3600' 		
	```

### *room/123* url 만들기		
- localhost:8000/rooms/123 		
- urls.py 파일에다			

	def room(request, room_id): # room_id를 받기 때문에 받아줘야함
		return HttpResponse("This is a room detail " + room_id)		

- urlpatterns에다가			
	url(r'^rooms/(?P<room_id>\d+)/$', room), # 추가하기		


### wpsblog/controller의 역할을 하는 controller.py 만들고 기능 옮기기 	
- wpsblog/ (main dir) 안에서 controller.py 만들기
- home, room 함수 추가하기
- urls.py 폴더에 controller의 함수 불러오기
	`from wpsblog.controller import home, room`		
- controller.py => views.py: Django에서는 MVT 모델이기 때문에


### 직방 api를 활용해서 room id를 가져오는 페이지 만들기		
- requests 추가하기		
	`pip install requests`
- 함수 만들기: 직방 api를 받아오기			
	```
	def room(requesst, room_id):
		url = "https://api.zigbang.com/v1/items?detail=true&item_ids=" + room_id
		response = requests.get(url)
		return HttpResponse(response.content)
	```
- json 코드가 아니라 예쁘게 안나옴 => 우리가 json이라고 명시해줘야함	
	`content_type="application/json",`		
이렇게 추가해주면 바꿔줌		
>	`curl localhost:8000/rooms/123 -I # 정보를 확인할 수 있음
> curl이 아닌 웹 브라우져 => Network 항목에서 Response Header에 Content_Type을 확인할 수 있음.
> 현재 장고 1.10 버전에서 적용이 되지 않아 문제 해결중 => migrations, migrate 하자 브라우저 상에서는 바뀌는데 curl 상에서는 바뀌지 않음		


\# 숙제: PEP0008 문서		
- [PEP 8]()을 읽고 settings.py 등을 수정하기
- watcha api: news.json (network 항목에서 찾기) => 50개의 뉴스정보, 이미지들이 나옴. => 장고에서 하나의 페이지로 어떻게 띄울 수 있을지 고민. 
- 힌트: hello world에 <h1>'hello world'/</h1> 이면 html처럼 뜬다. 어떻게 하면 movies라는 url에서 어떤 view를 작동시켜서 html을 만들 수 있을지?
