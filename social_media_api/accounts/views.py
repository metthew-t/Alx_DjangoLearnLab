from rest_framework import status, generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from .models import CustomUser
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer

# Registration
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        return Response({
            'token': serializer.validated_data['token'],
            'user': UserProfileSerializer(serializer.validated_data['user']).data
        })
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Profile
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    if request.method == 'GET':
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Follow User View (class-based)
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()
    lookup_url_kwarg = 'user_id'

    def post(self, request, user_id=None):
        target_user = self.get_object()
        if request.user == target_user:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(target_user)
    # Create notification
        Notification.objects.create(
        recipient=target_user,
        actor=request.user,
        verb='started following you'
    )
        return Response({"message": f"You are now following {target_user.username}."}, status=status.HTTP_200_OK)

# Unfollow User View (class-based)
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()
    lookup_url_kwarg = 'user_id'

    def post(self, request, user_id=None):
        target_user = self.get_object()
        if request.user == target_user:
            return Response(
                {"error": "You cannot unfollow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )
        request.user.following.remove(target_user)
        return Response(
            {"message": f"You have unfollowed {target_user.username}."},
            status=status.HTTP_200_OK
        )