from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)
     
    def __str__(self):
       return f'{self.deptno}'
    
class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    mgr=models.IntegerField(null=True)
    hiredate=models.DateField()
    sal=models.IntegerField()
    comission=models.IntegerField(null=True)
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.empno}'