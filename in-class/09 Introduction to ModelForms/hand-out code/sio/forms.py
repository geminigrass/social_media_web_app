from django import forms
from sio.models import *

class CreateStudentForm(forms.ModelForm):
    andrew_id = forms.CharField(required=True, label='andrew id')
    first_name = forms.CharField(required=True,label='first name')
    last_name = forms.CharField(required=True, label='last name')

    class Meta:
        model = Student
        fields = ('andrew_id','first_name','last_name')

class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ('students',)

class RegisterStudentForm(forms.Form):
    andrew_id = forms.CharField(required=True, label='andrew id')
    course_number = forms.CharField(required=True, label='course number')



