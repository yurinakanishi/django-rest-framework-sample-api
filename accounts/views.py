from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token
from .serializers import RegistrationSerializer
from rest_framework.decorators import api_view, permission_classes

User = get_user_model()


@api_view(
    [
        "POST",
    ]
)
@permission_classes((AllowAny,))
def registration_view(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data["response"] = "Registration Successful!"
            data["name"] = account.name
            data["email"] = account.email
            token = Token.objects.get(user=account).key
            data["token"] = token
        else:
            data = serializer.errors

        return Response(data, status=status.HTTP_201_CREATED)


class Registration(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data["response"] = "User created successfully"
            data["email"] = account.email
            data["name"] = account.name
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(
            data,
            status=status.HTTP_201_CREATED,
        )


class UserInfo(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            try:
                user = UserSerializer(request.user)
                return Response(user.data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(
                    {"error": f"Something went wrong: {str(e)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        else:
            return Response(
                {"error": "You must be authenticated to access this endpoint."},
                status=status.HTTP_401_UNAUTHORIZED,
            )


class Logout(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            return Response(
                {"success": "User successfully logged out."},
                status=status.HTTP_205_RESET_CONTENT,
            )
        except Exception as e:
            return Response(
                {"error": f"Something went wrong: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
