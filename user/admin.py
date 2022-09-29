from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from user.forms import UserAdminChangeForm, UserAdminCreationForm
from user.models import *


# Register your models here.
# admin.site.register(Hotel_user_table)
class UserAdmin(BaseUserAdmin, admin.ModelAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('email','fullName','role')
    list_filter = ('role','active')
    ordering = ('id',)

    fieldsets = (
        (None,{'fields': ('email', 'password')}),

        ('Personal Details',{'fields': ('fullName', 'contactNumber')}),
        ('Auth Details',{'fields': ('role', 'active','staff','admin')}),
    )

    add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2','role')}
            ),
        )


admin.site.register(User, UserAdmin)
