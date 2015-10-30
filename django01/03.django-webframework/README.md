# 3. Django 웹 프레임워크
- 파이썬 웹 프레임워크 중에서 가장 준비가 잘 되어 있는 프레임워크
- (MVC 패턴에 해당하는) MTV 패턴에 따라 개발하도록 설계되어 있다.


## 3.1 일반적인 특징
- (*) 현재 가장 많이 사용
    - (*) 2003년 : Lawrence Journal-World newspaper 웹 개발팀의 내부 프로젝트로 시작
    - (*) 2005년 : 오픈소스 프로젝트로 공개
    - (*) Google App Engine 에서 사용
- MVC 패턴 기반 MTV
    - MVC(Model-View-Controller) 기반으로, 용어만 다르지 개념은 동일
        - View --> Template
        - Controller --> View
    - Model-Template-View
- 객체 관계 매핑
    - ORM(Object-Relational Mapping)을 통해 다양한 데이터베이스 시스템 지원
- 자동으로 구성되는 관리자 화면
    - 데이터베이스 관리 기능을 위하여 기본 기능으로 관리자 화면을 제공 
- 우아한 URL 설계
    - 파이썬 프레임워크의 일반적인 Elegant URL 방식을 채택
- 자체 템플릿 시스템
- 캐시 시스템
    - 캐시용 페이지 : 메모리, 데이터베이스, 파일 시스템에 저장 가능
    - 캐시 단위 : 페이지, 사이트 전체, 특정 뷰의 결과, 템플릿의 일부 영역 지정 가능 
- 다국어 지원
- 풍부한 개발 환경
    - 테스트용 웹서버를 포함 --> 개발과정에서 아파치 등의 웹 서버가 없어도 테스트 진행 가능
    - 디버깅 모드 --> 상세 메시지 제공 등
- 소스 변경사항 자동 반영
    - *.py 파일의 변경 여부를 감시 


## 3.2 Django 프로그램 설치
- (*) 설치 과정은 운영체제 상관없이 동일
- Document
    - https://docs.djangoproject.com/en/1.8/intro/install/
    - https://pip.pypa.io/en/latest/
        

### 3.2.1 기존 Django 프로그램삭제
- (*) pip 프로그램으로 설치하는 경우 예전 버전의 장고를 자동으로 삭제해 준다.

- Django 설치 디렉토리 찾기
 
 
    $ python -c "import sys; sys.path = sys.path[1:]; import django; print(django.__path__)"
    
    
- Django 수동 삭제


    $ cd /Library/Python/2.7/site-packages/
    $ rm -rf django
    $ rm -rf Django*


### 3.2.2 pip 프로그램  설치
- (*) Python Install Program
    - 파이썬 오픈소스 저장소인 PyPI(Python Package Index)에 있는 패키지를 설치/관리

- get-pip.py 가져오기


    $ wget https://bootstrap.pypa.io/get-pip.py
    or 
    $ curl -O https://bootstrap.pypa.io/get-pip.py
    or 
    Browser --> https://pip.pypa.io/en/latest/installing/#install-pip

    $ sudo python get-pip.py

- Django 설치


    $ sudo pip install Django
    or
    $ sudo pip install Django --upgrade
    --> /Library/Python/2.7/site-packages/django


### 3.2.3 수동으로 설치
- Browser --> https://www.djangoproject.com/download/


    $ tar xvzf Django-1.8.5.tar.gz
    $ cd Django-1.8.5
    $ sudo python setup.py install


### 3.2.4 윈도우에서 Django 설치
- (*) Administrator 권한으로 설치 권장
- 3.2.3 과 동일


### 3.2.5 Django 프로그램 설치 확인

    $ python
    >>> import django
    >>> print django.get_version()


## 3.3 Django에서의 Application 개발 방식
- 전체 프로그램 --> Project
- 모듈화된 단위 프로그램 --> Application


### 3.3.1 MTV 패턴
- MVC --> MTV
    - View --> Template
    - Controller --> View
- 처리 과정
    - 클라이어트 요청 --> URL conf 모듈이 URL 분석 --> URL 처리를 담당하는 View의 로직이 수행
        - --> DB 처리가 필요하면 Model을 통해서 처리
    - --> View의 로직 처리 결과를 Template 을 사용하여 HTML 생성 --> HTML을 클라이언트에게 전송


### 3.3.2 Model - 데이터베이스 설계
- Model : 사용될 데이터에 대한 정의를 담고 있는 클래스
    - ORM(Object-Relational Mapping) 사용 <-- SQL 없이도 DB Access 가능
        - (*) Database Engine(SQLite3, MySQL, PostgreSQL, ...)을 변경하더라도 ORM을 통한 API 변결 불필요. 
    - (*) 직접 SQL을 사용해 Database의 데이터를 읽어올 수 있다.
- Model 클래스 --> Table
- Model 클래스의 Attribute --> Table's Column
- models.py 에 정의


### 3.3.3 Template - 화면 UI 설계
- 자체 Template 시스템을 가진다
    - 문법을 제공한다.
- Template 에서 Python 코드를 직접 사용 가능
- *.html 확장자를 가지며 적절한 디렉토리에 위치시켜야 한다.
    - TEMPLATE_DIRS 또는 INSTALLED_APPS 에 지정된 디렉토리를 지정된 순서대로 검색한다.
        - (*) settings.py (프로젝트 설정 파일) 에 정의되어 있다.


__settings.py__


    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'polls'
    )
    
    TEMPLATE_DIRS = ['/home/shkim/pyBook/ch03/templates' ]
    
    (순서) TEMPLATE_DIRS --> INSTALLED_APPS
        /home/shkim/pyBook/ch03/templates
        /usr/lib/python2.7/site-packages/django/contrib/admin/templates
        /usr/lib/python2.7/site-packages/django/contrib/auth/templates
        /usr/lib/python2.7/site-packages/django/contrib/contenttypes/templates
        /usr/lib/python2.7/site-packages/django/contrib/sessions/templates
        /usr/lib/python2.7/site-packages/django/contrib/messages/templates
        /usr/lib/python2.7/site-packages/django/contrib/staticfiles/templates
        /home/shkim/pyBook/ch03/pools/templates


### 3.3.4 URLconf - URL 설계
- 파이썬의 URL 지정 방식을 Elegant URL 이라고 부른다.
- urls.py
    - URL & 처리 함수(View)를 매핑


### 3.3.5 View - 로직 설계
- 웹 요청을 받고 응답을 반환해 준다.
    - ex) 웹 요청 --> 데이터베이스 접속 등 해당 애플리케이션의 로직에 맞는 처리 
          --> 그 결과 데이터를 HTML로 변환하기 위해 Template 처리 후 --> 최종 HTML로 된 응답 데이터를 클라이언트로 반환 
- 함수 또는 클래스의 메소드로 작성된다.
- views.py

## 3.4 프로젝트 뼈대 만들기
- (*) 용어의 개념을 웹 서버 개발 측면에서 좀 더 구체화하여 사용하고 있다.
- Project : 전체 프로그램
- Application : 프로젝트를 몇 개의 기능 그룹으로 나누었을 때 이 하위 서브 프로그램
    - Project 디렉토리와 Application 디렉토리를 구분하고 있다.
        - Project & Application : Python Package Directory에 해당한다. <-- "__init.py__" 이 존재하는 디렉토리
    - 하나의 Application이 여러 개의 Project에 포함될 수 있다. <-- 재사용
    - Project를 모아서 더 큰 Project를 만들수 있다.


### 3.4.1 프로젝트 생성
 

    $ django-admin.py startproject mysite
        - mysite/ : Project 관련 Directory/File 을 모으는 역할만 한다. --> 이름 변경 가능 --> ch3/ 로 변경
        - mysite/myste/ : Project Directory
    $ mv mysite ch3


### 3.4.2 애플리케이션 생성


    $ python manage.py startapp polls
    

### 3.4.3 데이터베이스 변경사항 반영
- Default : SQLite3 Database Engine 사용
- Django 는 모든 웹 프로젝트 개발시 반드시 사용자와 사용자 그룹 테이블이 필요하다고 가정하고 설계되었다. 


    $ python manage.py migrate
        - 사용자 / 사용자 그룹 테이블을  생성하기 위해
        - db.sqlite3 생성


### 3.4.4 지금까지 작업 확인하기
- runserver : 간단한 테스트용 웹 서버


__runserver__
    # 현재 명령을 실행중인 서버의 IP 주소로 웹 접속 요청을 받는 경우
    $ python manage.py runserver 0.0.0.0:8000
    
    Browser --> http://your.server.ip.address:8000
    
        # Default(127.0.0.1:8000)
        $ python manage.py runserver
        
        # Default(127.0.0.1) + 8888 port
        $ python manage.py runserver 8888
        
        # Background 에서 웹서버를 실행  
        $ python manage.py runserver 0.0.0.0:8000 &
    

__Admin 접속__


    Browser --> http://your.server.ip.address:8000/admin
    - 생성된 계정이 없어 접속 불가


__Administrator(Super User) 생성__


    $ python manage.py createsuperuser
        - djangoadmin / djangoadmin / a@b.com
        - Users, Groups 테이블 확인 가능
            - settings.py 에 django.contrib.admin 애플리케이션이 등록되어 있기 때
    

__Directory 확인_


    # Ubuntu Only
    $ tree ch3


## 3.5 애플리케이션 개발하기 - 설계
- 화면 UI 설계
    - View & Template 코딩
    - index.html / detail.html / results.html
- Table 설계
    - Model 코딩 
    - Question / Choice
- (*) 독립적으로 개발 가능한 Model 을 먼저 코딩 


## 3.6 애플리케이션 개발하기 - Model 코딩

__Procedure__


    # Database 지정
    $ vi settings.py
    
    # Table 정의 
    $ vi models.py
    
    # 정의된 Table을 Admin에서 보이도록 한다
    $ vi admin.py
    
    # 변경 사항 추출 
    $ python manage.py makemigrations
    
    # 변경 사항을 Database에 반영
    $ python manage.py migrate
    
    $ python manage.py runserver


### 3.6.1 데이터베이스 지정
- settings.py 확인 
    - DATABASES
        - DATABASES.default.ENGINE : sqlite3
        - DATABASES.default.NAME : db.sqlite3
    - (*) 프로젝트의 애플리케이션들은 모두 설정 파일에 지정되어야 한다
        - INSTALLED_APPS.polls
    - (*) Timezone
        - TIME_ZONE : UTC --> Asia/Seoul


### 3.6.2 테이블 정의
- polls 애플리케이션은 Question & Choice 두 개의 테이블 필요
- polls/models.py
    - django.db.models
        - Model
        - CharField
        - DateTimeField
        - IntegerField
        - ForeignKey


### 3.6.3 Admin 사이트에 테이블 반영
- polls/admin.py
    - admin.site.register()


### 3.6.4 데이터베이스 변경사항 반영


    $ python manage.py makemigrations
    $ python manage.py migrate
    
    # Django가 사용하는 SQL 확인 가능
    $ python manage.py sqlmigrate polls 0001


### 3.6.5 지금까지 작업 확인하기
- Open http://your.com.ip.address/admin


## 3.7 애플리케이션 개발하기 - View 및 Template 코딩
- URL & View
    - 항상 1:1 관계로 매핑
    - URL/View 매핑을 URLconf 라고 한다
    - urls.py
- URLconf 설계
    - /polls/           : index()
    - /polls/5/         : detail()
    - /polls/5/votes/   : vote()
    - /polls/5/results/ : results()
    - /admin/           : Django


### 3.7.1 URLconf 코딩
- polls/urls.py
    - django.conf.urls.patterns()
    - django.conf.urls.url()
- mysite/settings.py
    - ROOT_URLCONF : Django 가 URL 분석시 이 곳에 정의된 urls.py 를 가장 먼저 분석


### 3.7.2 View 함수 index() 및 템플릿 작성
- polls/templates/polls/index.html
    - TEMPLATE_DIRS, INSTALLED_APPS 의 디렉토리를 검색
    - 템플릿 파일 충돌 방지위해 templates/ 하위에 다시 애플리케이션명으로 디렉토리 생성한다 


    $ mkdir -p polls/templates/polls


### 3.7.3 View 함수 detail() 및 폼 템플릿 작성
- detail.html
- polls.views.detail()


### 3.7.4 View 함수 vote() 및 리다이렉션 작성
- polls.views.vote()


### 3.7.5 View 함수 results() 및 템플릿 작성
- polls.views.results()
- results.html
- View 함수와 Template 태그 양쪽에서 모두 URL 스트링 추출 가능
    - Template --> {% url 'polls:detail' question.id %}
    - View 함수 --> reverse('polls:detail', args=(question.id,))
