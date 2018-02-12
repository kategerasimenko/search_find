from django.shortcuts import render
from django.views import generic
from .models import *

class IndexView(generic.ListView):
    template_name = 'index.html'
    model = SemanticField
    context_object_name = 'field_list'

class SemanticFieldView(generic.DetailView):
    template_name = 'field.html'
    model = SemanticField
    context_object_name = 'field_detail'
