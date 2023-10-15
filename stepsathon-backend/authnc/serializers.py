from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from authnc.models import CustomUser
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate


class MiniUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('uuid', 'email', 'username', 'profile_picture','first_name', 'last_name', 'imei_number')


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(request=self.context.get('request'), email=email, password=password)

        if not user:
            data = {'detail': 'Incorrect credentials.'}
            return data

        data['user'] = user
        return data
    

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    # password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = CustomUser
        fields = ('uuid', 'email','profile_picture', 'password','first_name', 'last_name', 'imei_number')
    
    
    def create(self, validated_data):

        user = CustomUser.objects.create(
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'], 
        )
        user.set_password(validated_data['password'])
        user.save()
        return MiniUserSerializer(user)
    
    """Assuming the password validation is done in the frontend."""

    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError({"password": "Password fields didn't match."})
    #     return attrs
    
    

