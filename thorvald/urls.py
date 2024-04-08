from django.contrib import admin
from django.urls import path
from .views import FighterViewSet
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"fighters", FighterViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/enemies/", views.get_enemies, name="get_enemies"),
    path("api/thorvald/", views.get_thorvald, name="get_thorvald"),
]
