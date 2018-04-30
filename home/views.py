from django.shortcuts import render
from django.views import generic

class IndexView(generic.TemplateView):
    template_name = 'home/index.html'

class MainView(generic.TemplateView):
    template_name = 'home/main.html'

class NanjangListView(generic.ListView):
    pass

class JujumListView(generic.ListView):
    pass