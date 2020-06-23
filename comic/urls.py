from django.urls import path
from . import views




urlpatterns = [
	path('', views.page_list), 
	path('page/<int:pk>/', views.page_detail, name='page_detail'),
	path('page/new', views.page_new, name='page_new'), 
	path('page/<int:pk>/edit', views.page_edit, name='page_edit'),
	path('page/<int:pk>/next', views.page_next, name='page_next'),
	path('about', views.about, name="about"), 
	path('updates',views.updates, name="updates"),
]
