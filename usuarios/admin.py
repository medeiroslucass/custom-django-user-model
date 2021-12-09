from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUsuarioCreationForm, CustomUsuarioChangeForm
from .models import CustomUsuario

@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioCreationForm
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display = ('first_name', 'last_name', 'email', 'tel', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informacoes Pessoais', {'fields' : ('first_name' , 'last_name', 'tel')}),
        ('Permissoes', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permission')}),
        ('Datas Importantes', {'fields' : ('last_login', 'date_joined')}),
    )

