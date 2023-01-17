from django.urls import path

from ..swagger.views import schema_view

urlpatterns = [
    path('swagger/', schema_view),
]
