from rest_framework import serializers
from .models import CustomUser  # Assuming your user model is named CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'full_name', 'date_of_birth')  # Add other fields as needed

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            full_name=validated_data.get('full_name', ''),
            date_of_birth=validated_data.get('date_of_birth', None),
            # Add other fields as needed
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})
