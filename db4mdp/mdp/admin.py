from django.contrib import admin
from django_postgres_extensions.admin.options import PostgresAdmin
from .models import MDP

class MDPAdmin(admin.ModelAdmin):
    list_display=('mdp_name',)
    
admin.site.register(MDP, MDPAdmin)
