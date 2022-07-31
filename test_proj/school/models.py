from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class MyUserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, phone, password, **extra_fields):
        """Create and save a User with the given email and password."""
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, phone, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)
    def create_superuser(self, phone, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(phone, password, **extra_fields)


class Teacher(AbstractUser):
    phone = models.CharField(verbose_name='Номер телефона', max_length=255, unique=True)
    subject = models.CharField(verbose_name='Предмет', max_length=255)
    classgrade = models.OneToOneField(to='departments.ClassGrade', on_delete=models.SET_NULL,
                                      related_name='class_teacher', null=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELD = []

    def __str__(self):
        return self.phone


class Student(models.Model):
    full_name = models.CharField(verbose_name='Фио', max_length=255)
    mail_address = models.EmailField(max_length=255)
    birthdate = models.DateField(verbose_name='Дата рождения')
    classgrade = models.ForeignKey(to='departments.ClassGrade', on_delete=models.SET_NULL,
                                   related_name='class_students', null=True)
    address = models.CharField(verbose_name='Адресс проживания', max_length=255)
    GENDER_CHOICES = (
        ('M', 'Мальчик'),
        ('F', 'Девочка'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    photo = models.FileField('Аватарка', upload_to='student_photos/', null=True)

    def __str__(self):
        return f'{self.full_name} {self.classgrade}'

