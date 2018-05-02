from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views import generic
from jujum.models import  Jujum
import json

class JujumDetailView(generic.DetailView):
    model = Jujum

def jujum_like(request, pk):

    jujum = get_object_or_404(Jujum, pk=pk)
    jujum.like_count = jujum.like_count + 1
    jujum.save()

    context = { 'like_count': jujum.like_count}

    return HttpResponse(json.dumps(context), content_type="application/json")