from django.urls import path
from .views import student,notification,tutor
from .auth import StudentLogin
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet

urlpatterns = [
    path('student/login', StudentLogin.as_view(),name="Student Login"),
    path('', student.as_view(),name="Student"),
    path('notifications',notification.as_view(),name="Notifications"),
    path('tutor',tutor.as_view(),name="Tutor"),
    #  path('admin/devices', FCMDeviceAuthorizedViewSet.as_view({'post': 'create'}), name='create_fcm_device'),
]