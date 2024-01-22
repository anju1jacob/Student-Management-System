"""
URL configuration for clgdb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from clgdbapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("loging", views.loging, name="loging"),
    path("stud_reg", views.stud_reg, name="stud_reg"),
    path("Logouts", views.Logouts, name="Logouts"),

    #admin module.....
    path("admin_home", views.admin_home, name="admin_home"),
    path("admin_teacher", views.admin_teacher, name="admin_teacher"),
    path("teacher_reg", views.teacher_reg, name="teacher_reg"),
    path("admin_viewteacher", views.admin_viewteacher, name="admin_viewteacher"),
    path("del_teacher/<int:id>", views.del_teacher, name="del_teacher"),
    path("admin_deptwisecount", views.admin_deptwisecount, name="admin_deptwisecount"),
    path("admin_student", views.admin_student, name="admin_student"),
    path("admin_viewstud", views.admin_viewstud, name="admin_viewstud"),
    path("del_stud/<int:id>", views.del_stud, name="del_stud"),
    path("stud_accept", views.stud_accept, name="stud_accept"),
    path("confirm_stud/<int:id>", views.confirm_stud, name="confirm_stud"),

    # student module...
    path("stud_home", views.stud_home, name="stud_home"),
    path("stud_detail", views.stud_detail, name="stud_detail"),
    path("stud_edit/<int:id>", views.stud_edit, name="stud_edit"),
    path("stud_update/<int:id>", views.stud_update, name="stud_update"),
    path("stud_teacher_view", views.stud_teacher_view, name="stud_teacher_view"),

    # Teacher module...
    path("teacher_home", views.teacher_home, name="teacher_home"),
    path("teacher_detail", views.teacher_detail, name="teacher_detail"),
    path("teacher_edit/<int:id>", views.teacher_edit, name="teacher_edit"),
    path("teacher_update/<int:id>", views.teacher_update, name="teacher_update"),
    path("teacher_stud_view", views.teacher_stud_view, name="teacher_stud_view"),
]
