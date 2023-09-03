# from .views import Notificatiorouter.register('reservation',views.ReservationViewSet,basename='reservation')nView, ReminderView, ReservationView, BorrowView
from .viewsets import WishlistViewSet
from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('wishlist', WishlistViewSet, basename='wishlist')
urlpatterns = [
    path('borrow/', views.borrow_view),
    path('notification/', views.notification_view),
    path('reservation/', views.reservation_view),
    path('reminder/', views.reminder_view),
]

urlpatterns += router.urls
