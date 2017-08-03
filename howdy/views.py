# howdy/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

# Add this view
class AboutusPageView(TemplateView):
    template_name = "aboutus.html"

class OaklandPageView(TemplateView):
    template_name = "oakland.html"

class SanfranciscoPageView(TemplateView):
    template_name = "sanfrancisco.html"

class FremontPageView(TemplateView):
    template_name = "fremont.html"

class BerkeleyPageView(TemplateView):
    template_name = "berkeley.html"

class HomelessPageView(TemplateView):
    template_name = "homeless.html"
