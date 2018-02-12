from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import *

from collections import defaultdict
from itertools import groupby
import html
import pprint

class IndexView(generic.ListView):
    template_name = 'index.html'
    model = SemanticField
    context_object_name = 'field_list'    

def SemanticFieldView(request,pk):
    template_name = 'verb.html'
    langs = Language.objects.all()
    semfield = SemanticField.objects.get(pk=pk)
    meaningexamples = MeaningExample.objects.filter(field=semfield)
    meaning_pk = defaultdict(list)
    for mex in meaningexamples:
        # to do: sort as langs sorted, restore missing values (e.g. no example for japanese)
        langex = LanguageExample.objects.filter(meaning=mex)
        meaning_pk[mex.meaning.pk].append((mex,langex))
    meaning_list = [(Meaning.objects.get(pk=k),len(v),v) for k,v in meaning_pk.items()] # уровень значений
    meaning_list = sorted(meaning_list,key=lambda x: (x[0].meaning_type.meaning_type,x[0].meaning))
    meaning_list = [(k, list(g)) for k,g in groupby(meaning_list, key=lambda x: (x[0].meaning_type.meaning_type))] # уровень типов значений
    meaning_list = [(x[0],sum([y[1] for y in x[1]]),x[1]) for x in meaning_list]
    return render(request,template_name,{'field':semfield.field,'langs':langs,'all_meanings':meaning_list})
    #return HttpResponse(html.escape(pprint.pformat(meaning_list)))
    
    
    
    

        
            
