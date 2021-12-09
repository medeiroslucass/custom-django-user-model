from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    use_in_migrations = True  # Avisa ao django que isso virara uma tabela

    def _create_user(self,email,password, **extra_fields):
        if not email:
            raise ValueError('O email é obrigatorio.')
        
        email= self.normalize_email(email) # Forma para facilitar o entendimento dos caracteres no banco
        user = self.model(email=email, username=email, **extra_fields) # oq sera passado ao usuario
        user.set_password(password) # criptografa a senha
        user.save(using=self._db) # salva usando o banco
        return user
    
    def create_user (self,email,password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email,password, **extra_fields)

    def create_superuser(self,email,password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super useer precisa de superuser como true')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Staff precisa de is_staff como true')

        return self._create_user(email,password, **extra_fields)



class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True, )
    tel = models.CharField('Telefone', max_length=15)
    is_staff = models.BooleanField('Membro da Equipe', default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'tel']

    def __str__(self):
        return self.email

    objects = UsuarioManager()