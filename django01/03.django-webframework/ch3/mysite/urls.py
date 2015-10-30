# encoding=utf-8

"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from polls import views

# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
# ]


# Example 3-8
# def patterns(prefix, *args)
# urlpatterns = patterns('',
#                        # def url(regex, view, kwargs=None, name=None, prefix='')
#                        #    - view <-- regex 에서 추출한 인자 & HttpRequest를 전달
#                        #    - kwargs : 추가 인자 전달
#                        #    - name : template 파일에서 사용
#
#                        # views.index(request)
#                        url(r'^polls/$', views.index, name='index'),
#
#                        # views.detail(request, question_id='3')
#                        url(r'^polls/(?P<question_id>\d+)/$', views.detail, name='detail'),
#
#                        # views.vote(request, question_id='3')
#                        url(r'^polls/(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
#
#                        # views.results(request, question_id='3')
#                        url(r'^polls/(?P<question_id>\d+)/results/$', views.results, name='results'),
#
#                        url(r'^admin/', include(admin.site.urls)),
#                        )

# Example 3-9 & 3-10
urlpatterns = patterns('',
                       # namespace : URL 패턴의 이름 충돌 방지위한 것
                       #    - ex) polls:detail vs. blog:detail
                       url(r'^polls/', include('polls.urls', namespace="polls")),
                       url(r'^admin/', include(admin.site.urls)),
                       )
