# howdy/urls.py
from django.conf.urls import url
from howdy import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^aboutus/$', views.AboutusPageView.as_view()), # Add this /about/ route
    url(r'^oakland/$', views.OaklandPageView.as_view()), # Add this /about/ route
    url(r'^sanfrancisco/$', views.SanfranciscoPageView.as_view()), # Add this /about/ route
    url(r'^fremont/$', views.FremontPageView.as_view()), # Add this /about/ route
    url(r'^berkeley/$', views.BerkeleyPageView.as_view()), # Add this /about/ route
    url(r'^homeless/$', views.HomelessPageView.as_view()), # Add this /about/ route
]
