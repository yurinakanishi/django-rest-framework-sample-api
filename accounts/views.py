from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import status


User = get_user_model()


class Registration(APIView):
    permission_classes = (AllowAny,)  #

    def post(self, request):
        try:
            data = request.data
            name = data["name"]
            email = data["email"].lower()
            password = data["password"]

            if not User.objects.filter(email=email).exists():
                User.objects.create_user(name=name, email=email, password=password)
                return Response(
                    {"success": "User created successfully"},
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST
                )

        except Exception as e:
            return Response(
                {"error": f"Something went wrong: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class UserInfo(APIView):
    def get(self, request):
        try:
            users = request.user
            user = UserSerializer(users)
            return Response({"user": user.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": f"Something went wrong: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
