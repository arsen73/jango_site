from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from polls.models import Polls, Choice
from django.views import generic
from django.utils import timezone


class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_poll_list'
	page_title = 'asdasd'

	def get_queryset(self):
		""" Return the last five published polls """
		test = {'cont': Polls.objects.filter(
				pub_date__lte=timezone.now()
			).order_by('-pub_date')[:5],
		'page_title': '111'}
		return test

class DetailView(generic.DetailView):
	model = Polls
	template_name = 'polls/detail.html'
	context_object_name = 'poll'

	def get_queryset(self):
		"""
		Excludes any polls that aren't published yet.
		"""
		return Polls.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
	model = Polls
	template_name = 'polls/results.html'
	context_object_name = 'poll'
		
def vote(request, poll_id):
	p = get_object_or_404(Polls, pk=poll_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html',{
			'poll': p,
			'error_message': "You didn't selected a choice.",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
	return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))