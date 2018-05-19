from django.conf.urls import include, url
from django.contrib import admin
from sio.views import home, create_student, create_course, register_student,get_all_courses

urlpatterns = {
    url(r'^admin/', admin.site.urls,name='admin'),
    url(r'^$', home),
    url(r'^home$', home),

    url(r'^create-student$', create_student),
    url(r'^create-course$', create_course),
    url(r'^register-student$', register_student),
    url(r'^get-all-courses$', get_all_courses),

}
