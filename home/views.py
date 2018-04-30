from django.shortcuts import render
from django.views import generic
from home.models import Nanjang, Jujum

class IndexView(generic.TemplateView):
    template_name = 'home/index.html'

class MainView(generic.ListView):
    queryset = Nanjang.objects.all()
    context_object_name = 'nanjang_list'
    template_name = 'home/main.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['jujum_list'] = Jujum.objects.all()
        return context

class NanjangDetailView(generic.DetailView):
    model = Nanjang
    
class JujumDetailView(generic.DetailView):
    model = Jujum


# def main(request):
#     nanjang_list = Nanjang.objects.all()
#     jujum_list = Jujum.objects.all()
#     context = {'nanjang_list': nanjang_list, 'jujum_list' : jujum_list }
#     return render(request, 'home/main.html', context)
