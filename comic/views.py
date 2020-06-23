from django.shortcuts import render, get_object_or_404
from .models import Page
from django.utils import timezone
from .forms import PageForm
from django.shortcuts import redirect
from django.core.paginator import Paginator


# Create your views here.


def page_list(request):
	pages = Page.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

	paginator = Paginator(pages, 1)

	page = request.GET.get('page')
	pages = paginator.get_page(page)

	return render(request, 'comic/page_list.html', {'pages':pages})



def page_detail(request, pk): 
	page = get_object_or_404(Page, pk=pk)
	return render(request, 'comic/page_detail.html', {'page': page})



def page_new(request):
	if request.method == "POST":
		form = PageForm(request.POST, request.FILES)
		if form.is_valid():
			page = form.save(commit=False)
			page.author = request.user
			page.published_date = timezone.now()
			page.save()
			return redirect('page_detail', pk=page.pk)
	else:
		form = PageForm()
	return render(request, 'comic/page_edit.html', {'form': form})



def page_edit(request, pk): 
	page = get_object_or_404(Page, pk=pk)
	if request.method == "POST":
		form = PageForm(request.POST, request.FILES, instance=page)
		if form.is_valid():
			page = form.save(commit=False)
			page.author = request.user
			page.published_date = timezone.now()
			page.save()
			return redirect('page_detail', pk=page.pk)
	else:
		form = PageForm(instance=page)
	return render(request, 'comic/page_edit.html', {'form':form})


def page_next(request,pk):
	page = get_object_or_404(Page, pk=pk +1)
	return redirect('page_detail', pk=page.pk +1)




def about(request):
	return render(request, 'comic/about.html')