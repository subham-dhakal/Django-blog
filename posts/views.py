from django.http import HttpResponse,HttpResponseRedirect	
from django.shortcuts import render,get_object_or_404
from django.contrib import messages


from .models import Post
from .forms import PostForm

# Create your views here.
def post_posts(request): 
	query=Post.objects.all()
	context={"title":"All Posts are displayed here ","objects_list":query}
	return render(request,'index.html',context)

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance=form.save(commit=False)
		print (form.cleaned_data.get("title"))
		instance.save()
		messages.success(request,"Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.success(request," Not Successfully Created")
		
	context={
		"form":form
	}	
	return render(request,'post_form.html',context)


def post_retrive(request,id=None):
	instance=get_object_or_404(Post,id=id)
	context={"title":instance.title,"instance":instance}
	return render(request,'post_retrive.html',context)

def post_update(request,id=None): 
	instance=get_object_or_404(Post,id=id)
	form=PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context={"title":instance.title,"instance":instance,"form":form}
	return render(request,'post_form.html',context)


def post_delete(request): 
	return HttpResponse("<h1>Delete</h1>")