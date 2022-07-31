from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status, filters
from rest_auth.models import TokenModel
from django.contrib.auth import authenticate
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.core.mail import EmailMessage
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from school.models import Student, Teacher
from school.serializers import TeacherRegisterSerializer, TeacherLoginSerializer, StudentSerializer, \
    SendEmailsSerializer, SearchStudentSerializer


class TeacherRegisterView(CreateAPIView):
    serializer_class = TeacherRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response('success', status=status.HTTP_201_CREATED)


class TeacherLoginView(CreateAPIView):
    serializer_class = TeacherLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.data.get('phone')
        password = serializer.data.get('password')
        teacher = authenticate(request, phone=phone, password=password)
        if teacher:
            token = TokenModel.objects.get(user=teacher)
            return Response({'key': token.key}, status=status.HTTP_201_CREATED)
        return Response('invalid login', status=status.HTTP_401_UNAUTHORIZED)


class StudentView(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = 'pk'
    permission_classes = (IsAuthenticatedOrReadOnly, )


class SendEmailsView(CreateAPIView):
    serializer_class = SendEmailsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def create(self, request, *args, **kwargs):
        teacher_id = request.user.id
        teacher_classgrade = Teacher.objects.get(id=teacher_id).classgrade
        students = Student.objects.filter(classgrade=teacher_classgrade)
        email_list = [i.mail_address for i in students]
        message = request.data.get('message')
        email = EmailMessage('Сообщение от Учителя', message, to=email_list)
        email.send()
        return Response('Ваше сообщение было отправлено вашим студентам!')


class SearchStudentView(ListCreateAPIView):
    search_fields = ['full_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Student.objects.all()
    serializer_class = SearchStudentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

