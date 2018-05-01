from django.shortcuts import render
from django.views import generic
from jujum.models import  Jujum

class JujumDetailView(generic.DetailView):
    model = Jujum
