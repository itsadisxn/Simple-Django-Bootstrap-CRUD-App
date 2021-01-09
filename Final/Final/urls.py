"""
Definition of urls for Final.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from app.views import ProfileListView, ProfileDetailView, ProfileCreateView, ProfileUpdateView, ProfileDeleteView


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('profiles/', views.ProfileListView.as_view(), name='profiles'),
    path('profile/<int:pk>', views.ProfileDetailView.as_view(), name='detail'),
    path('create/', views.ProfileCreateView.as_view(), name='create'),  
    path('edit/<int:pk>/', views.ProfileUpdateView.as_view(), name='update'),  
    path('delete/<int:pk>/', views.ProfileDeleteView.as_view(), name='delete'),
]

