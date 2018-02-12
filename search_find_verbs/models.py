from __future__ import unicode_literals

from django.db import models

OBJECT_REF_CHOICES = (
    ('ref_def','референтный определенный'),
    ('ref_indef','референтный неопределенный'),
    ('nonref','нереферентный'),
    ('abstr','абстрактный')
)

OBJECT_ANIMACY_CHOICES = (
    ('anim','одушевленный'),
    ('inan','неодушевленный'),
    ('noobj','безобъектное')
)

PURPOSE_CHOICES = (
    ('purp','умышленно'),
    ('byacc','случайно')
)

class SemanticField(models.Model):
    field = models.CharField(max_length=30,)
    comments = models.TextField(blank=True,default='')
    
    def __str__(self):
        return self.field

        
class MeaningType(models.Model):
    meaning_type = models.CharField(max_length=30,)
    
    def __str__(self):
        return self.meaning_type

        
class Meaning(models.Model):
    meaning_type = models.ForeignKey('MeaningType')
    meaning = models.CharField(max_length=100,)
    object_ref = models.CharField(max_length=10,choices=OBJECT_REF_CHOICES,blank=True,default='')
    object_animacy = models.CharField(max_length=5,choices=OBJECT_ANIMACY_CHOICES,blank=True,default='')
    purpose = models.CharField(max_length=5,choices=PURPOSE_CHOICES,blank=True,default='')
    
    def __str__(self):
        return ' - '.join([str(self.meaning_type),self.meaning,self.object_ref,self.object_animacy,self.purpose])

        
class MeaningExample(models.Model):
    meaning = models.ForeignKey('Meaning')
    field = models.ForeignKey('SemanticField')
    specification = models.CharField(max_length=200,blank=True)
    example = models.TextField()
    
    def __str__(self):
        return  self.example[:100]

        
class Language(models.Model):
    language = models.CharField(max_length=30,)
    
    def __str__ (self):
        return self.language

    
class Verb(models.Model):
    language = models.ForeignKey('Language')
    verb = models.CharField(max_length=30,)
    
    def __str__(self):
        return  ' - '.join([str(self.language),self.verb])
 
 
class LanguageExample(models.Model):
    meaning = models.ForeignKey('MeaningExample')
    field = models.ForeignKey('SemanticField')
    language = models.ForeignKey('Language')
    verbs = models.ManyToManyField('Verb')
    example = models.TextField(blank=True)


