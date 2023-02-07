from django.urls import path, include

urlpatterns = [
    path('', include('apps.auth_reg.urls')),
    path('', include('apps.swagger.urls')),
    path('project/', include('apps.projects.urls')),
    path('user-profile/', include('apps.user_profile.urls')),
    path('project/', include('apps.projects.urls')),
]
