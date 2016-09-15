# encoding=utf-8

# Example 3-1. URLconf 예시
"""
    Django 에서 URL 분석 순서
    - settings.py 의 ROOT_URLCONF 로부터 URLconf(urls.py)의 위치를 알아낸다.
    - URLconf 를 로딩하여 urlpatterns 의 URL 리스트를 검사
    - 매칭된 URL 의 View 를 호출
        - HttpRequest 의 매칭된 인자들을 View 에 넘겨준다.
    - 매칭 실패시 에러처리 View 를 호출

    Regular Expression
    - . (Dot) : 모든 문자 하나
    - ^ (Caret) : 문자열의 시작
    - $ : 문자열의 끝
    - [] : 괄호안의 문자 하나
    - [^] : 괄호안의 문자 이외의 문자 하나
    - * : 0번 이상 반복 == {0,}
    - + : 1번 이상 반복 == {1,}
    - ? : 0 또는 1 번 반복 == {0,1}
    - {n} : n 번 반복
    - {m,n} : m~n 번 반복
    - | : A|B, A 또는 B
    - [a-z] : a~z까지 임의의 문자 한 개
    - \w : 영문/숫자/_ 한개 == [0-9a-zA-Z]
    - \d : 숫자 한개 [0-9]

"""

from django.conf.urls import patterns, url
from . import views

# pattenrs(prefix, *args)
urlpatterns = patterns('',
                       url(r'^articles/2003/$', views.special_case_2003),
                       url(r'^articles/(\d{4})/$', views.year_archive),
                       url(r'^articles/(\d{4})/(\d{2})/$', views.month_archive),
                       url(r'^articles/(\d{4})/(\d{2})/(\d+)/$', views.article_detail)
                       )
