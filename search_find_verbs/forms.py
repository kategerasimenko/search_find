from django import forms
from .models import *


class SearchForm(forms.Form):
        semfield = forms.ModelMultipleChoiceField(queryset=SemanticField.objects.all().order_by('field'),required=False, label='Семантическое поле',  widget=forms.SelectMultiple(attrs={'multiple class':'form-control'}))
        meaning_type = forms.ModelMultipleChoiceField(queryset=MeaningType.objects.all(),required=False, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}), label='Тип значения')
        meaning_choices = Meaning.objects.order_by('meaning').values_list('meaning',flat=True).distinct()
        meaning = forms.MultipleChoiceField(choices=zip(meaning_choices,meaning_choices),required=False, label='Значение', widget=forms.SelectMultiple(attrs={'multiple class':'form-control'}))
        object_ref = forms.MultipleChoiceField(choices=OBJECT_REF_CHOICES,required=False,widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}), label='Объектная референция')
        object_animacy = forms.MultipleChoiceField(choices=OBJECT_ANIMACY_CHOICES,required=False,widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}), label='Одушевлённость объекта')
        purpose = forms.MultipleChoiceField(choices=PURPOSE_CHOICES,required=False,widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}), label='Цель')
        language = forms.ModelMultipleChoiceField(queryset=Language.objects.all().order_by('language'),required=False, label='Язык', widget=forms.SelectMultiple(attrs={'multiple class':'form-control'}))
        verb_conj = forms.ChoiceField(choices=[('and','AND'),('or','OR')], widget=forms.RadioSelect(attrs={'class': 'form-check-label'}), label='Отношение между несколькими выбранными глаголами')
        verb = forms.ModelMultipleChoiceField(queryset=Verb.objects.all().order_by('language__language','verb'),required=False, label='Глагол', widget=forms.SelectMultiple(attrs={'class':'form-control'}))
        example = forms.CharField(max_length=300,required=False, label='Пример', widget=forms.Textarea(attrs={'class':'form-control'}))
