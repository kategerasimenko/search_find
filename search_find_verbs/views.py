from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import *
from .forms import *

from collections import defaultdict, OrderedDict
from functools import reduce
from itertools import groupby
import html
import pprint
import operator


def create_hierarchy(meaning_pk):
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
    return meaning_list


class IndexView(generic.ListView):
    template_name = 'index.html'
    model = SemanticField
    context_object_name = 'field_list'
    ordering = ['field']

def SemanticFieldView(request,pk):
    template_name = 'verb.html'
    langs = Language.objects.all()
    semfield = SemanticField.objects.get(pk=pk)
    meaningexamples = MeaningExample.objects.filter(field=semfield)
    meaning_pk = defaultdict(list)
    for mex in meaningexamples:
        langex = OrderedDict.fromkeys([x.language for x in langs],value=('',''))
        for ex in LanguageExample.objects.filter(meaning=mex):
            langex[ex.language.language] = (', '.join([x.verb for x in ex.verbs.all()]), ex.example.replace('\n','<br/>'))
        meaning_pk[mex.meaning.pk].append((mex,langex))
    meaning_list = create_hierarchy(meaning_pk)
    return render(request,template_name,{'field':semfield.field,'langs':langs,'all_meanings':meaning_list})
    #return HttpResponse(html.escape(pprint.pformat(langex)))


def SearchFormView(request):
    if request.GET: # add example search and AND/OR button for verbs
        template_name = 'results.html'
        if 'language' in request.GET:
            langs = Language.objects.filter(pk__in=request.GET.getlist('language'))
        else:
            langs = Language.objects.all()
        correspondence = {
            'semfield':'field__pk__in',
            'meaning_type':'meaning__meaning_type__pk__in',
            'meaning':'meaning__meaning__in',
            'object_ref':'meaning__object_ref__in',
            'object_animacy':'meaning__object_animacy__in',
            'purpose':'meaning__purpose__in'}
        values = {correspondence[param]:request.GET.getlist(param) for param in request.GET 
                  if param in correspondence}
        meaningexs = MeaningExample.objects.filter(**values)
        print(values)
        meaningexs = sorted(meaningexs,key=lambda x: (x.field.field))
        meanings_by_field = [(k, list(g)) for k,g in groupby(meaningexs, key=lambda x: (x.field.field))] # делим на семполя
        meaning_list = []
        for field,meaningexamples in meanings_by_field:
            meaning_pk = defaultdict(list)
            verbs = request.GET.getlist('verb') if 'verb' in request.GET else []
            for mex in meaningexamples:
                langex = OrderedDict.fromkeys([x.language for x in langs],value=('',''))
                examples_all = LanguageExample.objects.filter(meaning=mex)
                if verbs:
                    print()
                    if request.GET['verb_conj'] == 'and':
                        examples_for_verb = LanguageExample.objects.filter(meaning=mex)
                        for v in verbs:
                            examples_for_verb = examples_for_verb.filter(verbs__in=[v])
                    else:
                        examples_for_verb = LanguageExample.objects.filter(meaning=mex,verbs__in=verbs)
                else:
                    examples_for_verb = True
                examples_for_ex = LanguageExample.objects.filter(meaning=mex,example__contains=request.GET['example']) if request.GET['example'] else True
                if examples_for_verb and examples_for_ex:
                    for ex in examples_all:
                        if ex.language.language in langex:
                            langex[ex.language.language] = (', '.join([x.verb for x in ex.verbs.all()]), ex.example.replace('\n','<br />')) #br not working
                    meaning_pk[mex.meaning.pk].append((mex,langex))
            meaning_list_curr = create_hierarchy(meaning_pk)
            if meaning_list_curr:
                meaning_list.append((field,meaning_list_curr))
        
        #return HttpResponse(html.escape(pprint.pformat(meaning_list)))  
        return render(request,template_name,{'results':meaning_list,'langs':langs})
        
    template_name = 'search_form.html'
    form = SearchForm(initial={'verb_conj': 'and'})
    return render(request,template_name,{'form':form})
    
    

        
            
