from django import forms
from .models import *


class SearchForm(forms.Form):
        semfield = forms.ModelMultipleChoiceField(queryset=SemanticField.objects.all().order_by('field'),required=False, label='Семантическое поле')
        meaning_type = forms.ModelMultipleChoiceField(queryset=MeaningType.objects.all(),required=False,widget=forms.CheckboxSelectMultiple(), label='Тип значения')
        meaning_choices = Meaning.objects.order_by('meaning').values_list('meaning',flat=True).distinct()
        meaning = forms.MultipleChoiceField(choices=zip(meaning_choices,meaning_choices),required=False, label='Значение')
        object_ref = forms.MultipleChoiceField(choices=OBJECT_REF_CHOICES,required=False,widget=forms.CheckboxSelectMultiple(), label='Объектная референция')
        object_animacy = forms.MultipleChoiceField(choices=OBJECT_ANIMACY_CHOICES,required=False,widget=forms.CheckboxSelectMultiple(), label='Одушевлённость объекта')
        purpose = forms.MultipleChoiceField(choices=PURPOSE_CHOICES,required=False,widget=forms.CheckboxSelectMultiple(), label='Цель')
        language = forms.ModelMultipleChoiceField(queryset=Language.objects.all().order_by('language'),required=False, label='Язык')
        verb = forms.ModelMultipleChoiceField(queryset=Verb.objects.all().order_by('language__language','verb'),required=False, label='Глагол')
        example = forms.CharField(max_length=300,required=False, label='Пример')