from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from project_finder_web_app import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("hackathon_team_request_viewset", views.HackathonTeamRequestViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('login/', views.UserLoginAPIView.as_view(), name='login'),
    path('register/', csrf_exempt(views.UserCreateAPIView.as_view()), name='register'),
    path('detail/', views.UserDetailViewSet.as_view({'get': 'list'}), name='detail'),
    path('hackathon_list/', views.HackathonList.as_view(), name='hackathon_list'),
    path('hackathon_create/', views.HackathonCreate.as_view(), name='hackathon_create'),
    path('hackathon_detail/<int:pk>', views.HackathonDetail.as_view(), name='hackathon_detail'),
    path('hackathon_team_list/', views.HackathonTeamList.as_view(), name='hackathon_team_list'),
    path('hackathon_team_create/', views.HackathonTeamCreate.as_view(), name='hackahon_team_create'),
    path('hackathon_team_detail/<int:pk>', views.HackathonTeamDetail.as_view(), name='hackathon_team_detail'),
    path('hackathon_team_request_list/', views.HackathonTeamRequestList.as_view(), name='hackathon_team_request_list'),
    path(
        'hackathon_team_request_create/',
        views.HackathonTeamRequestCreate.as_view(),
        name='hackathon_team_request_create'
    ),
    path('logout/', views.UserLogoutAPIView.as_view(), name='logout'),
]
