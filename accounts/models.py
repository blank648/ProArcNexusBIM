from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)

class UtilizatorManager(BaseUserManager):
    #valideaza existenta username, utilizatori, roluri si profiluri
    def create_user(self, username, password=None, role='user', **extra_fields):
        if not username:
            raise ValueError('Username obligatoriu')
        user = self.model(username=username, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    #seteaza rolul admin, is_staff=True, is_superuser=True si apeleaza create_user
    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('role', 'admin')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

#atribuie user_id, username, parola_hash, role, is_active, is_staff
class Utilizator(AbstractBaseUser, PermissionsMixin):
    userID = models.BigAutoField(db_column='UserID', primary_key=True)
    username = models.CharField(db_column='Username', max_length=100, unique=True)
    parolahash = models.CharField(db_column='ParolaHash', max_length=255)

    role = models.CharField(
        db_column='Rol', max_length=20,
        choices=[('admin', 'Admin'), ('manager', 'Manager'), ('user', 'Utilizator')],
        default='user'
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UtilizatorManager()#manager custom

    USERNAME_FIELD = 'username'#folosit la login
    REQUIRED_FIELDS = []

    #nu creaza tabela, deoarece deja exista
    class Meta:
        db_table = 'Utilizator'
        managed = False

    def __str__(self):
        return self.username
