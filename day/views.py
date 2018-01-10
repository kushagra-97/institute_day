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

def curruser(request):
	user = request.user
	if user.is_authenticated():
		return HttpResponse(str(user.username))
	return HttpResponse('None')

# Create your views here.
def home(request):
    return render(request, 'index.html')

def elements(request):
    return render(request, 'elements.html')

def generic(request):
    return render(request, 'generic.html')        

# def registration(request):
#     return render(request, 'registration.html')     

@csrf_exempt
@login_required(login_url="/")
def registration(request):
	template_name = 'registration.html'
	context = {
	}
	# Create your views here.
	user=request.user
	

	if request.method == "POST":
			post = request.POST
			print(post)

			
			student=Students.objects.create(user = user)
			student.mentor = post.get('mentor')
			student.title = post.get('title')
			student.department = post.get('department')
			student.subarea = post.get('subarea')
			student.abstract = post.get('abstract')
			student.save()
			
			context['status']=1
			context['firstname'] =  request.user.first_name
			context['lastname'] =  request.user.last_name
			context['mentor'] =  post.get('mentor')
			context['title'] =  post.get('title')
			context['department'] =  post.get('department')
			context['subarea'] =  post.get('subarea')
			context['abstract'] =  post.get('abstract')
			print("success")
			

			return JsonResponse(context)

	else:#request.method == "GET"
			
			try:
				s=student.object.get(user = user)
				context['status']=1
				context['firstname'] =  student.user.first_name
				context['lastname'] =  student.user.last_name
				context['mentor'] =  student.mentor
				context['title'] =  student.title
				context['department'] = student.department
				context['subarea'] = student.subarea
				context['abstract'] =  student.abstract
				context['email']=student.user.email

			except:
				context['status']=0



			# # context['name'] =  request.user.first_name;
			# context['mentor'] =  post.get('mentor');
			# context['title'] =  post.get('title');
			# context['department'] =  post.get('department');
			# context['subarea'] =  post.get('subarea');
			# context['abstract'] =  post.get('abstract');
			# context['email']=request.user.username;
			# return render(request,template_name,context)               	
			return JsonResponse(context)

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

