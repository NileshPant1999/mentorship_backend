from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import (CategorySerializer,
                          CompanyDetailSerializer,
                          PostSerializer)
from .models import Category, CompanyDetails, Post
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny


class CompanyDetailsView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = CompanyDetailSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get("pk")
        return get_object_or_404(CompanyDetails, customer=item)


class CreateCompany(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = CompanyDetailSerializer(data=request.data)
        if serializer.is_valid():
            company = serializer.save()
            if company:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)

            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class PostList(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CategoryList(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
