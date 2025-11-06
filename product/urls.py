from django.urls import path
from product.views import CategoryListAPIView

urlpatterns = [
    path('category/', CategoryListAPIView.as_view(), name='category')
]