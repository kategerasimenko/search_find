from django.contrib import admin
from search_find_verbs.models import *

admin.site.register(MeaningType)
admin.site.register(Language)

class MeaningInline(admin.TabularInline):
    model = MeaningExample
    extra = 1
    verbose_name_plural = 'Meanings with specifications and context examples'

class LanguageInline(admin.TabularInline):
    model = LanguageExample

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):

        field = super(LanguageInline, self).formfield_for_foreignkey(db_field, request, **kwargs)

        if db_field.name == 'meaning':
            if request._obj_ is not None:
                field.queryset = field.queryset.filter(field__exact = request._obj_)  
            else:
                field.queryset = field.queryset.none()

        return field

    extra = 1
    ordering = ('meaning',)
    verbose_name_plural = 'Meanings in different languages'
 
@admin.register(SemanticField)
class SemanticFieldAdmin(admin.ModelAdmin):
    inlines = (MeaningInline, LanguageInline)
    ordering = ('field',)
    fields = ('field','comments')

    def get_form(self, request, obj=None, **kwargs):
        # just save obj reference for future processing in Inline
        request._obj_ = obj
        return super(SemanticFieldAdmin, self).get_form(request, obj, **kwargs)

@admin.register(Meaning)    
class MeaningAdmin(admin.ModelAdmin):
    fieldsets = (('Info',{'fields':(('meaning_type','meaning'),('object_ref','object_animacy','purpose'))}),)
    ordering = ('meaning_type','meaning','object_ref','object_animacy','purpose')

@admin.register(Verb)     
class Verb(admin.ModelAdmin):
    ordering = ('language','verb')
