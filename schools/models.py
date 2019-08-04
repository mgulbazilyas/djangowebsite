from django.db import models

# Create your models here.

class School(models.Model):
    school = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.school

class Subject(models.Model):
    school = models.ForeignKey(School,on_delete=True)
    subject = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.subject
class ClassData(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    class_number = models.IntegerField()
    class_size = models.IntegerField()

    def __str__(self):
        return str(self.class_number)

class ProfessorData(models.Model):
    classData = models.ForeignKey(ClassData,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(primary_key=True)

    def __str__(self):
        return self.last_name+", "+self.first_name