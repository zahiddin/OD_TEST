from django.db import models


class School(models.Model):
    title = models.CharField(verbose_name='Название школы', max_length=255)
    created_date = models.DateTimeField('Дата и время создание школы', auto_now_add=True)

    def __str__(self):
        return self.title


class ClassGrade(models.Model):
    title = models.CharField(verbose_name='Название класса', max_length=255)
    school = models.ForeignKey(to='School', on_delete=models.CASCADE, related_name='school_classes')

    def __str__(self):
        return self.title
