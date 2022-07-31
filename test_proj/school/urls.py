from django.urls import path

from school.views import TeacherRegisterView, TeacherLoginView, StudentView, SendEmailsView, SearchStudentView


urlpatterns = [
    path('register/', TeacherRegisterView.as_view()),
    path('login/', TeacherLoginView.as_view()),
    path('student/', StudentView.as_view({'post': 'create', 'get': 'list'})),
    path('student/<int:pk>', StudentView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('sendmails/', SendEmailsView.as_view()),
    path('searchstudents/', SearchStudentView.as_view())
]

