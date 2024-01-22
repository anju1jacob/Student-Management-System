from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, student, teacher, department
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request,'home.html')

def loging(request):
    if request.method == "POST":
       username = request.POST['username']
       password = request.POST['password']
       userpass = authenticate(request,username=username, password=password)
       if userpass is not None and userpass.is_superuser==1:
           return redirect('admin_home')
       elif userpass is not None and userpass.is_staff==1:
           login(request, userpass)
           request.session['teacher_id']=userpass.id
           return redirect('teacher_home')
       elif userpass is not None and userpass.is_active==1:
           login(request, userpass)
           request.session['stud_id']=userpass.id
           return redirect('stud_home')
       else:
        return HttpResponse("Invalid login")
    else:
        return render(request,'loging.html')
    

def stud_reg(request):
    if request.method =='POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        mail = request.POST['mail']
        un = request.POST['username']
        pwd = request.POST['pwd']
        dept = request.POST['dept']
        address = request.POST['address']
        phn = request.POST['phone']
        
        a = User.objects.create_user(first_name=fn, last_name=ln, email=mail, username=un, password=pwd, 
                                     usertype='student', is_staff=False, is_active=False)
        a.save()
        b = department.objects.create(dept_name=dept)
        b.save()
        z = student.objects.create(stud_id=a, dept_id=b, address=address, phone=phn)
        z.save()
        return redirect('home')
    else:
        return render(request,'stud_reg.html')
    
#Admin Module......

def admin_home(request):
    total_students = student.objects.count()
    total_teachers = teacher. objects.count()
    return render(request,'admin_home.html',{'count':total_students, 'total':total_teachers})

def admin_teacher(request):
    return render(request,'admin_teacher.html')

def teacher_reg(request):
    if request.method =='POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        mail = request.POST['mail']
        un = request.POST['username']
        pwd = request.POST['pwd']
        dept = request.POST['dept']
        salary = request.POST['salary']
        experience = request.POST['experience']
        address = request.POST['address']
        phn = request.POST['phone']
        
        a = User.objects.create_user(first_name=fn, last_name=ln, email=mail, username=un, password=pwd, 
                                     usertype='teacher', is_staff=True, is_active=True)
        a.save()
        b = department.objects.create(dept_name=dept)
        b.save()
        z = teacher.objects.create(teacher_id=a,dept_id=b, address=address, phone=phn,salary=salary, experience=experience)
        z.save()
        return redirect('admin_teacher')
    else:
        return render(request,'teacher_reg.html')
    
def admin_viewteacher(request):
    view = teacher.objects.select_related('teacher_id','dept_id').all()
    return render(request,'admin_viewteacher.html',{'views':view})

def del_teacher(request,id):
    teach = teacher.objects. get(id=id)
    user_id =teach.teacher_id.id 
    deptid=teach.dept_id.id
    teach.delete()
    User.objects.filter(id=user_id).delete()
    department.objects.filter(id=deptid).delete()
    return redirect('admin_viewteacher')

def admin_deptwisecount(request):
    cs_dept_count = teacher.objects.filter(dept_id__dept_name='CSE').count()
    ec_dept_count = teacher.objects.filter(dept_id__dept_name='ECE').count()
    ce_dept_count = teacher.objects.filter(dept_id__dept_name='CE').count()
    me_dept_count = teacher.objects.filter(dept_id__dept_name='ME').count()
    ee_dept_count = teacher.objects.filter(dept_id__dept_name='EEE').count()

    cs = student.objects.filter(dept_id__dept_name='CSE').count()
    ec = student.objects.filter(dept_id__dept_name='ECE').count()
    ce = student.objects.filter(dept_id__dept_name='CE').count()
    me = student.objects.filter(dept_id__dept_name='ME').count()
    ee = student.objects.filter(dept_id__dept_name='EEE').count()

    return render(request, 'admin_deptwisecount.html', {'cs_dept_count': cs_dept_count, 'ec_dept_count': ec_dept_count, 'ce_dept_count': ce_dept_count,
        'me_dept_count': me_dept_count, 'ee_dept_count': ee_dept_count, 'cs': cs, 'ec': ec, 'ce': ce, 'me': me, 'ee': ee })


def admin_student(request):
    return render(request,'admin_student.html')

def admin_viewstud(request):
    view = student.objects.select_related('stud_id','dept_id').all()
    return render(request,'admin_viewstud.html',{'views':view})

def del_stud(request,id):
    stud = student.objects. get(id=id)
    user_id =stud.stud_id.id 
    deptid=stud.dept_id.id
    stud.delete()
    User.objects.filter(id=user_id).delete()
    department.objects.filter(id=deptid).delete()
    return redirect('admin_viewstud')

def stud_accept(request):
    view = student.objects.select_related('stud_id','dept_id').all()
    return render(request,'stud_accept.html',{'views':view})

def confirm_stud(request,id):
    view = student.objects.select_related('stud_id').get(id=id)
    view.stud_id.is_active = True
    view.stud_id.save()
    return redirect('stud_accept')

# Student module....
def stud_home(request):
    stud_id = request.session.get('stud_id', None)
    if stud_id is not None: 
        return render(request, 'stud_home.html')
    else:
        return HttpResponse("Invalid session data. Please log in again.")

def stud_teacher_view(request):
     stud_id = request.session.get('stud_id', None)
     if stud_id is not None:
         student_info = student.objects.get(stud_id=stud_id)
         y = student_info.dept_id.dept_name
         teachers =teacher.objects.filter(dept_id__dept_name=y)
         return render(request, 'stud_teacher_view.html', {'teachers': teachers})
    
    
def stud_detail(request):
    stud_id = request.session.get('stud_id', None)
    if stud_id is not None:
        # Assuming stud_id is a ForeignKey to User in your student model
        student_info = student.objects.get(stud_id=stud_id)
        return render(request, 'stud_detail.html', {'context':student_info})
    
def stud_edit(request,id):
    student_info = student.objects.get(id=id)
    return render(request,"stud_update.html",{'edit':student_info})

def stud_update(request,id):
    if request.method =="POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        mail = request.POST['mail']
        un = request.POST['username']
        address = request.POST['address']
        phn = request.POST['phone']
        y = student.objects.get(id=id)
        y.address=address
        y.phone=phn
        y.save()

        user_obj =y.stud_id
        user_obj.first_name = fn
        user_obj.last_name = ln
        user_obj.email = mail
        user_obj.username = un
        user_obj.save()
        return redirect('stud_detail')
    else:
        return render(request,"stud_update.html")

    
# Teacher module...
def teacher_home(request):
    teacher_id = request.session.get('teacher_id', None)
    if teacher_id is not None: 
        return render(request,'teacher_home.html')
    else:
        return HttpResponse("Invalid session data. Please log in again.")

def teacher_detail(request):
    teacher_id = request.session.get('teacher_id', None)
    if teacher_id is not None:
        # Assuming stud_id is a ForeignKey to User in your student model
        teacher_info = teacher.objects.get(teacher_id=teacher_id)
        return render(request, 'teacher_detail.html', {'context':teacher_info})

def teacher_stud_view(request):
     teacher_id = request.session.get('teacher_id', None)
     if teacher_id is not None:
         teacher_info = teacher.objects.get(teacher_id=teacher_id)
         y = teacher_info.dept_id.dept_name
         students =student.objects.filter(dept_id__dept_name=y)
         return render(request, 'teacher_stud_view.html', {'students': students})
    
def teacher_edit(request,id):
    teacher_info = teacher.objects.get(id=id)
    return render(request,"teacher_update.html",{'edit':teacher_info})


def teacher_update(request,id):
    if request.method =="POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        mail = request.POST['mail']
        un = request.POST['username']
        salary = request.POST['salary']
        experience = request.POST['experience']
        address = request.POST['address']
        phn = request.POST['phone']
        y = teacher.objects.get(id=id)
        y.salary=salary
        y.experience=experience
        y.address=address
        y.phone=phn
        y.save()

        user_obj =y.teacher_id
        user_obj.first_name = fn
        user_obj.last_name = ln
        user_obj.email = mail
        user_obj.username = un
        user_obj.save()
        return redirect('teacher_detail')
    else:
        return render(request,"teacher_update.html")
    
def Logouts(reuest):
    logout(reuest)
    return redirect('home')