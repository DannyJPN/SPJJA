from django.db import models
from django.contrib.postgres.fields import ArrayField
import datetime
from django.core.exceptions import ValidationError

# Create your models here.

class Player(models.Model):
    birthdate = models.DateTimeField("Date of birth")
    name = models.CharField(max_length = 40)
    surname = models.CharField(max_length = 50)
    team = models.ForeignKey("Team",on_delete = models.PROTECT,null = True)
    wins =0
    loses  =0
    bilance =0.0
    def save(self,*args,**kwargs):
        if(datetime.date.today()<self.birthdate.date()):
            raise ValidationError("Error: future date")
        else:
            super(Player,self).save(*args,**kwargs)
         
    def age(self):
        return datetime.date.today().year - self.birthdate.date().year
        
        
    def __str__(self):
        return '{} {} ({})'.format(self.surname,self.name,self.birthdate.date())
    
    
class Team(models.Model):
    name = models.CharField(max_length = 100)
    leag_choices = (
                ("DL","District League"),
                ("RL","Regional League"),
                ("SL","State League"),
                ("EL","Extra League"),
                
            )
    league = models.CharField(max_length=20,choices=leag_choices,null=True)
    playerlist=[]
    def __str__(self):
       return self.name



class Match(models.Model):
    player1 = models.ForeignKey("Player",on_delete = models.PROTECT,null=False,related_name = "player1")
    player2 = models.ForeignKey("Player",on_delete = models.PROTECT,null=False,related_name = "player2")
    set1 =  models.CharField(max_length=3,null=True,blank=True)
    set2 =  models.CharField(max_length=3,null=True,blank=True)
    set3 =  models.CharField(max_length=3,null=True,blank=True)
    set4 =  models.CharField(max_length=3,null=True,blank=True)
    set5 =  models.CharField(max_length=3,null=True,blank=True)
    
    
    result1=0 
    result2=0 
    
    date_of_occ = models.DateTimeField("Date of occurrence")
    
    
    def is_number(self,s):
        if s is None:
            return True
        try:
            int(s)
            return True
        except ValueError:
            pass
 
        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
 
        return False
    
    def valid_sets(self):
        pos=0
        neg=0
        sets = (self.set1,self.set2,self.set3,self.set4,self.set5)
        for one in sets:
            
            if self.is_number(one) is False and one is not None:
                
                return False
            else:
                if one is None:
                    pass
                elif  int(one) <0:
                    neg +=1
                else:
                    pos+=1
            
        if (pos is 3 and neg<3 and neg >=0) or (neg is 3 and pos<3 and pos >=0):
            return True
        else:
            return False         
            
    def save(self,*args,**kwargs):
        
        if(datetime.date.today() < self.date_of_occ.date()):
            raise ValidationError("Error: future date")
        elif(self.valid_sets() is False):
           # raise ValidationError("Error: Not a number!!!!")
           pass
        else:
            super(Match,self).save(*args,**kwargs)
    
    
    def __str__(self):
       return '{}-{}\t{}:{}'.format(self.player1,self.player2,self.result1,self.result2)
        
    
        
        
