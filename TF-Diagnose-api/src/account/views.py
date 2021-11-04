from django.contrib.auth import user_logged_in
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView,
    DestroyAPIView,
)
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth import get_user_model
from src.core.pagination import UserPagination

from src.account.serializers import (
    UserSerializer,
    UserCreateSerializer,
    EmptySerializer
)

User = get_user_model()


class CustomAuthToken(ObtainAuthToken, CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user_data = UserSerializer(instance=user).data
        user_logged_in.send(sender=user.__class__, request=request, user=user)
        return Response({
            'token': token.key,
            'user': user_data,
        })


class Logout(CreateAPIView):
    serializer_class = EmptySerializer

    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if request.user and getattr(request.user, 'id'):
            token = Token.objects.get(user=request.user)
            if token:
                token.delete()
        return Response(status=status.HTTP_200_OK)


class UserViewSet(ListCreateAPIView, DestroyAPIView, GenericViewSet):
    serializer_class = UserSerializer
    pagination_class = UserPagination
    filter_backends = (
        SearchFilter,
        OrderingFilter,
    )
    search_fields = (
        'first_name',
        'last_name',
        'email',
        'username',
    )
    ordering_fields = '__all__'
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update',):
            return UserCreateSerializer
        else:
            return UserSerializer

    def get_permissions(self):
        if self.action in ('create', 'update', 'partial_update',):
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAuthenticated()]