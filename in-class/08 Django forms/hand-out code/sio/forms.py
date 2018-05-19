from django import forms
from sio.models import Student,Course




class create_student_form(forms.Form):
    andrew_id = forms.CharField(required=True,label='andrew id')
    first_name = forms.CharField(required=True,label='first name')
    last_name = forms.CharField(required=True, label='last name')


    # def clean(self):
    #     cleaned_data = super(create_student_form, self).clean()
    #     return cleaned_data
    #
    #
    # def clean_andrew_id(self):
    #     andrew_id = self.cleaned_data.get('andrew_id')
    #     if Student.objects.get(andrew_id__exact=andrew_id):
    #         raise forms.ValidationError("AndrewID already exists.")
    #     return andrew_id

class create_class_form(forms.Form):
    course_number = forms.CharField(max_length=20)
    course_name = forms.CharField(max_length=255)
    instructor = forms.CharField(max_length=255)




