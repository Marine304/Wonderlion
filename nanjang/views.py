from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views import generic
from nanjang.models import Nanjang
import json

class NanjangListView(generic.ListView):
    model = Nanjang

class NanjangDetailView(generic.DetailView):
    model = Nanjang

def nanjang_like(request, pk):

    nanjang = get_object_or_404(Nanjang, pk=pk)
    nanjang.like_count = nanjang.like_count + 1
    nanjang.save()

    context = { 'like_count' : nanjang.like_count }
    
    return HttpResponse(json.dumps(context), content_type="application/json")