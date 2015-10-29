from django.shortcuts import render
from polls.models import Question

# Create your views here.


def index(request):
    # django.core.serializers.python.Serializer
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}

    '''
        def render(request, template_name, context=None,
           context_instance=_context_instance_undefined,
           content_type=None, status=None, current_app=_current_app_undefined,
           dirs=_dirs_undefined, dictionary=_dictionary_undefined,
           using=None):
           return HttpResponse(content, content_type, status)

        django.shortcuts
            - 웹 프로그램 개발시 자주 사용되는 기능들을 미리 개발하여 내장 함수로 제공
    '''
    return render(request, 'polls/index.html', context)
