from django.urls import path
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views

from .views import index

app_name = 'market'
urlpatterns = [

    # path('', views.HomePageView.as_view(), name='home_page'),
    path('', index)
    # path('cinemas/', views.CinemasListView.as_view(), name='cinemas_list'),
    # path('cinemas/<slug:slug>/', views.CinemaDescriptionView.as_view(), name='cinema_description'),
    # path('cinemas/<slug:cinema_slug>/<int:hall_number>/', views.hall_description_view, name='hall_description'),
    #
    # path('about/', views.AboutView.as_view(), name='about'),

]
