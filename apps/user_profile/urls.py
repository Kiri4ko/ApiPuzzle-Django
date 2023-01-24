from os import path

from rest_framework import routers

from .user_company.views import HeadCompanyView

router = routers.SimpleRouter()
router.register(r'user-company', HeadCompanyView)

urlpatterns = router.urls
