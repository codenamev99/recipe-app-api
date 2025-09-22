"""
Views for the suer API.
"""
from rest_framework import generics

from user.serializers import UserSerializer


class CreateUserVIew(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer
