# encoding=utf-8

# mysite/settings.py
#   - ROOT_URLCONF : Django 가 URL 분석시 이 곳에 정의된 urls.py 를 가장 먼저 분석

from django.conf.urls import patterns, url
from polls import views

# Example 3-9 & 3-10
# def patterns(prefix, *args)
urlpatterns = patterns('',
                       # def url(regex, view, kwargs=None, name=None, prefix='')
                       #    - view <-- regex 에서 추출한 인자 & HttpRequest를 전달
                       #    - kwargs : 추가 인자 전달
                       #    - name : template 파일에서 사용

                       # views.index(request)
                       url(r'^$', views.index, name='index'),

                       # views.detail(request, question_id='3')
                       url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),

                       # views.vote(request, question_id='3')
                       url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),

                       # views.results(request, question_id='3')
                       url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
                       )
