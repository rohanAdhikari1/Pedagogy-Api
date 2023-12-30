from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import StudentSerializer,NotificationSerializer,TutorStdSerializer,TutorAdmSerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from rest_framework.authentication import TokenAuthentication
from .models import Notifications,Tutor
from firebase_admin.messaging import Message,Notification
from .permissions import IsActive
from fcm_django.models import FCMDevice
       

###Views for student

class student(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsActive]
    def get(self,request):
        try:
            return Response({
            'status':False,
            'message':'Something went wrong!'
            })
        except Exception as e:
            print(e)
            return Response({
                'status':False,
                'message':'Something went wrong!'
            })
    def post(self,request):
        try:
            data = request.data
            serializer = StudentSerializer(data=data)
            if serializer.is_valid():
                return Response({
                'status':True,
                'data':serializer.data
                })
            return Response({
                'status':False,
                'message':'invalid data',
                'result':serializer.errors
                })
        except Exception as e:
            print(e)
            return Response({
            'status':False,
            'message':'Something went wrong!'
            })





##########################################################
        





##########################################################
        

###Views for notifications

class notification(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsActive]
    def get(self,request):
        try:
            notifobj = Notifications.objects.filter(Q(group=request.user.role) | Q(group='all'))[:30] 
            serializer = NotificationSerializer(notifobj,many=True)
            return Response({
                'status':True,
                'result':serializer.data
                })
        except Exception as e:
            print(e)
            return Response({
            'status':False,
            'message':'Something went wrong!'
            })
        
    def post(self,request):
        try:
            data = request.data
            serializer = NotificationSerializer(data=data)
            if serializer.is_valid():
                devices = FCMDevice.objects.all()
                devices.send_message(Message(notification=Notification(title=data.get('title'), body=data.get('content'))))
                serializer.save()
                return Response({
                'status':True,
                'data':{
                    'uid': serializer.data.get('uid')
                }
                })
            return Response({
                'status':False,
                'message':'invalid data',
                'result':serializer.errors
                })
        except Exception as e:
            print(e)
            return Response({
            'status':False,
            'message':'Something went wrong!'
            })
        


##########################################################
        





##########################################################
        

###Views for Tutor
class tutor(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsActive]
    def get(self,request):
        try:
            notifobj = Tutor.objects.all()[:30] 
            if(request.user.role == "admin"):
                serializer = TutorAdmSerializer(notifobj,many=True)
            else:
                serializer = TutorStdSerializer(notifobj,many=True)
            return Response({
                'status':True,
                'result':serializer.data
                })
        except Exception as e:
            print(e)
            return Response({
            'status':False,
            'message':'Something went wrong!'
            })
        
    def post(self,request):
        try:
            data = request.data
            serializer = NotificationSerializer(data=data)
            if serializer.is_valid():
                return Response({
                'status':True,
                'data':{
                    'uid': serializer.data.get('uid')
                }
                })
            return Response({
                'status':False,
                'message':'invalid data',
                'result':serializer.errors
                })
        except Exception as e:
            print(e)
            return Response({
            'status':False,
            'message':'Something went wrong!'
            })