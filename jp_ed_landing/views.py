# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import SubscriberForm

# Create your views here.


def landing(request):
	form = SubscriberForm(request.POST or None)
	if request.method == "POST" and form.is_valid():
		data = form.cleaned_data
		new_form = form.save()

	return render(request, 'jp_ed_landing/jp_ed_landing.html', locals())