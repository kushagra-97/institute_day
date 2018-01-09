from django.shortcuts import render
from django.shortcuts import render_to_response, HttpResponse, redirect
from django.http import Http404,JsonResponse,HttpResponseBadRequest
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import generic
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout

from .models import *
import datetime
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'index.html')

def elements(request):
    return render(request, 'elements.html')

def generic(request):
    return render(request, 'generic.html')        

def registration(request):
    return render(request, 'registration.html')     


def registration(request):
	template_name = 'registration.html'
	context = {
	}
	# Create your views here.
	if request.method == "POST":
			post = request.POST
			print(post)

			context['name'] =  post.get('name');
			context['mentor'] =  post.get('mentor');
			context['title'] =  post.get('title');
			context['department'] =  post.get('department');
			context['subarea'] =  post.get('subarea');
			context['abstract'] =  post.get('abstract');
			context['email']=request.user.username;

			student=Students.objects.create()
			student.name = post.get('name')
			student.mentor = post.get('mentor')
			student.title = post.get('title')
			student.department = post.get('department')
			student.subarea = post.get('subarea')
			student.abstract = post.get('abstract')
			student.save()

	else:#request.method == "GET"
			return render(request,template_name,context)               	


# def update(request):
	
	# instance = get_object_or_404(Post)
	# form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	# if form.is_valid():
	# 	instance = form.save(commit=False)
	# 	instance.save()
	# 	messages.success(request, "updated")
	# 	return HttpResponseRedirect(instance.get_absolute_url())

	# context = {
		
	# 	"form":form,
	# }
	# return render(request, "create.html", context)

# def home(request):
# 	return render(request, 'home.html')

