from django.contrib import admin
from .models import Usuario
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UsuarioAdmin(UserAdmin):
    #Campos que se mostrarán en la lista de usuarios
    list_display = ('username', 'email', 'is_staff', 'is_active')
    #Campos que se usarán para buscar usuarios  
    list_filter = ('is_staff', 'is_superuser', 'is_active')

    #Campos que se mostrarán al editar un usuario
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permisos', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login','date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 
                       'password2', 'is_staff', 'is_active')},
        ),
    )
    search_fields = ('username', 'email')   
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)
    
admin.site.register(Usuario, UsuarioAdmin)