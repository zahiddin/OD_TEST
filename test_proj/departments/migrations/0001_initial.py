# Generated by Django 4.0.6 on 2022-07-30 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название школы')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создание школы')),
            ],
        ),
        migrations.CreateModel(
            name='ClassGrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название класса')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_classes', to='departments.school')),
            ],
        ),
    ]
