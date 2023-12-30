from rest_framework import permissions

class IsActive(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_active
        # return hasattr(user, 'user_profile') and user.user_profile.role in ['student', 'teacher']





# for checking
# from .permissions import IsStudentOrTeacher

# class StudentView(generics.RetrieveUpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     permission_classes = [IsAuthenticated, IsStudentOrTeacher]

# class TeacherView(generics.RetrieveUpdateAPIView):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer
#     permission_classes = [IsAuthenticated, IsStudentOrTeacher]