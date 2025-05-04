from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import ProfileNotFound, NotYourProfile
from .models import Profile
from .serializers import ProfileSerializer, UpdateProfileSerializers
from .renderes import ProfileJSONRenderer

class AgentListAPIView(generics.ListAPIView):
    """
    List all agents
    """
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset= Profile.objects.filter(is_agent=True)

class TopAgentsListAPIView(generics.ListAPIView):
    """
    List all top agents
    """
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset= Profile.objects.filter(top_agent=True)
    
class GetProfileAPIView(APIView):
    """
    Get a profile by username
    """
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJSONRenderer]
    
    def get(self, request, username):
        user =self.request.user
        user_profile=Profile.objects.get(user=user)
        serializer=ProfileSerializer(user_profile, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateProfileAPIView(APIView):
    """
    Update a profile by username
    """
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJSONRenderer]
    
    def patch(self, request, username):
        try:
            Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            raise ProfileNotFound
        
        user_name=request.user.username
        if user_name != username:
            raise NotYourProfile
        
        data=request.data
        serializer=UpdateProfileSerializers(instance=request.user.profile, data=data, partial=True)
        
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)