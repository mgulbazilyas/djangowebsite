from django.contrib import admin

# Register your models here.
from schools.models import School, Subject, ClassData, ProfessorData

admin.site.register(School)
admin.site.register(Subject)
admin.site.register(ClassData)
admin.site.register(ProfessorData)