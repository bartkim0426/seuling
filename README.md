# 블로그

Seul-ing blog

code-ing, seulcode
travel-ing, seultravel
movie-ing, seulmovie
book-ing, seulbook

## 목표

블로그를 정확하게 개발 후 유사한 프로젝트를 손코딩
수찬님 강의 완강하기
1일 1강 듣기

### 설치할 패키지
1. 일단 `Django`를 설치.
```
$ pip install django=1.10.6
```
- python_packages.sh: 패키지 적을 때마다 적으면 불편하기 때문에, 새로운 방법으로

```
$./python_packages.sh
```			
- 더 완벽한 형태의 패키지 관리: requirements.txt	
```
$pip install -r requirments.txt
```		
- 배포시의 메모리를 줄이기 위해 requirements/ 안에 배포용, 개발용 나누기  
```
$pip install -r requirements/development.txt # 개발시에
```

2. Django project scaffolding
```
$django-admin startproject wpsblog
```
