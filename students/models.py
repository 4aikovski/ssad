from django.db import models

# Create your models here.

class student(models.Model):
    last_name = models.CharField(verbose_name="Фамилия",max_length=50)
    First_name = models.CharField(verbose_name="Имя",max_length=50)
    Second_name = models.CharField(verbose_name="Отчество",max_length=50,blank=True,null=True)
    numver = models.CharField(verbose_name="Номер Зачётки",max_length=10)
    birthday = models.DateField(verbose_name="Дата Рождения",max_length=10,blank=True, null = True)

    def __str__(self) -> str:
        result = f"{self.last_name} {self.First_name[0]}"
        if self.Second_name:
            result += f"{self.Second_name[0]}"
        return result
    
    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
