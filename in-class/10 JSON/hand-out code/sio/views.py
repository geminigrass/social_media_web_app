from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.db import transaction

from sio.models import *
from sio.forms import *

def home(request):
    context = {'courses':Course.objects.all(),
               'messages':[],
               'create_student_form':create_student_form(),
               'create_course_form':CreateCourseForm(),
               'register_student_form':RegisterStudentForm()
               }
    return render(request, 'sio.html', context)


# Createaget_all_coursesactiontousethetemplatetogeneratea JSON response for all courses.
def get_all_courses(request):
    # manual way:
    # context = {}
    # courses = Course.objects.all()
    # context['courses'] = courses
    # print("----------------------------")
    # print(Course.objects.get(course_number=15214).students.all())
    # return render(request, 'courses.json', context, content_type='application/json')

    # with django serialization:
    print("---------------------")
    print(Course.objects.all())
    data = serializers.serialize("json",Course.objects.all())
    return HttpResponse(data, content_type="application/json")


@transaction.atomic
def create_student(request):
    messages = []
    context = {'courses':Course.objects.all(),
               'messages':[],
               'create_student_form':create_student_form(),
               'create_course_form':CreateCourseForm(),
               'register_student_form':RegisterStudentForm()
               }

    if request.method == 'GET':
        return render(request, 'sio.html', context)

    form = create_student_form(request.POST)
    context['create_student_form'] = form

    if not form.is_valid():
        return render(request, 'sio.html', context)

    form.save()

    messages.append("Success!")
    return render(request, 'sio.html', context)

@transaction.atomic
def create_course(request):
    messages = []
    context = {'courses':Course.objects.all(),
               'messages':[],
               'create_student_form':create_student_form(),
               'create_course_form':CreateCourseForm(),
               'register_student_form':RegisterStudentForm()
               }

    if request.method == 'GET':
        return render(request, 'sio.html', context)

    form = CreateCourseForm(request.POST)
    context['create_course_form'] = form

    if not form.is_valid():
        return render(request, 'sio.html', context)

    form.save()

    messages.append("Success!")
    return render(request, 'sio.html', context)


@transaction.atomic
def register_student(request):
    messages = []
    context = {'courses':Course.objects.all(),
               'messages':[],
               'create_student_form':create_student_form(),
               'create_course_form':CreateCourseForm(),
               'register_student_form':RegisterStudentForm()
               }

    if request.method == 'GET':
        return render(request, 'sio.html', context)

    form =RegisterStudentForm(request.POST)
    context['register_student_form'] = form

    if not form.is_valid():
        return render(request, 'sio.html', context)

    form.save()
    context['courses']=Course.objects.all()
    messages.append("Success!")
    return render(request, 'sio.html', context)
