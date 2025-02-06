from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'brands', views.BrandViewSet, basename='brand')
router.register(r'products', views.ProductViewSet, basename='product')
router.register(r'manuals', views.UserManualViewSet, basename='manual')

urlpatterns = [
    path('', include(router.urls)),
    path('profile/', views.CompanyProfileView.as_view(), name='company-profile'),
    path('register/', views.UserRegistrationView.as_view(), name='user-register'),
]
