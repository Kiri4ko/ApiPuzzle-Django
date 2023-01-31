from rest_framework import routers

from .user_company.views import HeadCompanyView, POCompanyView

router = routers.SimpleRouter()
router.register(r'head-company', HeadCompanyView)
router.register(r'po-company', POCompanyView)
urlpatterns = router.urls
