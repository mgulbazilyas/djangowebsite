from django.contrib import admin

# Register your models here.
from servayapp.models import Topic, Webpage

admin.site.register(Topic)
admin.site.register(Webpage)