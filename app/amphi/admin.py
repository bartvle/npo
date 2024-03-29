"""
"""


from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.admin import ModelAdmin
from django import forms

from npo.admin import admin_site

from .models import Input


#TODO: add data from 2015 and 2016
#TODO: let view by everyone
#TODO: only change own ones.


class InputAdmin(ModelAdmin):
    list_display = ('date', 'full_name', 'location', 'toads', 'frogs', 'salamanders', 'toads_death', 'frogs_death', 'salamanders_death', 'remark')
    list_display_links = ('date', 'full_name', 'location',)
    list_filter = ('date', 'location')

    def get_form(self, request, obj=None, **kwargs):
        """
        Limit choices for 'by' to corresponding group and set logged-in user as default (not if admin).
        """
        form = super(InputAdmin, self).get_form(request, obj, **kwargs)
        users = User.objects.filter(groups__pk=2)
        user = request.user
        if user in users:
            form.base_fields['by'].choices = [(user.pk, user.get_full_name()) for user in users]
            form.base_fields['by'].initial = user            
        return form

    def full_name(self, instance):
        if instance.by is None:
            return 'Ander'
        else:
            return instance.by.first_name + ' ' + instance.by.last_name
    full_name.short_description = _('by')


admin_site.register(Input, InputAdmin)
