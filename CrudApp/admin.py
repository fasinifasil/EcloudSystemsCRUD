from django.contrib import admin
from django.contrib.auth.models import User


# Register your models here.
from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'active')
    search_fields = ('username',)
    list_filter = ('active',)
    ordering = ('username',)
    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'active')
        }),
    )
    readonly_fields = ('password',)

admin.site.register(User, UserAdmin)
