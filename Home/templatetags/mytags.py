from django.contrib.auth.models import Group
from django import template
from Home.models import Comment


register=template.Library()
@register.filter(name='has_group')
def has_group(user,group_name):
    return user.groups.filter(name=group_name).exists()

@register.filter
def obj_del(user,comment):
   
    if user.has_perm('Home.delete_comment',comment):
        return True
    else:
        return False

