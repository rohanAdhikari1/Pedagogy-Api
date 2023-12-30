from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate
from fcm_django.models import FCMDevice

class StudentLogin(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        data = request.data
        errors =[]

        if 'phone' not in data:
            errors.append({'phone':'Phone number is required.'})

        if 'password' not in data:
            errors.append({'password':'Password is required.'})
        
        if len(errors) >0:
            return Response({
            'status': 403,
            'errors': errors,
            'message': 'Something went wrong!'
            }, status=403)
        
        user = authenticate(phone=data.get('phone'), password=data.get('password'))
        fcmtoken = data.get('token') if data.get('token') else ""
        if user:
            if user.role =="student":
                if user.is_active:
                    token, created = Token.objects.get_or_create(user=user)
                    try:
                        device,created = FCMDevice.objects.update_or_create(
                            name=user.name,
                            registration_id=fcmtoken,
                            active=True,
                            type="android"
                        )
                        return Response({
                        'status':True,
                        'token':token.key
                        })
                    except Exception as e:
                        print(e)
                        return Response({
                            'status':False,
                            'message': 'Something went wrong. Server operation Failed!'
                            })
                else:
                    return Response({
                        'status':False,
                        'message': 'User is not active. please contact administration.'
                        })
            else:
                return Response({
                'status':False,
                'message': 'Invalid credentials'
                })
                        
        else:
            return Response({
                'status':False,
                'message': 'Invalid credentials'})