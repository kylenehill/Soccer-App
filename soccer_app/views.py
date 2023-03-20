from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import PlayerForm
# PlayerForm
from .models import Player
# compare to get results
import sys
sys.path.append('..')
import compare #see if this works


# Create your views here.

def results_view(request):
	user_result_likelihood = compare.get_result_likelihood() #remove if does not work
	context = {"user_result_likelihood": user_result_likelihood} # remove if does not work, then remove context from next line
	return render(request, "results_view.html", context)
	#return render(request, "results_view.html", {})

def player_create_view(request):

	my_form = PlayerForm()

	if request.method == 'POST':
		my_form = PlayerForm(request.POST or None)
		if my_form.is_valid():

			print(my_form.cleaned_data)
			Player.objects.create(**my_form.cleaned_data)
			# insert call to run python scripts here
			## 

			return redirect('/results/')
			#return render(request, "results_view.html", {})
			#return redirect(results_view)
			#my_form.save()
		else:
			print(my_form.errors)



	context = {
		'form' : my_form
	}

	return render(request, "test_homepage.html", context)



def homepage_view(request, *args, **kwargs):
	#return HttpResponse("<h1>Hello Soccer World</h1>")
	# print(request.GET)
	# print(request.POST)
	# if request.method == 'POST':

	# 	print(request.POST)
	return render(request, 'draft_homepage.html', {})