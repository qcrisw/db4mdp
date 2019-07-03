from django import forms
from django.contrib import admin
from django.contrib.admin.models import LogEntry, DELETION
from django.utils.html import escape
from django.urls import reverse
from django_postgres_extensions.admin.options import PostgresAdmin
from .models import MDP, Enrichment, Languages, QualityMeasure, Task, Reference, AboutPage, HandlingAbility, MathJaxFormulas
from import_export.admin import ImportExportModelAdmin
from .resources import *

#from django.contrib.admin import AdminSite
#class MyAdminSite(AdminSite):
#    site_url = "/admin/make_changes"

admin.site.site_header  = "DB4MDP Admin"
admin.site.site_title   = "DB4MDP Admin Portal"
admin.site.index_title  = "Welcome to the DB4MDP Admin Portal"
admin.site.site_url     = "/mdp"

#class QuickFilter(admin.SimpleListFilter):
#    title = 'Name'
#    parameter_name = 'quick_filter'

#    def lookups(self, request, model_admin):
#        return(
#            ('1', 'True')
#            ('0', 'False')
#        )

#    def queryset(self, request, queryset):
#        if self.value() == '1':
#            return queryset.annotate(Count('items')).filter(items__count__gte=2)
#        return queryset
 
#class MDPAdminForm(forms.ModelForm):
#  class Meta:
#    model = MDP
#    widgets = {
#      'multiple_select_and_freetext': MSAFWidget(),
#    }
#    fields = '__all__'

class WidAttrOverride(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(WidAttrOverride, self).__init__(*args, **kwargs)
        print(self.fields)
        index_specifiers = ['complexity', 'citation', 'technique_handling_ability', 'mathjaxeqn', 'python', 'best_mdp_list']
        for i in range(len(index_specifiers)):
            if self.fields.get(index_specifiers[i]):
                index = i
                break
        placeholders = [
                            ['PCA', 'Principal Component Analysis', 'iPCA, etc.', 'Enter your comments here...'
                             ],
                            ['Enter the reference here (ID automatically generated)'
                             ],
                            ['Enter a new ability for a technique to have towards handling a particular criterion'
                             ],
                            ['Enter the MathJax equation (with LaTeX formatting)'
                             ],
                            ['Enter a new progamming language'
                             ],
                            ['Dimension Synthesis','$$ scr{\M} $$','PCA, iPCA, ...', 'Fill this to specify the suggested tasks to be performed prior to this one','Fill this field to specify the tasks that inherit from the results obtained after performing this task']
                       ]
        i=0
        for field_name in self.fields:
            field = self.fields.get(field_name)  
            if field:
                if type(field.widget) in (admin.widgets.AdminTextInputWidget, forms.TextInput):
                    print(field, field.widget)
                    if field.label:
                        field.widget = admin.widgets.AdminTextInputWidget(attrs={'placeholder': placeholders[index][i]})
                        i+=1
                    else:
                        field.widget = forms.TextInput(attrs={'placeholder': 'Enter your data here'})
        descr_field = self.fields.get('description')
        if descr_field:
            descr_field.widget = admin.widgets.AdminTextareaWidget(attrs={'placeholder': placeholders[index][-1]})
    #class Meta:
    #    model = DemoModel

@admin.register(MathJaxFormulas)
class MathJaxAdmin(ImportExportModelAdmin):
    pass

@admin.register(HandlingAbility)
class HandlingAdmin(ImportExportModelAdmin):
    pass

@admin.register(MDP)
class MDPAdmin(ImportExportModelAdmin):
    form = WidAttrOverride
    list_display=('projection_name', 'mdp_id')
    list_filter = [
        'dissimilarity',
        'ordinal',
        'cartesian',
        'ne_structures',
        'categorical',
        'linearity',
        'supervision',
        'multi_level',
        'locality',
        'steerability',
        'stability',
        'out_of_core_data'
    ]
    fieldsets = (
        (None, {
            'fields': (
                ('mdp_name', 'mdp_fullname'),
            )
        }),
        ('Data Type', {
            'classes': ('collapse',),
            'fields': (
                            ('dissimilarity', 'ordinal', 'cartesian'),
                            ('ne_structures', 'categorical',),
                      )
        }),
        ('Properties', {
            'classes': ('collapse',),
            'fields':  (
                            ('linearity','supervision', 'multi_level'),
                            ('locality', 'steerability', 'stability', 'out_of_core_data'),\
                       )
        }),
        ('References', {
            'classes': ('collapse',),
            'fields': ('reference_list', )
        }),
        ('Complexity', {
            'classes': ('collapse',),
            'fields': ('complexity',)
        }),
        ('Programming Languages Handled', {
            'classes': ('collapse',),
            'fields': ('langs_handled',)
        }),
        ('Variants of the Technique', {
            'classes': ('collapse',),
            'fields': ('tech_variants','variant_refs')
        }),
        (None, {
            'fields': ('description',)
        }),
    )
    filter_horizontal = ['reference_list', 'complexity', 'langs_handled', 'variant_refs']
    search_fields = ['mdp_name']
    #readonly_fields = ('mdp_id')
    resource_class = MDPResource

@admin.register(Enrichment)
class EnrichmentAdmin(ImportExportModelAdmin):
    list_display=('enrichment_name','enrichment_type')
    list_filter = [
        'enrichment_type'
    ]
    resource_class = EnrichmentResource

@admin.register(Languages)
class LanguageAdmin(ImportExportModelAdmin):
    list_display=('language_name', 'language_id')
    search_fields = ['language_name']
    resource_class = LanguagesResource

#@admin.register(Variants)
#class VariantAdmin(ImportExportModelAdmin):
#    list_display=('mdp_name', 'variant_id', 'variants')
#    search_fields = ['variants','mdp_name']
#    resource_class = VariantResource

@admin.register(QualityMeasure)
class QMAdmin(ImportExportModelAdmin):
    fields = [
                ('measure_id', 'measure_name', 'best'),    
                ('local','globall'),
                ('dissimilarity','correlation','probability','rank'),
                ('geometric','set_difference', 'homology'),
                'rangee',
                'reference'
    ]
    list_display=('measure_name', 'measure_id', 'best')
    list_filter = [
        'local',
        'globall',
        'dissimilarity',
        'correlation',
        'probability',
        'rank',
        'geometric',
        'set_difference',
        'homology',
        'rangee',
        'best'
    ]
    search_fields = ['measure_name']
    resource_class = QualityResource

@admin.register(Task)
class TaskAdmin(ImportExportModelAdmin):
    fields = [
                'task_name',
                ('task_type', 'task_property'),
                ('input_space', 'output_space'),
                'actor',
                'ts',
                ('best_mdp_list', 'mdp_id'),
                ('parent_id', 'child_id'),
                'task_subset',
                'reference_list'
    ]
    list_display=('task_name', 'task_id', 'task_type')
    list_filter = [
        'actor',
        'task_property',
        'task_type'
    ]
    search_fields = ['task_name']
    resource_class = TaskResource

@admin.register(Reference)
class ReferenceAdmin(ImportExportModelAdmin):
    form = WidAttrOverride
    fields = ['citation']
    list_display = ('citation', 'id')
    search_fields = ['citation']
    resource_class = RefResource

@admin.register(AboutPage)
class AboutAdmin(ImportExportModelAdmin):
    list_display = ('name', 'email')
    search_fields = ['name', 'email']
    resource_class = AboutResource


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    date_hierarchy = 'action_time'
    readonly_fields = ('content_type',
        'user',
        'action_time',
        'object_id',
        'object_repr',
        'action_flag',
        'change_message'
    )
    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]
    search_fields = [
        'object_repr',
        'change_message'
    ]
    list_display = [
        'action_time',
        'user',
        'content_type',
        'object_link',
        'action_flag',
        'change_message',
    ]
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser and request.method != 'POST'
    def has_delete_permission(self, request, obj=None):
        return False
    def get_actions(self, request):
        actions = super(LogEntryAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
    def object_link(self, obj):
        if obj.action_flag == DELETION:
            link = escape(obj.object_repr)
        else:
            ct = obj.content_type
            link = u'<a href="%s">%s</a>' % (
                reverse('admin:%s_%s_change' % (ct.app_label, ct.model), args=[obj.object_id]),
                escape(obj.object_repr),
            )
        return link
    object_link.allow_tags = True
    object_link.admin_order_field = 'object_repr'
    object_link.short_description = u'object'    
    def queryset(self, request):
        return super(LogEntryAdmin, self).queryset(request) \
            .prefetch_related('content_type')


#admin.site.register(LogEntry, LogEntryAdmin)
    
#admin.site.register(MDP, MDPAdmin)
#admin.site.register(Enrichment, EnrichmentAdmin)
#admin.site.register(Languages, LanguageAdmin)
#admin.site.register(Variants, VariantAdmin)
#admin.site.register(QualityMeasure, QMAdmin)
#admin.site.register(Task, TaskAdmin)

#admin_site = MyAdminSite(name='myadmin')


