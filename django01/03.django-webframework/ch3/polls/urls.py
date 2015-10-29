# encoding=utf-8

# mysite/settings.py
#   - ROOT_URLCONF : Django 가 URL 분석시 이 곳에 정의된 urls.py 를 가장 먼저 분석

from django.conf.urls import patterns, url
from polls import views

# def patterns(prefix, *args)
urlpatterns = patterns('',
                       # def url(regex, view, kwargs=None, name=None, prefix='')
                       #    - view <-- regex 에서 추출한 인자 & HttpRequest를 전달
                       #    - kwargs : 추가 인자 전달
                       #    - name : template 파일에서 사용

                       # views.index(request)
                       url(r'^polls/$', views.index, name='index'),

                       # views.detail(request, question_id='3')
                       url(r'^polls/(?P<question_id>\d+)/$', views.detail, name='detail'),

                       # views.vote(request, question_id='3')
                       url(r'^polls/(?P<question_id>\d+)/vote/$', views.vote, name='vote'),

                       # views.results(request, question_id='3')
                       url(r'^polls/(?P<question_id>\d+)/results/$', views.results, name='results'),

                       url(r'^admin/', include(admin.site.urls)),
                       )


'''
    mysite/urls.py 에 모두 정의 가능
        - 그러나 추천하지 않는다

    from django.conf.urls import patterns, include, url
    from django.contrib import admin

    urlpatterns = [
        # namespace : URL 패턴의 이름 충돌 방지위한 것
        # - ex) polls:detail, blog:detail
        url(r'^polls/', include('polls.urls'), namespace="polls")
        url(r'^admin/', include(admin.site.urls)),
    ]
'''