from django.conf.urls import url, include
from . import views


urlpatterns = [
	url(r'^arshan/$', views.home, name='home'),
	# url(r'^landing/$', views.landing, name='landing'),
	]