from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register("tables", views.BookingViewSet, "booking")

urlpatterns = [
    path("menu/", views.MenuListView.as_view(), name="menu_list"),
    path("menu/<int:pk>/", views.MenuSpecificView.as_view(), name="menu_specific"),
    path("booking/", include(router.urls)),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]
