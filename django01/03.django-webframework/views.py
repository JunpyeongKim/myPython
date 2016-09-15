# encoding=utf-8

# Example 3-2. 간단한 뷰 - 현재의 날짜와 시간 반환

from django.http import HttpResponse
# from django.http import HttpResponseNotFound
import datetime


# 함수로 뷰를 작성
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now

    # Success
    return HttpResponse(html)

    # Fail
    #   - HttpResponseNotFound : HttpResponse 클래스의 하위 클래스
    # return HttpResponseNotFound('<h1>Page not found</h1>')
