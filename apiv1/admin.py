from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student,BaseUser,Notifications,Tutor
from django.utils import timezone
from firebase_admin.messaging import Message,Notification
from fcm_django.models import FCMDevice

class StudentAdmin(admin.ModelAdmin):
    list_display=('name','uid','parent_name','phone','school','class_name','board','address','landmark','profile_image','is_active','created_at','updated_at')
    search_fields=('name','parent_name')
    list_filter=('class_name','board','school')
    fields = ['name','password', 'parent_name','phone','school','class_name','board','address','landmark','profile','is_active']

    def reset_password_action(self, request, queryset):
        for user in queryset:
            user.set_password("Pedagogystudents")
            user.save()
            self.message_user(request, f'Password reset for {queryset.count()} user(s).')
            
    def save_model(self, request, obj, form, change):
        raw_password = form.cleaned_data['password']
        user = Student(phone=obj.phone)
        user.set_password(raw_password)
        obj.password = user.password
        super().save_model(request, obj, form, change)


    reset_password_action.short_description = 'Reset password for selected users'
    actions = [reset_password_action] + list(UserAdmin.actions)


class Users(admin.ModelAdmin):
    list_display=('name','phone','role')

class NotificationAdmin(admin.ModelAdmin):
    list_display=('uid','title','content','group','created_at','updated_at')
    def save_model(self, request, obj, form, change):
        devices = FCMDevice.objects.all()
        devices.send_message(Message(notification=Notification(title=obj.title, body=obj.content)))
        super().save_model(request, obj, form, change)

admin.site.register(Student,StudentAdmin)
# admin.site.register(BaseUser,Users)
admin.site.register(Notifications,NotificationAdmin)
admin.site.register(Tutor)