from django.shortcuts import render
from rest_framework.generics import ListAPIView
from product.models import Category
from product.serializers import CategorySerializer


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        self.queryset = Category.objects.all()
        return self.queryset
    