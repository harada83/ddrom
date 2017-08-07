# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Subscriber

# Register your models here.
class SubscriberAdmin(admin.ModelAdmin):
	#list_display = ('name', 'email')
	list_display = [field.name for field in Subscriber._meta.fields]
	list_filter = ['name']
	search_fields = ["name", "email"]

	fields = ["email"]
	#exclude = [""]
	
	class Meta:
		model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)