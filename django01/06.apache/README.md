# 6. 웹 서버(Apache) 연동

## 6.1 mode_wsgi 확장 모듈
- Apache 웹 서버의 프로그램 명 --> httpd
- Apache는 추가로 필요한 기능을 모듈로 만들어 동적 로딩 방식으로 기능을 확장 가능
    - mod_alias : 클라이언트 요청 URL --> 서버 내 디렉토리로 매핑
    - mod_auth : 사용자 인증 
    - mod_jk : 톰캣 연동 
    - mod_proxy : Proxy 기능 
    - mod_rewrite : URL rewrite 지원
    - mod_php : PHP 스크립트 실행 
    - mod_perl : Perl 스크립트 실행 
    - mod_wsgi : 파이썬 웹 애플리케이션을 실행할 수 있는 확장 모듈중 하나 
- mod_wsgi
    - 파이썬 웹 애플리케이션 표준 규격인 WSGI (Web Server Gateway Interface)를 구현한 확장 모듈 
    - PEP(Python Enhancement Proposals) 333에 정의되어 있음 
    - 이것을 사용해 웹 애플리케이션(WSGI 애플리케이션)을 실행하는 2가지 모드
        - 1) Embedded Mode
            - Apache 자식 프로세스 컨텍스트 내에서 애플리케이션이 실행된다
            - mod_python 방식과 유사
            - 단점 : WSGI 애플리케이션의 소스가 변경되어 다시 적용하려면 Apache 전체를 재기동 해야 한다.
        - 2) Daemon Mode
            - Apache 2.0 이상에서 지원
            - 전용 프로세스에서 애플리케이션이 실행된다
            - F(Fast)CGI / S(Simple)CGI와 유사
                - 차이점 : 별도의 프로세스 관리자, WSGI 어댑터  불필요 --> 모든 처리는 mod_wsgi가 관리 
            - Apache 모듈로 서비스하는 다른 애플리케이션에 미치는 영향이 미미하다
            - 필요하다면 WSGI 애플리케이션 간에도 서로 영향을 주지 않도록 실행 유저를 달리하여 데몬 프로세스로 기동하는 것도 가능
        - (*) 2가지 모드는 동작 방식은 다르지만, 대용량 웹 애플리케이션에서의 처리 성능은 크게 없다
    - C 로 구현
        - 내부적으로 Apache가 직접 파이썬 API와 동작하므로 상대적으로 적은 메모리를 사용
        - CGI에 비해서도 좋은 성능을 보인다
    - ==> Django에서는 안정성을 고려하여 Daemon Mode로 실행할 것을 권장


## 6.2 Django의 웹 서버 연동 원리
- mysite/wsgi.py
    - (*) Django & Web Server 를 연결하기 위한 파일
    - WSGI 규격에 따라 호출 가능한(callable) 애플리케이션 객체를 정의 --> 객체명은 반드시 application 이어야 한다
        - Apache(httpd.conf) : WSGIScriptAlias
        - runserver(mysite/settings.py) : WSGI_APPLICATION
        - (*) 웹 서버는 이 application 객체를 호출하여 Django 애플리케이션을 실행한다
- 설정 정보 로딩을 위한 settings 모듈 위치 지정 방법
    - Apache 등의 웹 서버 : wsgi.py 에서 지정
        - (ex) os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    - runserver : 실행 옵션 또는 프로젝트명.settings 사용
        - (ex) $ python manage.py runserver --settings=mysite.settings
- (*) httpd.conf
    - (*) /etc/httpd/conf/httpd.conf
        - $ sudo apt-get install apache2
        - $ sudo service apache2 status/stop/start
        - $ sudo netstat -lntp | grep apache2
        - (*) ll /etc/apache2
        - (*) ll /var/www/html


## 6.3 상용 서버 적용 전 Django 의 설정 변경
- mysite.settings.DEBUG = False 이면 반드시 ALLOWED_HOSTS 를 설정해야 한다
    - CSRF(Cross Site Request Forgery) 공격을 방지하기 위해
- Apache 같은 웹서버가 정적 파일의 위치를 알수 있도록  해주어야 한다
    - mysite.settings.STATIC_ROOT : collectstatic 명령 실행시 정적 파일들을 한곳에 모아주는 디렉토리
        - ex) STATIC_ROOT = os.path.join(BASE_DIR, "www_static")
        - STATICFILES_DIRS에 정의된 디렉토리에서 정적 파일을 찾아 STATIC_ROOT 에 복사해 준다 
    - Apache 설정 파일 : Alias /static 설정 필요
- 상용모드에서는 데이터베이스 파일 / 로그 파일을 apache 사용자 권한으로 액세스 가능해야 한다
    - $ cd /home/shkim/pyBook/ch6
    - $ mkdir db
    - $ chmod 777 db/
    - $ chmod 666 db/db.sqlite3
- settings.LOGGING
    - $ cd /home/shkim/pyBook/ch6
    - $ chmod 777 logs/
    - $ chmod 666 logs/logfile
- (*) https://docs.djangoproject.com/en/1.8/howto/deployment/checklist
    

## 6.4 Embedded Mode 로 실행

### 6.4.1 아파치 설정 
- httpd.con 에 mod_wsgi 관련 설정 추가 필요
- 설정 및 실행은 root 권한으로


    $ cd /etc/httpd/conf
    $ vi httpd.conf
    
- WSGIScriptAlias / /home/shkim/pyBook/ch6/mysite/wsgi.py
- WSGIPythonPath / /home/shkim/pyBook/ch6/
    - 파이썬 임포트 경로를 지정
- <Directocy /home/shkim/pyBook/ch6/mysite>
    - 아파치가 액세스 가능하도록 접근 권한 설정
- <Files wsigi.py>
    - 아파치가 액세스 가능하도록 접근 권한 설정
- Alias /static/ /home/shkim/pyBook/ch6/www_static
- <Directocy /home/shkim/pyBook/ch6/www_static>
    - 아파치가 액세스 가능하도록 접근 권한 설정

### 6.4.2 지금까지 작업 확인
- runserver 로는 정상동작하나, Apache 로 서비스가 안되는 경우
    - SE(Security Enhancec)Linux 보안 정책 변경 필요
        - $ setenforce permissive
        - $ service httpd start
        - (*) setenforce : 현재 쉘에서만 임시 변경된다
        - (*) config 파일 : 부팅시에 적용된다
            - enforcing / permissive / disable
- open your.com.ip.address
    - $ cd /etc/httpd/logs
    - $ tail access_log


## 6.5 Daemon Mode 로 실행

### 6.5.1 아파치 설정 

    $ cd /etc/httpd/conf
    $ vi httpd.conf

- WSGIScriptAlias / /home/shkim/pyBook/ch6/mysite/wsgi.py
- WSGIDaemonProcess mysite python-path=/home/shkim/pyBook/ch6
- WSGIProcessGroup mysite
- <Directocy /home/shkim/pyBook/ch6/mysite>
    - 아파치가 액세스 가능하도록 접근 권한 설정
- <Files wsigi.py>
    - 아파치가 액세스 가능하도록 접근 권한 설정
- Alias /static/ /home/shkim/pyBook/ch6/www_static
- <Directocy /home/shkim/pyBook/ch6/www_static>
    - 아파치가 액세스 가능하도록 접근 권한 설정