from apps.auth_reg.validators import validate_password
from rest_framework import serializers
from .models import User


# Create class UserRegistrSerialize
class UserRegistrSerializer(serializers.ModelSerializer):
    # Password repeat field
    password_rep = serializers.CharField(
        max_length=128, write_only=True,
    )
    password = serializers.CharField(
        max_length=128, write_only=True,
    )

    class Meta:
        model = User
        fields = [
            'full_name', 'nickname',
            'email', 'phone',
            'user_status',
            'password', 'password_rep',
        ]

    # Saving a new user
    def save(self, *args, **kwargs):
        user = User(
            full_name=self.validated_data['full_name'],  # Name and Surname
            nickname=self.validated_data['nickname'],  # Nickname
            email=self.validated_data['email'],  # Email
            phone=self.validated_data['phone'],  # Phone
            user_status=self.validated_data['user_status'],  # User status
        )

        # Password check
        password = self.validated_data['password']
        # Password check again
        password_rep = self.validated_data['password_rep']
        # Checking if passwords match
        if password != password_rep:
            raise serializers.ValidationError({password: "Password doesn't match!"})

        # Django default password validation
        validate_password(password=password_rep)

        # Save the password
        user.set_password(password)
        # Save the user
        user.save()
        return user
