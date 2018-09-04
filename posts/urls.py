from django.conf.urls import url
from django.contrib import admin

from .views import (
	post_posts,
	post_create,
	post_retrive,
	post_update,
	post_delete,
	)

urlpatterns = [
    url(r'^$',post_posts),		
    url(r'^create/$',post_create),
    url(r'^(?P<id>\d+)/$',post_retrive, name="details"),       # /d=[0-9],  + = at least one id should be passed
    url(r'^(?P<id>\d+)/edit/$',post_update, name="update"),
    url(r'^delete/$',post_delete),

]
