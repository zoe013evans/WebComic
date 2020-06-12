from django.shortcuts import render
from .models import Page
from django.utils import timezone

# Create your views here.


def page_list(request):
	pages = Page.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'comic/page_list.html', {'pages':pages})