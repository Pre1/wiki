from django.shortcuts import render, redirect
from .models import Page
# Create your views here.



def list(request):
	context = {
		"subjects": Page.objects.all()
	}

	return render(request, 'list.html', context)


def detail(request, page_id):
	context = {
		"subject": Page.objects.get(id = page_id)
	}
	
	return render(request, 'detail.html', context)