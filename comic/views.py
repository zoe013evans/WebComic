from django.shortcuts import render, get_object_or_404
from .models import Page
from django.utils import timezone


# Create your views here.


def page_list(request):
	pages = Page.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'comic/page_list.html', {'pages':pages})





def page_detail(request, pk): 
	page = get_object_or_404(Page, pk=pk)
	return render(request, 'comic/page_detail.html', {'page': page})


