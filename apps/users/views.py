# # Connect the status
# from rest_framework import status
# # Connect the response
# from rest_framework.response import Response
# # Connect data to create
# from rest_framework.generics import CreateAPIView
# # Connect access rights
# from rest_framework.permissions import IsAuthenticated
# # Connect the User model
# from .models import User
# # Connect the UserRegistrSerializer
# from .serializers import UserRegistrSerializer
#
# # Create class RegistrUserView
#
# class RegistrUserView(CreateAPIView):
#     queryset = User.objects.all()
#     # Add serializer UserRegistrSerializer
#     serializer_class = UserRegistrSerializer
#     # Add access rights
#     permission_classes = [IsAuthenticated]
#
#
#     # Creating a new user
#     def post(self, request, *args, **kwargs):
#         serializer = UserRegistrSerializer(data=request.data)
#         data = {}
#         # Data validation
#         if serializer.is_valid():
#             # Saving a new user
#             serializer.save()
#             data['response'] = True
#             # Response 200
#             return Response(data, status.HTTP_201_CREATED)
#         else:
#             data = serializer.errors
#             # Response error
#             return Response(data)
