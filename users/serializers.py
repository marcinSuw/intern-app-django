from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from rest_framework_jwt.serializers import JSONWebTokenSerializer, authenticate
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(min_length=8, write_only=True,)
    password2 = serializers.CharField(min_length=8, write_only=True,)

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Passwords should be the same.')
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["password"])
        if user:
            payload = jwt_payload_handler(user)
            return {
                'token': jwt_encode_handler(payload)
            }
        return user

    class Meta:
        fields = [
            'username',
            'email',
            'password',
        ]


class CustomJWTSerializer(JSONWebTokenSerializer):
    username_field = 'email'

    def validate(self, attrs):

        password = attrs.get("password")
        user_obj = User.objects.filter(
            email=attrs.get("email")).first()
        if user_obj is not None:
            credentials = {
                'username': user_obj.username,
                'password': password
            }
            if all(credentials.values()):
                user = authenticate(**credentials)
                if user:
                    if not user.is_active:
                        msg = 'User account is disabled.'
                        raise serializers.ValidationError(msg)
                    payload = jwt_payload_handler(user)
                    return {
                        'token': jwt_encode_handler(payload),
                        'user': user
                    }
                else:
                    msg = 'Unable to log in with provided credentials.'
                    raise serializers.ValidationError(msg)
            else:
                msg = 'Must include "{username_field}" and "password".'
                msg = msg.format(username_field=self.username_field)
                raise serializers.ValidationError(msg)
        else:
            msg = 'Account with this email/username does not exists'
            raise serializers.ValidationError(msg)
