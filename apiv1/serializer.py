from rest_framework import serializers
from .models import Student,Notifications,Tutor


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"


##########################################################
        





##########################################################
        

###aerializer for Notification
class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notifications
        fields = ("title",'content','created_at','updated_at')


##########################################################
        





##########################################################
        

###serializer for Tutor
class TutorStdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tutor
        fields = ("name",'high_degree_qual','avaiable_time','is_professional','profile','year_exp')

class TutorAdmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tutor
        fields = "__all__"