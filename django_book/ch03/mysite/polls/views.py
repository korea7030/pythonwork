# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView

from polls.models import Choice, Question

import logging
logger = logging.getLogger(__name__)

class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

# def index(request):
#   latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
#    context = {'latest_question_list': latest_question_list}
 #   return render(request, 'polls/index.html', context)

class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id) # Question : model(table)명 , pk = question_id : 검색조건
#     return render(request, 'polls/detail.html', {'question': question})
class ResultView(DetailView):
    model = Question
    template_name = 'polls/results.html'

# def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    logger.debug("vote().question.id: %s" % question_id)
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice']) # choice 값 가져오기
    except (KeyError, Choice.DoesNotExist): # 에러 발생할 경우
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', { # 질문과 함께 에러메시지 뿌려주기
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else: # vote 성공시
        selected_choice.votes += 1 # 투표값 누적 +1
        selected_choice.save() # 테이블 저장
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,))) # 항상 HttpResponseRedirect 를 반환하여 리다이렉션 처리
