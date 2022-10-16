from django.shortcuts import render

from django.http import HttpResponse


def home(request):
	template_name = 'mainpage/home.html'
	return render(request, template_name)

def exec(request):
	template_name = 'mainpage/exec.html'
	return render(request, template_name)

def partner(request):
	template_name = 'mainpage/partner.html'
	return render(request, template_name)


def events(request):
	template_name = 'mainpage/events.html'
	return render(request, template_name)

def contact(request):
	template_name = 'mainpage/contact.html'
	return render(request, template_name)
