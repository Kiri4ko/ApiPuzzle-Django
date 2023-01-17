from rest_framework import routers

from .views import ProjectView

router = routers.SimpleRouter()
router.register(r'projects/', ProjectView, basename='Project')

urlpatterns = [
                  # path('projects/', ),  # Start Project

              ] + router.urls
