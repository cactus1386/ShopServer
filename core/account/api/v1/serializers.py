from rest_framework import serializers
from ...models import User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions

class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = User
        fields = ("email", "password", 'password1')

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("password1"):
            raise serializers.ValidationError({"detail": "password does not match"})
        
        try:
            validate_password(attrs.get('password'))

        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'password': list(e.messages)})

        return super().validate(attrs)

    def create(self, validated_data):
        return super().create(validated_data)
    
