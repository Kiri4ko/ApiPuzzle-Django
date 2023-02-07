from rest_framework import routers

from .views import ProjectView

router = routers.SimpleRouter()
router.register(r'', ProjectView)
urlpatterns = router.urls
