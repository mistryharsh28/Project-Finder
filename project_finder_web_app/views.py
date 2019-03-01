from .models import Hackathon, HackathonTeam, HackathonTeamRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
    HackathonSerializer,
    HackathonDetailSerializer,
    HackathonTeamSerializer,
    HackathonTeamRequestSerializer
)
from rest_framework import status
from .permissions import IsTeacher, IsReadOnly, IsOwnerOrReadOnly
from django.http import HttpResponseRedirect
from .models import User
from rest_framework import viewsets
from rest_framework.serializers import ValidationError
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.contrib.auth import authenticate, login, logout
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from project_finder_web_app.serializers import UserCreateSerializer, UserLoginSerializer, UserDetailSerializer
from rest_framework.decorators import action


class UserDetailViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = authenticate(
                username=serializer.data.get("username"),
                password=serializer.data.get("password"),
            )
            if user:
                login(request, user)
# return HttpResponseRedirect(redirect_to="/menu_item/")
                return Response(serializer.data, status=HTTP_200_OK)
            else:
                raise ValidationError("Wrong Login Credentials")
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserLogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return HttpResponseRedirect("/api/login/")


class HackathonList(ListAPIView):
    serializer_class = HackathonSerializer
    queryset = Hackathon.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class HackathonCreate(ListCreateAPIView):
    serializer_class = HackathonSerializer
    queryset = Hackathon.objects.all()
    permission_classes = (IsTeacher | IsReadOnly,)


# Here the permissions are not working
class HackathonDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = HackathonDetailSerializer
    queryset = Hackathon.objects.all()
    permissions_classes = (IsOwnerOrReadOnly,)


class HackathonTeamList(ListAPIView):
    serializer_class = HackathonTeamSerializer
    queryset = HackathonTeam.objects.all()
    permissions_classes = (IsAuthenticatedOrReadOnly,)


class HackathonTeamCreate(ListCreateAPIView):
    serializer_class = HackathonTeamSerializer
    queryset = HackathonTeam.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class HackathonTeamDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = HackathonTeamSerializer
    queryset = HackathonTeam.objects.all()
    permissions_classes = (IsAuthenticatedOrReadOnly,)


class HackathonTeamRequestList(ListAPIView):
    serializer_class = HackathonTeamRequestSerializer
    queryset = HackathonTeamRequest.objects.all()
    permissions_classes = (IsAuthenticated,)


class HackathonTeamRequestCreate(ListCreateAPIView):
    serializer_class = HackathonTeamRequestSerializer
    queryset = HackathonTeamRequest.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class HackathonTeamRequestViewSet(viewsets.ModelViewSet):
    serializer_class = HackathonTeamRequestSerializer
    queryset = HackathonTeamRequest.objects.all()

    @action(detail=True, methods=["put", "get"])
    def accept(self, request, pk=None):
        hackathon_team_request = self.get_object()
        hackathon_team_request.accept()
        return Response({"message": "Request accepted"})

    @action(detail=True, methods=["put", "get"])
    def reject(self, request, pk=None):
        hackathon_team_request = self.get_object()
        hackathon_team_request.reject()
        return Response({"message": "Request rejected"})
