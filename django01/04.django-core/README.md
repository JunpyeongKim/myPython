4. Django 의 핵심 기능
====================

# 4.1 Admin 사이트 꾸미기
- 데이터베이스에 들어있는 데이터를 쉽게 관리가능한 기능을 제공
    - 데이터 생성 / 조회 / 변경 / 삭제 등
    - http://localhost:8000/admin


## 4.1.1 데이터 입력 및 수정
- CharField, DateTimeField 에 적합한 UI 위젯을 보여준다


## 4.1.2 필드 순서 변경하기
- 테이블을 보여주는 UI 양식을 변경할 경우 
- polls/admin.py
    - admin.ModelAdmin 상속 --> QuestionAdmin 정의
        - fields = ['pub_date', 'question_text']
    - admin.site.register(Question, QuestionAdmin)


## 4.1.3 각 필드를 분리해서 보여주기
- polls/admin.py
    - fields --> fieldsets
        - ex) fieldsets = [('Question Statement', {'fields': ['question_text']}),]


## 4.1.4 필드 접기
- polls/admin.py
    - 'classes': ['collapse']
        - ex) ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']})


## 4.1.5 Foreign Key 관계 화면
- ex) 질문 하나에 3개의 답변 항목이 있다면 --> Choice 레코드를 추가하는 동일한 작업을 3번 반복해야 해서 번거롭다


## 4.1.6 Question 및 Choice 를 한 화면에서 변경하기
- (*) Question 레코드를 기준으로 여러 개의 Choice 레코드가 연결되므로 --> 1:N
- extra : 한 번에 보여주는 choice_text 의 숫자가 결정된다
    - ex) What is your hobby? 는 이미 3개의 choice_text가 존재 --> 그 외에 2개 항목 추가 입력 가능하도 된다
- class QuestionAdmin
    - inlines
- class ChoiceInline(admin.StackedInline):


## 4.1.7 테이블 형식으로 보여주기
- class ChoiceInline(admin.TabularInline):


## 4.1.8 레코드 리스트 항목 지정하기
- models.py
    - __unicode__() 함수의 리턴값을 레코드의 제목으로 사용
- 컬럼 항목 추가
    - polls/admin.py
        - list_display = ('question_text', 'pub_date')
        - 컬럼 헤더를 클릭하면 컬럼을 기준으로 정렬된다


## 4.1.9 list_filter 필터
- UI 화면에 필터 사이드바를 붙일 수 있다
- polls/admin.py
    - [Filter] : 기준 필드 타입에 따라 Django 가 자동으로 적절한 항목들을 보여준다
    - ex) list_filter = ['pub_date']
        - Any date, Today, ...


## 4.1.10 search_fields
- UI화면에 검색 박스 표시
- polls/admin.py
    - LIKE 쿼리로 검색
    - 여러 개의 필드 저징 가능
    - ex) search_fields = ['question_text']

## 4.1.11 polls/admin.py 변경 내역 정리
- N/A


## 4.1.12 Admin 사이트 템플릿 수정
- Django 의 기본 Admin 템플릿 파일을 우리 프로젝트로 복사후 변경 --> settings.py 에 새로 만든 프로젝트 템플릿 디렉토리를 등록


    $ cd ch4/
    $ mkdir -p templates/admin
    $ cp -v /Library/Python/2.7/site-packages/django/contrib/admin/templates/admin/base_site.html templates/admin/

- base_site.html
    - {{ site_header|default:_('Django administration') }} --> My Administration
- mysite/settings.py
    - TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates']