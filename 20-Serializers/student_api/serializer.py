from dataclasses import fields
from rest_framework import serializers
from django.utils.timezone import now
from student_api.models import Student

# class StudentSerializer(serializers.Serializer) :
#     first_name = serializers.CharField(max_length=50)
#     last_name = serializers.CharField(max_length=50)
#     number = serializers.IntegerField()
#     # id = serializers.IntegerField()

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.email)
#         instance.last_name = validated_data.get('last_name', instance.content)
#         instance.number = validated_data.get('number', instance.created)
#         instance.save()
#         return instance


class StudentSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()
    class Meta:
        model = Student
        # fields = ['id', 'first_name', 'last_name', 'number', 'days_since_joined']
        fields = '__all__'
        # exclude = ['id']

    def validate_first_name(self, value):
        if value.lower() == 'rafe':
            raise serializers.ValidationError("this name cant be our student")
        return value

    def get_days_since_joined(self, obj):
        return (now() - obj.regiser_date).days