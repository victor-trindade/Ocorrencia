# from django.shortcuts import render
# from django.urls import include
from django.views.generic import DetailView
from .models import Occurrence


class OccDetailView(DetailView):
    model = Occurrence
