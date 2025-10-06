from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

@api_view(["GET"])
@permission_classes([AllowAny])
def public_api(request):
    return Response({"message": "This is a public endpoint, no token required."})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def protected_api(request):
    user = request.user.username
    return Response({"message": f"Hello {user}, you accessed a protected API!"})


