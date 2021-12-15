from rest_framework.response import Response
from user_app.api.serializers import UserRegistrationSerializer, UserSerializer
from rest_framework import generics

class user_registration_view(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })
    
# from user_app.api.serializers import UserRegistrationSerializer
# from rest_framework.response import Response 
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.decorators import api_view

# @api_view(['POST',])
# def user_registration_view(request):

#     if request.method == 'POST':
#         serializer = UserRegistrationSerializer(data=request.data)

#         data = {}

#         if serializer.is_valid():
#             account = serializer.save()

#             data['response'] = 'Registration successful'
#             data['username'] = account.username
#             data['email'] = account.email
#             data['fullname'] = account.fullname
#             data['phone'] = account.phone
            
#             refresh = RefreshToken.for_user(account)
#             data['token'] = {
#                 'refresh': str(refresh),
#                 'access':str(refresh.access_token),
#             }

#         else:
#             data = serializer.errors
        
        
#         return Response(data)
