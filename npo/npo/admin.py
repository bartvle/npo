"""
"""


from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin


class AdminSite(AdminSite):
    """
    """
    pass


admin_site = AdminSite()

admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
