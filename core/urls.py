from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'core'

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'schools', views.SchoolViewSet)
router.register(r'classes', views.SchoolClassViewSet)
router.register(r'students', views.StudentViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
]
