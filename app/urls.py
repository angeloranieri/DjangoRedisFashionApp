from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserLogin

urlpatterns = [
    path('', views.home_item_list, name='item_list'),
    path('login/', LoginView.as_view(template_name='app/login.html', form_class=UserLogin), name='login'),
    path('logout/', LogoutView.as_view(template_name='app/logout.html'), name='logout'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('item/new/', views.item_new, name='item_new'),
    path('item/<int:pk>/edit/', views.item_edit, name='item_edit'),
    path('item/<int:pk>/owner/', views.owner_edit, name='owner_edit'),
]