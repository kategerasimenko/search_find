from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import *

from collections import defaultdict, OrderedDict
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
        langex = OrderedDict.fromkeys([x.language for x in langs],value=('',''))
        for ex in LanguageExample.objects.filter(meaning=mex):
            langex[ex.language.language] = (', '.join([x.verb for x in ex.verbs.all()]), ex.example.replace('\n','<br>'))
        meaning_pk[mex.meaning.pk].append((mex,langex))
    meaning_list = [(Meaning.objects.get(pk=k),len(v),v) for k,v in meaning_pk.items()] # уровень значений + их свойств
    meaning_list = sorted(meaning_list,key=lambda x: (x[0].meaning_type.meaning_type),reverse=True)
    meaning_list = [(k, list(g)) for k,g in groupby(meaning_list, key=lambda x: (x[0].meaning_type.meaning_type))] # уровень типов значений
    for i,item in enumerate(meaning_list):
        n = 0
        subgroups = []
        new_item = sorted(item[1],key=lambda x: (x[0].meaning))
        for k,g in groupby(new_item, key=lambda x: (x[0].meaning)): # уровень только значений
            group = list(g)
            subn = sum([x[1] for x in group])
            subgroups.append((k,subn,group))
            n += subn
        meaning_list[i] = (item[0],n,subgroups)
    return render(request,template_name,{'field':semfield.field,'langs':langs,'all_meanings':meaning_list})
    #return HttpResponse(html.escape(pprint.pformat(langex)))
    
    
    
    

        
            
