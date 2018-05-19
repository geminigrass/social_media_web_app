from django import forms
from sio.models import Student,Course




# class create_student_form(forms.Form):
#     andrew_id = forms.CharField(required=True,label='andrew id')
#     first_name = forms.CharField(required=True,label='first name')
#     last_name = forms.CharField(required=True, label='last name')


    # def is_valid(self):
    #
    #
    #     print( Student.objects.filter(andrew_id=self.andrew_id).count() )
    #     if Student.objects.filter(andrew_id=self.andrew_id).count() > 0:
    #         # raise forms.ValidationError("A student with Andrew ID %s already exists." %
    #         #           request.POST['andrew_id'])
    #         raise forms.ValidationError("A student with same Andrew ID is already exists")
    #     else:
    #         return True


class create_student_form(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('andrew_id','first_name','last_name')

class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_number', 'course_name', 'instructor']


class RegisterStudentForm(forms.Form):
    andrew_id = forms.CharField(label='Andrew ID', max_length=20)
    course_number = forms.CharField(max_length=20)
    def clean(self):
        cleaned_data = super(RegisterStudentForm, self).clean()
        andrew_id = cleaned_data.get('andrew_id')
        course_number = cleaned_data.get('course_number')
        if andrew_id and Student.objects.filter(andrew_id=andrew_id).count() == 0:
            raise forms.ValidationError("%s is not a student"%andrew_id)
        if course_number and Course.objects.filter(course_number=course_number).count() == 0:
            raise forms.ValidationError("%s is not a course"%course_number)
        return cleaned_data
    def save(self):
        student = Student.objects.get(andrew_id = self.cleaned_data.get('andrew_id'))
        course = Course.objects.get(course_number = self.cleaned_data.get('course_number'))
        course.students.add(student)
        course.save()

        return course