from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from polls.models import Question, Choice

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


def detail(request, question_id):
    # django.shortcut
    #   - def get_object_or_404(klass, *args, **kwargs):
    #   - (*) get_list_or_404() : filter() 를 사용
    #       - get_object_or_404() : get() 을 사용
    # Http404
    question = get_object_or_404(Question, pk=question_id)

    '''
        Relation --> Question : Choice = 1 : N
            - xxx_set 속성을 default로 제공한다
            - ex) question.choice_set.all()
                - Question 테이블의 question 레코드에 연결된 Choice 테이블의 레코드를 모두를 의미
                - question.choice_set.all : template syntax에서는 ()를 사용하지 않는다
    '''
    return render(request, 'polls/detail.html', {'question': question})


def vote(request, question_id):
    # Http404
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # reverse() : URLconf로부터 URL 패턴 --> URL 스트링을 구한다
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


def results(request, question_id):
    # Http404
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
