from django.shortcuts import get_object_or_404
from .models import Founder, Progress
from .serializers import FounderSerializer, ProgressSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class FounderDetails(generics.RetrieveAPIView):

    serializer_class = FounderSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get("pk")
        return get_object_or_404(Founder, user_id=item)


class ProgressList(generics.ListAPIView):

    permission_classes = [permissions.AllowAny]
    serializer_class = ProgressSerializer

    def get_queryset(self):
        user = self.request.user
        return Progress.objects.filter(founder_id=user).order_by("-start_date")


class ProgressDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProgressSerializer
    queryset = Progress.objects.all()

    lookup_field = "slug"


class CreateProgress(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format="json"):
        serializer = ProgressSerializer(data=request.data)
        if serializer.is_valid():
            progress = serializer.save()
            if progress:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class EditProgress(generics.UpdateAPIView):
    serializer_class = ProgressSerializer
    queryset = Progress.objects.all()


class CreateFounder(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = FounderSerializer(data=request.data)

        if serializer.is_valid():
            founder = serializer.save()
            if founder:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditFounder(generics.UpdateAPIView):
    serializer_class = FounderSerializer
    queryset = Founder.objects.all()
    lookup_field = "user"
