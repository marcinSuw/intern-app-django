from django.contrib.auth.models import User

from rest_framework import generics, views, status
from rest_framework.response import Response

from .serializers import RegisterSerializer
# Create your views here.


class RegisterUserView(views.APIView):

    permission_classes = []

    def post(self, request):
        s = RegisterSerializer(data=request.data)
        if s.is_valid():
            t = s.save()
            return Response(data=t, status=status.HTTP_201_CREATED)
        return Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(views.APIView):

    def get(self, request):
        data = {
            "username": request.user.username,
            "email": request.user.email
        }
        return Response(data=data, status=status.HTTP_200_OK)


class UsersListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
