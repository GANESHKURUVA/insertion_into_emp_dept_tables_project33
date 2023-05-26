from django.shortcuts import render
from app.models import *
# Create your views here.


def insert_dept(request):
    if request.method=='POST':
        deptno=request.POST['deptno']
        dname=request.POST['dname']
        loc=request.POST['loc']
        DE=Dept.objects.get_or_create(deptno=deptno,dname=dname,loc=loc)[0]
        DE.save()
    return render(request,'insert_dept.html')


def insert_emp(request):
    DPO=Dept.objects.all()
    d={'deptno':DPO}
    if request.method=='POST':
        deptno=request.POST['deptno']
        empno=request.POST['empno']
        enmae=request.POST['ename']
        job=request.POST['job']
        mgr=request.POST['mgr']
        hired=request.POST['hd']
        sal=request.POST['sal']
        comission=request.POST['comission']
        DO=Dept.objects.get(deptno=deptno)
        DO.save()
        EO=Emp.objects.get_or_create(empno=empno,ename=enmae,job=job,mgr=mgr,hiredate=hired,sal=sal,comission=comission,deptno=DO)[0]
        EO.save()
    return render(request,'insert_emp.html',d)