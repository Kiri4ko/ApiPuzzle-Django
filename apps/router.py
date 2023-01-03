from django.urls import path, include

urlpatterns = [
    path('', include('apps.auth_reg.urls')),
    path('', include('apps.swagger.urls')),
]
