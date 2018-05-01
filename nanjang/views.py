from django.shortcuts import render
from django.views import generic
from nanjang.models import Nanjang

class NanjangListView(generic.ListView):
    model = Nanjang

class NanjangDetailView(generic.DetailView):
    model = Nanjang
