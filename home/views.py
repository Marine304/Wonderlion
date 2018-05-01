from django.shortcuts import render
from django.views import generic
from nanjang.models import Nanjang
from jujum.models import Jujum

class IndexView(generic.TemplateView):
    template_name = 'home/index.html'

class MainView(generic.TemplateView):
    template_name = 'home/main.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['nanjang_list'] = Nanjang.objects.all()
        context['jujum_list'] = Jujum.objects.all()

        return context
