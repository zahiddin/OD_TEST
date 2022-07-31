from rest_auth.models import TokenModel
from rest_framework import serializers

from school.models import Teacher, Student
from departments.models import ClassGrade


class ClassGradeSeriazlier(serializers.ModelSerializer):
    class Meta:
        model = ClassGrade
        fields = ('id', 'title',)


class TeacherRegisterSerializer(serializers.ModelSerializer):
    classgrade = ClassGradeSeriazlier

    class Meta:
        model = Teacher
        fields = ('username', 'phone', 'password', 'subject', 'classgrade')

    def create(self, validated_data):
        teacher = Teacher.objects.create(
            username=validated_data.get('username'),
            phone=validated_data.get('phone'),
            subject=validated_data.get('subject'),
            classgrade=validated_data.get('classgrade'))
        teacher.set_password(validated_data.get('password'))
        teacher.save()
        TokenModel.objects.create(user=teacher)
        return teacher


class TeacherLoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField()


class StudentSerializer(serializers.ModelSerializer):
    classgrade = ClassGradeSeriazlier

    class Meta:
        model = Student
        fields = ('full_name', 'mail_address', 'birthdate', 'classgrade', 'address', 'gender', 'photo')


class SendEmailsSerializer(serializers.Serializer):
    message = serializers.CharField()


class SearchStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

