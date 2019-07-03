from django.db import models
from django import forms
from django.db.models.signals import post_save
from django.contrib.admin.models import LogEntry
from django.core.files import File
from .utils import run_on_save
from django.db import connection
import subprocess
file = open("new_changes.txt","w")


#set the unique=true aprameter for those parts of the model apart from the primary key that need to be unique (name etc.)
#Youre going to have to use model save overriding instead of using a post save signal because the save signal gets called whenever data is pushed into the database i.e. even on start up
#def run_on_save(sender,instance, **kwargs):
#    LogEntry.objects.all()
#    file = open("new_changes.txt","w")
#    file.write(changes)

#post_save.connect(run_on_save)

# Create your models here.

#instead of going through each individual class and changing their save methods, I'm just going to inherit in one class, change the save method and then inherit that class in all the 
#remaining models.

#class ModdedModel(models.Model):
#    def save(self, *args, **kwargs):
#        changes_file = ("new_changes.txt","w")
#        content2 = LogEntry.objects.all()
#        changes_file.write(content2)
#        super(ModdedModel, self).save(*args,**kwargs)   

class Reference(models.Model):
    #reference_id = models.AutoField(primary_key = True)
    citation = models.CharField(max_length = 250, unique = True)
    def __str__(self):
        return f'[{self.id}] {self.citation.strip()}'

class HandlingAbility(models.Model):
    #technique_handling_ability = models.CharField(max_length=2000, label='Enter a description of how the technique can handle the desired parameter')
    technique_handling_ability = models.CharField(max_length=2000)
    def __str__(self):
        return self.technique_handling_ability
    class Meta:
         verbose_name_plural = "Handling Abilities"

class MathJaxFormulas(models.Model):
    mathjaxeqn = models.CharField(max_length = 500, unique=True)
    def __str__(self):
        return self.mathjaxeqn
    class Meta:
         verbose_name_plural = "MathJax Formulae"

class Languages(models.Model):
    language_id =models.AutoField(primary_key=True)
    language_name = models.CharField('Programming Language',  max_length = 50, unique=True)
    reference_list =models.ManyToManyField(Reference, max_length=300)
    description = models.CharField('Comments/Description', null=True, blank=True, max_length = 2000)

    def _unicode_(self):
        return '/%s/' % self.language_name
    def get_absolute_url(self):
        return '/mdp/%s/' % self.language_id
    def __str__(self):
        return self.language_name
    class Meta:
         verbose_name_plural = "Programming Languages"

#Reduce number of many to many fields here. Could be done by incorporating them into another table but I don't think itll work because it's not a simple Yes/No selection. Each one of them has
#4 options base. Instead of fixing these, fix the other 4 options instead and then let the admin specify any extra info using the comments section.
class MDP(models.Model):
    mdp_id          = models.AutoField(primary_key=True)
    mdp_name        = models.CharField('MDP short form', max_length=500, unique = True)
    mdp_fullname    = models.CharField('MDP full form', max_length=500, unique = True)
    dissimilarity   = models.ManyToManyField(HandlingAbility, related_name = 'dissimilarity')
    ordinal         = models.ManyToManyField(HandlingAbility, related_name = 'ordinal')
    cartesian       = models.ManyToManyField(HandlingAbility, related_name = 'cartesian')
    ne_structures   = models.ManyToManyField(HandlingAbility, verbose_name = "Neighbouring Structures", related_name = 'ne_structures')
    categorical     = models.ManyToManyField(HandlingAbility, related_name = 'categorical')
    linearity       = models.ManyToManyField(HandlingAbility, related_name = 'linearity')
    supervision     = models.ManyToManyField(HandlingAbility, related_name = 'supervision')
    multi_level     = models.ManyToManyField(HandlingAbility, related_name = 'multi_level')
    locality        = models.ManyToManyField(HandlingAbility, related_name = 'locality')
    steerability    = models.ManyToManyField(HandlingAbility, related_name = 'steerability')
    stability       = models.ManyToManyField(HandlingAbility, related_name = 'stability')
    out_of_core_data= models.ManyToManyField(HandlingAbility, related_name = 'out_of_core_data')
    reference_list  = models.ManyToManyField(Reference, verbose_name = "List of References")
    complexity      = models.ManyToManyField(MathJaxFormulas, verbose_name = 'Complexity (MathJax)')
    langs_handled   = models.ManyToManyField(Languages, verbose_name = 'Languages Handled')
    tech_variants   = models.CharField(max_length = 200, null=True, blank=True)
    variant_refs    = models.ManyToManyField(Reference, related_name = 'variantrefs')
    description     = models.CharField('Comments/Description', null=True, blank=True, max_length = 2000)

    @property
    def projection_name(self):
        return f'{self.mdp_fullname} ({self.mdp_name.strip()})'

    #def queryset(self, request):
    #    qs = super(MyAdmin, self).queryset(request)
    #    qs = qs.order_by('mdp_id')
    #    return qs 

    def _unicode_(self):
        return '/%s/' % self.mdp_name
    def get_absolute_url(self):
        return '/mdp/%s/' % self.mdp_id
    def __str__(self):
        return self.mdp_name
    class Meta:
         verbose_name_plural = "Projection Techniques"
    
class QualityMeasure(models.Model):
    measure_id =models.AutoField(primary_key=True)
    measure_name= models.CharField(max_length=100, unique = True)
    local= models.CharField(max_length=100, null=True, blank=True)
    globall= models.CharField('Global', max_length=100, null=True, blank=True)
    dissimilarity= models.CharField(max_length=100, null=True, blank=True)
    correlation= models.CharField(max_length=100, null=True, blank=True)
    probability= models.CharField(max_length=100, null=True, blank=True)
    rank= models.CharField(max_length=100, null=True, blank=True)
    geometric= models.CharField(max_length=100, null=True, blank=True)
    set_difference= models.CharField(max_length=100, null=True, blank=True)
    homology= models.CharField(max_length=100, null=True, blank=True)
    rangee= models.CharField('Range (MathJax)', max_length=100)
    best= models.IntegerField('Best MDP')
    reference= models.CharField(max_length=100)
    description = models.CharField('Comments/Description', null=True, blank=True, max_length = 2000)
    def __str__(self):
        return self.measure_name
    class Meta:
         verbose_name_plural = "Quality Measures"

class TaskType:
    type_name = models.CharField(max_length = 100, unique=True)

class TaskProps:
    task_property = models.CharField(max_length = 100, unique = True)
    
class Task(models.Model):
    task_id =models.AutoField(primary_key=True)
    task_name= models.CharField(max_length=100, unique = True)
    task_type= models.ManyToManyField(TaskType)
    input_space= models.ManyToManyField(MathJaxFormulas)
    output_space= models.ManyToManyField(MathJaxFormulas)
    #create radio field for actor
    actor= models.CharField(max_length=100)
    ts= models.CharField(max_length=100)
    reference_list= models.ManyToManyField(max_length=100)
    best_mdp_list= models.CharField(max_length=200)
    task_property= models.ManyToManyField(TaskProps)
    parent_id = models.CharField(max_length = 100, null=True, blank=True)
    #parent = models.CharField(max_length = 150, null=True, blank = True)
    child_id = models.CharField(max_length = 50, null=True, blank = True)
    mdp_id =models.ForeignKey(MDP, on_delete=models.CASCADE)
    description = models.CharField('Comments/Description' , null=True, blank=True, max_length = 2000)
    task_subset = models.CharField('Specify the ID(s) of the tasks into which this main task is decomposed', max_length = 50, null=True, blank=True)
    def __str__(self):
        return self.task_name
    class Meta:
         verbose_name_plural = "Tasks"

class Enrichment(models.Model):
    enrichment_id =models.AutoField(primary_key=True)
    enrichment_name= models.CharField(max_length=100, unique = True)
    enrichment_type= models.CharField(max_length=100)
    references_type= models.CharField(max_length=100)
    description = models.CharField('Comments/Description', null=True, blank=True, max_length = 2000)
    def __str__(self):
        return (self.enrichment_name+' ('+str(self.enrichment_id)+')')
    def save(self, *args, **kwargs): 
        super(Enrichment, self).save(*args,**kwargs)    
        with open("new_changes.txt","w+") as changes_file:
            changes_file = File(changes_file)
            changes = LogEntry.objects.all()
            #print(changes)
            for change_made in changes:
                #print(change_made, changes)
                changes_file.write(str(change_made))
            changes_file.seek(0)
           # print(changes_file.read())
    class Meta:
         verbose_name_plural = "Enrichments"

class AboutPage(models.Model):
    name = models.CharField(max_length = 100)
    designation = models.CharField(max_length = 100)
    employee_of = models.CharField('Institute/Employer', max_length = 100)
    email = models.EmailField('Email address', max_length = 200)
    image_name = models.CharField('Image Name (New image to be saved in the static directory with the same name)', max_length = 50, default = "blank.png", blank = False) #set default
    def __str__(self):
        return self.name
    class Meta:
         verbose_name_plural = "Team Data"