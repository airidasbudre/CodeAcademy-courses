from django.contrib import admin

from .models import Project, Client, User, Work, Invoice, ClientAdmin, Profile, Employee
from import_export.admin import ImportExportModelAdmin
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('p_name', 'start_date', 'end_date', 'client')
    search_fields = ('client', 'p_name')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'company')

# class UserAdmin(admin.ModelAdmin):
#     list_display = ('name', 'surname', 'position')


class UserAdminForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

class UserAdmin(BaseUserAdmin):
    form = UserAdminForm
    add_form = UserAdminForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)



# Register your models here.
admin.site.register(Project)
admin.site.register(Client, ClientAdmin)
admin.site.register(Employee)
admin.site.register(Work)
admin.site.register(Invoice)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)

