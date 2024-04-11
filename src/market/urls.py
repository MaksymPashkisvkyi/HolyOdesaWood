from django.urls import path
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from django.contrib import admin

from .views import index, contacts, about, product_details_default

app_name = 'market'
urlpatterns = [

    # path('', views.HomePageView.as_view(), name='home_page'),
    path('',          index,                   name='index'),
    path('contacts/', contacts,                name='contacts'),
    path('about/',    about,                   name='about'),
    path('shop/',     product_details_default, name='product_details_default'),
    # path('admin/',    admin.site.urls, name='admin')

    # path('cinemas/', views.CinemasListView.as_view(), name='cinemas_list'),
    # path('cinemas/<slug:slug>/', views.CinemaDescriptionView.as_view(), name='cinema_description'),
    # path('cinemas/<slug:cinema_slug>/<int:hall_number>/', views.hall_description_view, name='hall_description'),
    #
    # path('about/', views.AboutView.as_view(), name='about'),
]
