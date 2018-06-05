from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from products import views as product_views


router = routers.DefaultRouter()
router.register(r'products', product_views.ProductViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'api-auth/', include('rest_framework.urls')),
    path(r'', include(router.urls))
]
