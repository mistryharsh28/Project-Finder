from .models import Hackathon, HackathonTeam, HackathonTeamRequest, Skill, User
from rest_framework import serializers
from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
)


class UserDetailSerializer(ModelSerializer):
    # password = serializers.CharField(style={"input_type": "password"})

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'sap_id',
            'mobile',
            'photo',
            'is_mentor',
            'is_teacher',
            'bio',
            'year',
            'skills',
            'interests',
            'Github',
            'LinkedIN',
            'Behance',
            'StackOverFlow',


            # 'first_name',
            # 'last_name',
        ]


class UserCreateSerializer(ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"})

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'sap_id',
            'mobile',
            'photo',
            'is_mentor',
            'is_teacher',
            'bio',
            'year',
            'skills',
            'interests',
            'Github',
            'LinkedIN',
            'Behance',
            'StackOverFlow',

            # 'first_name',
            # 'last_name',
        ]

        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):

        sap_id = data['sap_id']
        user_qs = User.objects.filter(sap_id=sap_id)
        if user_qs.exists():
            raise ValidationError("This sap_id already registered.")
        return data

    def create(self, validated_data):
        password = validated_data['password']
        user_obj = User(
            username=validated_data["username"],
            sap_id=validated_data["sap_id"],
            mobile=validated_data["mobile"],
            email=validated_data["email"],
            bio=validated_data["bio"],
            photo=validated_data["photo"],
            is_mentor=validated_data["is_mentor"],
            is_teacher=validated_data["is_teacher"],
            year=validated_data["year"],
            skills=validated_data["skills"],
            interests=validated_data["interests"],
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(serializers.ModelSerializer):
    username = CharField()
    password = serializers.CharField(style={"input_type": "password"})

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
        extra_kwargs = {"password": {"write_only": True}}


class HackathonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hackathon
        fields = [
            'id',
            'name',
            'creator',
            'hackathon_desc',
            'link',
            'hackathon_date',
        ]


class HackathonDetailSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.email')

    class Meta:
        model = Hackathon
        fields = [
            'id',
            'name',
            'creator',
            'hackathon_desc',
            'link',
            'hackathon_date',
        ]


class HackathonTeamSerializer(serializers.ModelSerializer):
    # hackathon = serializers.ReadOnlyField(source='hackathon.name')

    class Meta:
        model = HackathonTeam
        fields = [
            'name',
            'leader',
            'current_members',
            'hackathon',
            'vacancies',
            'closed',
            'cut_off_date',
            'skills_required',
        ]


class HackathonTeamRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = HackathonTeamRequest
        fields = [
            'id',
            'sender',
            'team',
            'message',
            'skills',
            'create_date',
            'status',
        ]
