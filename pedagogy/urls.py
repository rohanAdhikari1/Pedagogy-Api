from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

#django header customization
admin.site.site_header = "Pedagogy Super Admin Panel"
admin.site.site_title = "Welcome to Super Admin Panel"
admin.site.index_title = "Welcome to Admin Portal"

urlpatterns = [
    path('api/v1/',include('apiv1.urls')),
    path('proadmin/rohan', admin.site.urls),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
