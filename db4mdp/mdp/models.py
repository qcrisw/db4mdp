from django.db import models

# Create your models here.
class MDP(models.Model):
    mdp_id =models.IntegerField(primary_key=True)
    mdp_name= models.CharField(max_length=100)
    mdp_fullname= models.CharField(max_length=100)
    reference =models.CharField(max_length=100)
    dissimilarity =models.CharField(max_length=100)
    ordinal=models.CharField(max_length=100)
    cartesian=models.CharField(max_length=100)
    ne_structures=models.CharField(max_length=100)
    categorical=models.CharField(max_length=100)
    linearity=models.CharField(max_length=100)
    supervision=models.CharField(max_length=100)
    multi_level=models.CharField(max_length=100)
    locality=models.CharField(max_length=100)
    steerability=models.CharField(max_length=100)
    stability=models.CharField(max_length=100)
    out_of_core_data=models.CharField(max_length=100)
    complexity=models.CharField(max_length=100)
    complexity_name=models.CharField(max_length=100)
    
    def _unicode_(self):
        return '/%s/' % self.mdp_name
    def get_absolute_url(self):
        return '/mdp/%s/' % self.mdp_id
    def __str__(self):
        return self.mdp_name
    
class Languages(models.Model):
    language_id =models.IntegerField(primary_key=True)
    mdp_name= models.CharField(max_length=100)
    mdp_id =models.ForeignKey(MDP, on_delete=models.CASCADE)
    reference_list =models.CharField(max_length=100)
    cplusplus =models.CharField(max_length=100)
    java =models.CharField(max_length=100)
    python =models.CharField(max_length=100)
    matlab =models.CharField(max_length=100)
    javascript =models.CharField(max_length=100)
    r=models.CharField(max_length=100)

    def _unicode_(self):
        return '/%s/' % self.mdp_name
    def get_absolute_url(self):
        return '/language/%s/' % self.language_id

class Variants(models.Model):
    variant_id =models.IntegerField(primary_key=True)
    mdp_name= models.CharField(max_length=100)
    variants=models.CharField(max_length=100)
    variant_reference=models.CharField(max_length=100)
    mdp_id =models.ForeignKey('MDP', on_delete=models.CASCADE)

class QualityMeasure(models.Model):
    measure_id =models.IntegerField(primary_key=True)
    measure_name= models.CharField(max_length=100)
    local= models.CharField(max_length=100)
    globall= models.CharField(max_length=100)
    dissimilarity= models.CharField(max_length=100)
    correlation= models.CharField(max_length=100)
    probability= models.CharField(max_length=100)
    rank= models.CharField(max_length=100)
    geometric= models.CharField(max_length=100)
    set_difference= models.CharField(max_length=100)
    homology= models.CharField(max_length=100)
    rangee= models.CharField(max_length=100)
    rangee_name= models.CharField(max_length=100)
    best= models.IntegerField()
    reference= models.CharField(max_length=100)
    
class Task(models.Model):
    task_id =models.IntegerField(primary_key=True)
    task_name= models.CharField(max_length=100)
    task_type= models.CharField(max_length=100)
    input_space= models.CharField(max_length=100)
    input_space_name= models.CharField(max_length=100)
    output_space= models.CharField(max_length=100)
    output_space_name= models.CharField(max_length=100)
    actor= models.CharField(max_length=100)
    ts= models.CharField(max_length=100)
    reference_list= models.CharField(max_length=100)
    best_mdp_list= models.CharField(max_length=100)
    task_property= models.CharField(max_length=100)
    mdp_id =models.ForeignKey(MDP, on_delete=models.CASCADE)

class Enrichment(models.Model):
    enrichment_id =models.IntegerField(primary_key=True)
    enrichment_name= models.CharField(max_length=100)
    enrichment_type= models.CharField(max_length=100)
    references_type= models.CharField(max_length=100)



