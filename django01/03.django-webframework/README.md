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


