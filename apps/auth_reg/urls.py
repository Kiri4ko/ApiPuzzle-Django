from django.urls import path, include

urlpatterns = [
    path('auth/', include('rest_framework.urls')),  # Login, logout - Password and Email
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),  # JWT-endpoints,for managing JWT tokens
    path('auth/', include('djoser.urls.authtoken')),  # Login, logout - Token
]
