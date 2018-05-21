from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'login', views.login),
	url(r'logout', views.logout),
	url(r'register', views.register),
	url(r'success', views.success),
	url(r'index', views.index),
	url(r'^', views.index),
]
