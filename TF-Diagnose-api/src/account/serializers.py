from rest_framework import serializers
from src.account.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'country',
            'email',
            'place',
            'household_contact',
            'is_active',
            'last_login',
            'date_joined'
        )


class UserMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'country',
            'place',
            'household_contact',
        )

    def create(self, validated_data):
        password = validated_data['password']
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class EmptySerializer(serializers.Serializer):
    pass

