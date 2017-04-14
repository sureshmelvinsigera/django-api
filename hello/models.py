from django.db import models
#__str__()
from django.utils.encoding import python_2_unicode_compatible
#Create forms
from django.forms import ModelForm

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Gym(models.Model):
    gym_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

#This class must be introduced before it can be referenced
class MuscleGroup(models.Model):
    muscle_group = models.CharField(max_length=50)
    
    #Make single object to show "Chest" instead of "MuscleGroup object"
    def __str__(self):
        return self.muscle_group
    
class Excercise(models.Model):
    excercise = models.CharField(max_length=100)
    muscle_group = models.ForeignKey(
        MuscleGroup,
        on_delete = models.SET_NULL,
        blank = True,
        null = True,)
    
    def __str__(self):
        return self.excercise
        
class RndProgram(models.Model):
    
    def create():
        return Excercise.objects.all
        
        
    class Meta:
        #Do not create a database table
        managed = False
        

        
    