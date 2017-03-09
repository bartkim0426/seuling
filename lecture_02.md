---
## 01. Django 개발 환경 설정하기- pyenv, vertualenv, autoenv, gitignore

*blog 폴더에 가상환경 설치*		
	```
	$pyenv virtualenv 3.6.0b1 blog # 가상환경 생성하기, 파이썬 버전은 맘대로		
								   # pyenv versions로 파이썬 버전 확인 후 설치		
	$pyenv activate blog #blog 가상환경 활성화하기		
	$pip freeze # 가상환경을 초기화했기 때문에 패키지가 없어야한다.	
	``` 


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


