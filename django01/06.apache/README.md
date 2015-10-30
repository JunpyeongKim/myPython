# 6. 웹 서버(Apache) 연동

## 6.1 mode_wsgi 확장 모듈
- Apache 웹 서버의 프로그램 명 --> httpd
- Apache는 추가로 필요한 기능을 모듈로 만들어 동적 로딩방식으로 기능을 확장 가능
    - mod_alias : 클라이언트 요청 URL --> 서버 내 디렉토리로 매핑
    - mod_auth : 사용자 인증 
    - mod_jk : 톰캣 연동 
    - mod_proxy : Proxy 기능 
    - mod_rewrite : URL rewrite 지원
    - mod_php : PHP 스크립트 실행 
    - mod_perl : Perl 스크립트 실행 
    - mod_wsgi : 파이썬 웹 애플리케이션을 실행할 수 잇는 확장 모듈중 하나 
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
                - 차이점 : 별도의 프로세스 관리자 WSGI 어댑터  불필요 --> 모든 처리는 mod_wsgi가 관리 
            - Apache 모듈로 서비스하는 다른 애플리케이션에 미치는 영향이 미미하다
            - 필요하다면 WSGI 애플리케이션 간에도 서로 영향을 주지 않도록 실행 유저를 달리하여 데몬 프로세스로 기동하는 것도 가능
        - (*) 2가지 모드는 동작 방식은 다르지만, 대용량 웹 애플리케이션에서의 처리 성능은 크게 없다
    - C 로 구현
        - 내부적으로 Apache가 직접 파이썬 API와 동작하므로 상대적으로 적은 메모리를 사용
        - CGI에 비해서도 좋은 성능을 보인다
    - ==> Django에서는 안정성을 고려하여 Daemon Mode로 실행할 것을 권장
        