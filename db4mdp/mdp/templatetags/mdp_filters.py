from django import template

register = template.Library()

@register.filter(name = "index_access")
def accessing_elements(list_name, index):
    #print(index, list_name)
    return list_name[index]
