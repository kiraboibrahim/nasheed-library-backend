from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.exceptions import ValidationError


User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50, write_only=True,
                                     validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, validators=[validate_password])

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise ValidationError("passwords must be the same")

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        user = User.objects.create_user(username, password)
        return user

    class Meta:
        model = User
        fields = ["username", "password", "password2"]
