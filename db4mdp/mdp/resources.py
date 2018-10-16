from import_export import resources
from .models import QualityMeasure,MDP, Variants,Task, Enrichment, Languages

# for quality basic and advanced
class QualityResource(resources.ModelResource):
    class Meta:
        model = QualityMeasure

# for mdp basic and advanced
class MDPResource(resources.ModelResource):
    class Meta:
        model = MDP
        
#for basic and advanced
class TaskResource(resources.ModelResource):
    class Meta:
        model = Task

#for basic 
class EnrichmentResource(resources.ModelResource):
    class Meta:
        model = Enrichment
class LanguagesResource(resources.ModelResource):
    class Meta:
        model = Languages


