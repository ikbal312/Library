from django.urls import path, include

urlpatterns = [
    path('services/', include('service.urls')),
    path('user/', include('user.urls')),
    path('book/', include('book.urls')),
    path('', include('rest_framework.urls'))
]
