from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()

router.register(r'prediction', views.ImageViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls))
]