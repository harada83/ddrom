from django.conf.urls import url, include
from . import views


urlpatterns = [
	
	url(r'^jp_ed_landing/$', views.landing, name='jp_ed_landing'),
	]