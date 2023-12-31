from abc import ABC

from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils import timezone

from account.models import User

continent_choices = [
    ('AFRIQUE', 'Afrique'),
    ('EUROPE', 'Europe'),
    ('AMERIQUE', 'Amerique'),
    ('OCEANIE', 'Océanie'),
    ('ASIE', 'Asie'),
]

CARD_TYPES = [
        ('PASSPORT', 'Passport'),
        ('CNI', 'CNI'),
    ]

role_type_choices = [
        ('ADMINISTRATION', 'Administration'),
        ('SOFTWARE', 'Software'),
    ]

SEXE_CHOICES=(
    ("HOMME", "HOMME"),
    ("FEMMME", "FEMME"),
    ("AUCUN", "AUCUN")
)

"""
#Base modelClass
class ModelBasic(ABC):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

###############################  Country class  ################################################
class Country(models.Model):
    __metaclass__ = ModelBasic
    continent = models.CharField(max_length=255, choices=continent_choices)
    name = models.CharField(max_length=255),
    indicatif = models.CharField(max_length=255)
    iso_code = models.CharField(max_length=255)

    def __str__(self):
        return None

#############################   Role class  #####################################################"
class Role(models.Model):
    __metaclass__ = ModelBasic

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=role_type_choices, default='Administration')
    description = models.CharField(max_length=255)
    add_enterprise_admin = models.BooleanField(default=False)
    add_employee = models.BooleanField(default=False)
    update_employee = models.BooleanField(default=False)
    view_employee = models.BooleanField(default=False)
    delete_employee = models.BooleanField(default=False)


    def __str__(self):
        return None



class Entreprise(models.Model):
    __metaclass__ = ModelBasic

    name = models.CharField(max_length=255)
    ifu = models.CharField(max_length=255)
    rccm = models.CharField(max_length=255)
    dirrector_card_id = models.CharField(max_length=255)
    dirrector_card_file = models.ImageField(default='default.png')
    dirrector_card_type = models.CharField(max_length=255, choices=CARD_TYPES)
    director_lastname = models.CharField(max_length=255)
    director_firstname = models.CharField(max_length=255)
    is_approved = models.BooleanField(default=False)
    logo = models.ImageField(default='default.png')
    description = models.CharField(max_length=255)
    request_to_use = models.CharField(max_length=255)
    #country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"




##############################  Entreprise Admin    ###################################

class EntrepriseAdmin(models.Model):
    __metaclass__ = ModelBasic
    user = models.OneToOneField(User, on_delete=models.CASCADE),
    is_active = models.BooleanField(default=True)
    job = models.CharField(max_length=100)
    job_description = models.CharField(max_length=100)
    is_creator = models.BooleanField(default=False)
    enterprises = models.ManyToManyField(Entreprise)
    roles = models.OneToOneField(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"




################################# Entreprise admin rôle     ################################"

class EntrepriseAdminRole(models.Model):
    __metaclass__ = ModelBasic
    is_active = models.BooleanField(default=False)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    entreprise_admin = models.ForeignKey(EntrepriseAdmin, on_delete=models.CASCADE)

    def __str__(self):
        return None


##########################  class Employee  ##################################
class Employee(models.Model):
    __metaclass__ = ModelBasic
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return None


################################# Class Qr  ############################

class Qr(models.Model):
    __metaclass__ = ModelBasic
    is_current = models.BooleanField(default=False)
    qr_code = models.CharField(max_length=255)
    qr_image = models.ImageField(default="default.png")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE )

    def __str__(self):
        return None



##################################  Classe Security Code ####################

class SecurityCode(models.Model):
    __metaclass__ = ModelBasic
    is_current = models.BooleanField(default=False)
    code = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

############################### class Face   ###############################
class Face(models.Model):
    __metaclass__ = ModelBasic
    is_main = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    face_file = models.ImageField(default="default.png")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)



############################### class Room ####################################

class Room(models.Model):
    __metaclass__ = ModelBasic
    designation = models.CharField(max_length=255)
    check_security_code = models.BooleanField(default=False)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)


    def __str__(self):
        return None

############################# class Employee Room
class EmployeeRoom(models.Model):
    __metaclass__ = ModelBasic
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __repr__(self):
        return None

#################################### Employee status class  ###########################

class EmployeeStatusLog(models.Model):
    __metaclass__ = ModelBasic
    status = models.BooleanField(default=False)
    date_start = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(auto_now=True)
    employee_log = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return None

"""