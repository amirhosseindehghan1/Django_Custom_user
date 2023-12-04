from django.contrib import admin
from Account.models import MyUser
from django.contrib.auth.admin import UserAdmin


class MyUserAdmin(UserAdmin):
    list_display = ('email', 'mobile', 'first_name', 'last_name', 'is_active', 'is_staff','is_superuser')
    list_editable = ['is_active']


    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'mobile')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


    def get_fieldsets(self, request, obj=None):
        fs = super().get_fieldsets(request, obj)

        new_fieldsets = []
        for fieldset in fs:
            if 'username' in fieldset[1]['fields']:
                new_fields = list(fieldset[1]['fields'])
                new_fields.remove('username')
                fieldset = (fieldset[0], {'fields': new_fields})
            new_fieldsets.append(fieldset)

        return new_fieldsets


    ordering = ('email',)



    list_filter = ('is_superuser', 'is_active')


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'mobile', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )

admin.site.register(MyUser, MyUserAdmin)


