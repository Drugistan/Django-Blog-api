from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .api.serializer import RegisterSerializer, LoginSerializer
from rest_framework import status 

# Create your views here.


class RegisterView(APIView):

    def post(self, request):
        try:
            serializer_ = RegisterSerializer(data=request.data)
            if not serializer_.is_valid():
                return Response({
                    'data' : serializer_.errors,
                    'message' : "something went wrong"
                }, status= status.HTTP_400_BAD_REQUEST
                )
            serializer_.save()
            return Response({
                "data" : {},
                "message" : "your account is created"
            }, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            print(e)
            return Response({
                'data' : {},
                'message' : "somwthing went wrong"
            }, status=status.HTTP_400_BAD_REQUEST)
        

class LoginView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer_ = LoginSerializer(data=data)
            if not serializer_.is_valid():
                return Response({
                    'data' : serializer_.errors,
                    'message' : "something went wrong"
                }, status= status.HTTP_400_BAD_REQUEST
                )
            response = serializer_.get_jwt_token(serializer_.data)
            return Response(response, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                'data' : {},
                'message' : "somwthing went wrong"
            }, status=status.HTTP_400_BAD_REQUEST)
