from rest_framework.routers import SimpleRouter
from . import viewsets


router = SimpleRouter()
router.register('', viewsets.book_viewSet, basename='book')

urlpatterns = router.urls
