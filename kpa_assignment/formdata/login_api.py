from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    # The field is now named 'phone' to correctly match the frontend's payload.
    phone = serializers.CharField()
    password = serializers.CharField()

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            # These are the hardcoded credentials from the assignment
            phone = '7760873976'
            password = 'to_share@123'

            # Now we check against the 'phone' key from the serializer
            if serializer.validated_data['phone'] == phone and \
               serializer.validated_data['password'] == password:
                return Response({
                    "success": True,
                    "message": "Login successful",
                    "data": {
                        "token": "your_auth_token_here",
                        "userType": "admin"
                    }
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "success": False,
                    "message": "Invalid credentials"
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)