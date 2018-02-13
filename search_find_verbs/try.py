from django import forms
class SearchForm(forms.Form):
    semfield = forms.ModelMultipleChoiceField(queryset=SemanticField.objects.all().order_by('field'), required=False)
    meaning_type = forms.ModelMultipleChoiceField(queryset=MeaningType.objects.all(), required=False,
                                                  widget=forms.CheckboxSelectMultiple())
    meaning_choices = Meaning.objects.order_by('meaning').values_list('meaning', flat=True).distinct()
    meaning = forms.MultipleChoiceField(choices=zip(meaning_choices, meaning_choices), required=False)
    object_ref = forms.MultipleChoiceField(choices=OBJECT_REF_CHOICES, required=False,
                                           widget=forms.CheckboxSelectMultiple())
    object_animacy = forms.MultipleChoiceField(choices=OBJECT_ANIMACY_CHOICES, required=False,
                                               widget=forms.CheckboxSelectMultiple())
    purpose = forms.MultipleChoiceField(choices=PURPOSE_CHOICES, required=False, widget=forms.CheckboxSelectMultiple())
    language = forms.ModelMultipleChoiceField(queryset=Language.objects.all().order_by('language'), required=False)
    verb = forms.ModelMultipleChoiceField(queryset=Verb.objects.all().order_by('language__language', 'verb'),
                                          required=False)
    example = forms.CharField(max_length=300, required=False)

form = SearchForm()
labels = ['Семантическое поле', 'Тип значения', 'Значение', 'Объектная референция',
             'Одушевлённость объекта', 'Цель', 'Язык', 'Глагол', 'Пример']
print(form)