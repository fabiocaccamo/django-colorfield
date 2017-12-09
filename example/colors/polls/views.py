#-*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Choice, Poll
from .forms import ChoiceForm


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        return Poll.objects.all()[:5]


class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['form'] = ChoiceForm()
        return context


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    choice, created = p.choice_set.get_or_create(color=request.POST['color'])
    choice.votes += 1
    choice.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('results', args=(p.id,)))


def create_polls(request):
    '''create example poll'''
    if Poll.objects.count() == 0:
       question = "What is your favorite color?"
       poll = Poll.objects.create(question=question)
       choice = Choice.objects.create(poll=poll)
    else:
       poll = Poll.objects.last()
    return HttpResponseRedirect(reverse('results', args=(poll.id,)))
