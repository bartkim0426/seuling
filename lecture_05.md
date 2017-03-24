## 5강

### 01. Django_Setting_Module을 이용해서 장고 세팅 관리하기    

**일단 runserver 할 때 development 파일 불러오는 방법**


1. 환경 변수 (Environment variable)
- DJANGO_SETTINGS_MODULE을 수정하여 기본 값을 확인 가능
- manage.py에서 확인할 수 있다. 근데 이 값을 바꿔버리면 default로 개발 버전이 사용이 되기 때문에 manage.py를 바꾸지 않고 환경 변수를 지정해준다.
- 환경 변수 지정은 다음과 같다.
`export DJANGO_SETTINGS_MODULE='wpsblog.settings.deelopment'`   
- 이제 runserver를 실행시켜보면 `using settings 'wpsblog.settings.development'`라는 말이 뜨면서 개발 버전의 서버가 실행될 것이다.     
- 이를 매번 등록하기 귀찮기 때문에 `.env` 파일에다가 등록 해두면 폴더 들어올 때마다 설정이 될 것이다.

- 엄청 큰 의미가있다! pyenv와 비슷한 의미를 가지는데 ...
> 일관된 명령어 => python manage.py runserver
> 하지만 환경 변수에 따라서 자동으로 선택이 되고 나중에 테스트까지 될 것! 


2. alias를 활용
**alias**   
- 자주 쓰는 명령어를 쉽게 쓸 수 있도록 하는 것    
- `alias ll="ls -al"`하면 ls -al 대신에 ll을 사용 가능하다! 

```
alias m="python wpsblog/manage.py"
alias ms="python wpsblog/manage.py shell"
alias mrs="python wpsblog/manage.py runserver"
```
- 원래는 shell을 끄면 사라지기 때문에 bash_profile, zsh_profile 파일에 넣어두면 좋다.   

- 다음은 예시들   
```
alias ll="ls -al"
alias p="python"
alias ip="ipython"
```
- 자주 쓰는 명령어는 등록해놓고 써야겠다. (git 같은것도..)   
- 현재 적용된 alias: oh my zsh때문인데 기본 설정이 뭔지 아는것이 중요하다!!!    
```
-='cd -'
...=../..
....=../../..
.....=../../../..
......=../../../../..
1='cd -'
2='cd -2'
3='cd -3'
4='cd -4'
5='cd -5'
6='cd -6'
7='cd -7'
8='cd -8'
9='cd -9'
_=sudo
afind='ack -il'
d='dirs -v | head -10'
g=git
ga='git add'
gaa='git add --all'
gapa='git add --patch'
gau='git add --update'
gb='git branch'
gba='git branch -a'
gbd='git branch -d'
gbda='git branch --no-color --merged | command grep -vE "^(\*|\s*(master|develop|dev)\s*$)" | command xargs -n 1 git branch -d'
gbl='git blame -b -w'
gbnm='git branch --no-merged'
gbr='git branch --remote'
gbs='git bisect'
gbsb='git bisect bad'
gbsg='git bisect good'
gbsr='git bisect reset'
gbss='git bisect start'
gc='git commit -v'
'gc!'='git commit -v --amend'
gca='git commit -v -a'
'gca!'='git commit -v -a --amend'
gcam='git commit -a -m'
'gcan!'='git commit -v -a --no-edit --amend'
'gcans!'='git commit -v -a -s --no-edit --amend'
gcb='git checkout -b'
gcd='git checkout develop'
gcf='git config --list'
gcl='git clone --recursive'
gclean='git clean -fd'
gcm='git checkout master'
gcmsg='git commit -m'
'gcn!'='git commit -v --no-edit --amend'
gco='git checkout'
gcount='git shortlog -sn'
gcp='git cherry-pick'
gcpa='git cherry-pick --abort'
gcpc='git cherry-pick --continue'
gcs='git commit -S'
gcsm='git commit -s -m'
gd='git diff'
gdca='git diff --cached'
gdct='git describe --tags `git rev-list --tags --max-count=1`'
gdt='git diff-tree --no-commit-id --name-only -r'
gdw='git diff --word-diff'
gf='git fetch'
gfa='git fetch --all --prune'
gfo='git fetch origin'
gg='git gui citool'
gga='git gui citool --amend'
ggpull='git pull origin $(git_current_branch)'
ggpur=ggu
ggpush='git push origin $(git_current_branch)'
ggsup='git branch --set-upstream-to=origin/$(git_current_branch)'
ghh='git help'
gignore='git update-index --assume-unchanged'
gignored='git ls-files -v | grep "^[[:lower:]]"'
git-svn-dcommit-push='git svn dcommit && git push github master:svntrunk'
gk='\gitk --all --branches'
gke='\gitk --all $(git log -g --pretty=%h)'
gl='git pull'
glg='git log --stat'
glgg='git log --graph'
glgga='git log --graph --decorate --all'
glgm='git log --graph --max-count=10'
glgp='git log --stat -p'
glo='git log --oneline --decorate'
globurl='noglob urlglobber '
glog='git log --oneline --decorate --graph'
gloga='git log --oneline --decorate --graph --all'
glol='git log --graph --pretty='\''%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'\'' --abbrev-commit'
glola='git log --graph --pretty='\''%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'\'' --abbrev-commit --all'
glp=_git_log_prettily
glum='git pull upstream master'
gm='git merge'
gmom='git merge origin/master'
gmt='git mergetool --no-prompt'
gmtvim='git mergetool --no-prompt --tool=vimdiff'
gmum='git merge upstream/master'
gp='git push'
gpd='git push --dry-run'
gpoat='git push origin --all && git push origin --tags'
gpristine='git reset --hard && git clean -dfx'
gpsup='git push --set-upstream origin $(git_current_branch)'
gpu='git push upstream'
gpv='git push -v'
gr='git remote'
gra='git remote add'
grb='git rebase'
grba='git rebase --abort'
grbc='git rebase --continue'
grbi='git rebase -i'
grbm='git rebase master'
grbs='git rebase --skip'
grep='grep  --color=auto --exclude-dir={.bzr,CVS,.git,.hg,.svn}'
grh='git reset HEAD'
grhh='git reset HEAD --hard'
grmv='git remote rename'
grrm='git remote remove'
grset='git remote set-url'
grt='cd $(git rev-parse --show-toplevel || echo ".")'
gru='git reset --'
grup='git remote update'
grv='git remote -v'
gsb='git status -sb'
gsd='git svn dcommit'
gsi='git submodule init'
gsps='git show --pretty=short --show-signature'
gsr='git svn rebase'
gss='git status -s'
gst='git status'
gsta='git stash save'
gstaa='git stash apply'
gstc='git stash clear'
gstd='git stash drop'
gstl='git stash list'
gstp='git stash pop'
gsts='git stash show --text'
gsu='git submodule update'
gts='git tag -s'
gtv='git tag | sort -V'
gunignore='git update-index --no-assume-unchanged'
gunwip='git log -n 1 | grep -q -c "\-\-wip\-\-" && git reset HEAD~1'
gup='git pull --rebase'
gupv='git pull --rebase -v'
gwch='git whatchanged -p --abbrev-commit --pretty=medium'
gwip='git add -A; git rm $(git ls-files --deleted) 2> /dev/null; git commit --no-verify -m "--wip-- [skip ci]"'
history='fc -l 1'
l='ls -lah'
la='ls -lAh'
ll='ls -lh'
ls='ls -G'
lsa='ls -lah'
md='mkdir -p'
please=sudo
po=popd
pu=pushd
rd=rmdir
run-help=man
which-command=whence
```

**Django-extensions**
1. pip 추가하기
2. INSTALLED_APPS에 추가

[django-extensions page](https://github.com/django-extensions/django-extensions)

다양한 기능들을 제공   
- m show_urls   
보기 힘든 url들을 보기 쉽게 정돈해주고, 어떤 파일에 어떤 namespace를 가지고 있는지 보여준다.     

```
/policy/disclaimer/     wpsblog.views.policy.disclaimer policy:disclaimer
/policy/privacy/        wpsblog.views.policy.privacy    policy:privacy
/policy/terms/  wpsblog.views.policy.terms      policy:terms
/rooms/<room_id>/       wpsblog.views.room.room room
```
이런 형태로 결과물이 나오게 된다.   

- manage.py는 어떻게 동작하는 것일까?   
`/django/core/management/base.py` 에서 BaseCommand를 상속을 받아서 만들어보면 장고에서 사용 가능하게 만들어져 있다!   

- 즉, `python manage.py _____`라는 명령어를 통해서 management, commands 안의 _____ (함수명)으로 불러오는 구조이다.

- wpsblog/management/command/를 만들어서 직접 hello 명령어 구현하는 방법    
우선 다음 폴더, 파일 들을 만들어본다.

```
wpsblog/management/__init__.py
wpsblog/management/command/__init__.py
wpsblog/management/command/hello.py
```
그 다음 hello.py에 django.core.management에서 받아온 basecommand를 활용하여 새로운 manage.py 명령어를 등록한다.

```
from django.core.management.base import BaseCommand

class Command(BaseCommand)

  def handle(self, *args, **options):
      self.stdout.write("hello world")
```
이제 python manage.py의 명령어를 실행시켜 보면 `wpsblog`로부터 `hello`라는 코맨드를 불러올 수 있는 것을 확인 가능하다. 

### 02. Post Model 생성하기   

모델이 엄청나게 중요하다!!!    

원래는 SQL (Structured Query Language )를 통해서 디비에서 가져왔다.    
이는 RDB (관계형 데이터베이스)의 모든 프로그램이 마찬가지이다.     

하지만 장고에서는 SQL ... Python을 어떤식으로 묶어 놓았기 때문에 => SQL 문법 없이 할 수 있다. 이를 ORM이라고 부르는데,

> ORM ( Object Relation Mapping )
> - Object와 관계를 매핑한다
> - 각각의 colmun들이 세로로 있고
> - 각각의 low들이 하나의 줄 정보가 있다. 
> - 파이썬의 class와 굉장히 유사: Class(object) ... Excel(DB) 를 연결시킴    
> - 이제 SQL이 아니라 class를 짜면 된다! 장고에서 이를 자동으로 읽어서 데이터베이스를 만들어줌

장고는 장고 자체적인 ORM을 사용, 설정해야 할 것은 아무것도 없다.     
규칙에 맞게 코드를 짜기만 하면 된다: 어떤 규칙을 가지고 있고, 어떻게 사용하는지를 배운다.    

1. 변동 사항을 정확하게 기록하는 것
(makemigrations)
`python manage.py makemigrations wpsblog`
- migrations라는 폴더가 생긴다.   
- 이 폴더 아래 0001_initial.py가 생겼다.
- 즉, models.py 는 initial.py를 만들어주는 명령어 같은 것이다.    
- 데이터베이스가 한번에 변동되는 것이 아니라, 정확하게 DB를 기록을 해서 저장을 해 뒀다가 나중에 migrate 명령어로 적용시키는 것
- 어떻게 migration 파일을 잘 나누는지, 어떤 시점에 DB를 업데이트 시킬지가 매우 중요한 문제이다... (추후에 배포할 때)

2. 기록된 변동 사항을 DB에다가 반영하는 것
(migrate)
`python manage.py migrate`    
- 앱 이름을 안 붙임: 모든 변화에 의해서 적용됨
- 

**post list, detail 페이지 만들기**
- 우선 view 단에서 posts를 해체해서 만든다.    
`posts/__init__.py, detail.py, list.py`

그리고 render 함수를 활용, Post 모델을 불러서 함수를 만든다. 

```
from django.shortcuts import render

from wpsblog.models import Post


def list(request):
  return render(
         request,
         "posts/list.html",
         {}
  )
```   
- 그리고 위에서 지정한 html에 맞는 html을 생성한다.    
`templates/posts/list.html, detail.html`
각각의 html은 base.html을 상속하여 만들고, content에 내용을 넣어준다.

```
{% extends "base.html" %}
{% block content %}
<h1> Post List </h1>

{% endblock %}
```   
- 그리고 이제 `{{ }}`와 같은 장고 템플릿 태그를 활용하여 넣을 내용을 생각한다. List page에서는 각각의 post를 모두 불러와서 for 문을 돌리면 되므로 `list.py`에다가
```
...
{"posts": Post.objects.all()}
...
```     
로 가져와 주고, `list.html`에다가는     
```   
...
{% for post in posts %}
<h2> {{ post.title }} </h2>
<p> {{ post.content }} </p>
{% endfor %}
... 
```   
라고 넣어주면 된다. `detail.py` 페이지도 마찬가지로 사용하면 된다.   

- list.html에다가 각각의 디테일 페이지로 링크를 걸기 위해서는 for문 안에다가     

```
...
<a href="/posts/{{ post.id }}"> {{ post.title }} </a>
...
```
를 넣어주면 된다. `{% url template_namespace agv1 agv2 %}` 방식으로 하려면 다음과 같이 하면 되는데 잘 안된다...     
`<a href="{% url 'post-detail' post_id=post.id %}"> {{ post.title }} </a>`    

그런데 이런 방식은 view, html이 무겁기 때문에 모델을 최대한 무겁게 만들어 줘야 한댄다... (수찬님이)   

- 그래서 위의 url 기능을 models.py로 옮길 수 있다.   
`models.py`에다가 `def get_url()`을 추가한다..    
```
...
def get_url(self):
  url = "/posts/" + str(self.id) + "/"
  return url
...
```   
이렇게 한 다음 `detail.html`에다가   
`<a href="{{ post.get_url }}"> {{ post.title }} </a>`   
를 해주면 완벽하게 url이 불러진다. (장고 템플릿에서 불러와주면 함수가 자동으로 계산이 되서 불러진다.)    

- 그러나 이 url이 바뀌면 코드가 다 바뀌어야 한다는 단점이 있다.   
그래서 나온 것이 django.url.base에 있는 reverse라는 기능이다.     
ipython에서 reverse 함수를 사용 해 보면, `reverse('viewname', args, kwagrs...)`와 같이 사용 가능하다.    
```
reverse('post-list') # 이러면 결과로 /posts/가 나온다.
reverse('post-detail', kwargs={'post_id':1}) #  이러면 /posts/1/ 이 나온다
```   
이런 방식으로 사용할 수 있는데, 이를 장고에서는 get_absolute_url이라고 관습적으로 부른다.    

그래서 완성된 models.py의 함수는
```
def get_absoute_url(self):
  return reverse(
         'post-detail',
         kwargs = {'post_id':self.id},
  )
```   
이다.


**과제**  
https://search.naver.com/search.naver?where=post&sm=tab_jum&ie=utf8&query=파이썬
namer post라는 Model: title, thumbnail_image_url, summary, content, original url들의 정보를 크롤링하여 데이터베이스에 넣고   
(NaverPost.objects.create()로 시작...)   
크롤링을 해주는 명령어
`python manage.py crawl_naver "프로듀스101"`
=> 이에 대한 정보가 크롤링되어 DB에 들어가게...    
여기에 대한 리스트 페이지를 입력하기...

https://docs.djangoproject.com/en/1.10/howto/custom-management-command/ 에서 특정 값을 입력 받을 수 있도록...   


