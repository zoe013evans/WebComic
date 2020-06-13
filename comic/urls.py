from django.urls import path
from . import views




urlpatterns = [
	path('', views.page_list), 
	path('page/<int:pk>/', views.page_detail, name='page_detail'),
]