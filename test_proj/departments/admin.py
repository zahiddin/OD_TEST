from django.contrib import admin

from departments.models import School, ClassGrade


class ClassGradeInLine(admin.TabularInline):
    model = ClassGrade


class SchoolAdmin(admin.ModelAdmin):
    inlines = [
        ClassGradeInLine
    ]


admin.site.register(School, SchoolAdmin)
