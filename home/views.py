from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BlogSerializer
from rest_framework import status 
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Blog



class BlogView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        try:
            post = Blog.objects.filter(user=request.user)
            serializer_ = BlogSerializer(post, many=True)
            return Response(
                {
                    "data" : serializer_.data,
                    "message" : "Blogs fetched Successfully"
                }
            )
        except Exception as e:
            print(e)
            return Response({
                "data" : {serializer_.errors},
                "message" : "Something went wrong"  
            })
    
    def post(self, request):
        try:
            data = request.data
            serializer_ = BlogSerializer(data=data)
            data['user'] = request.user.id
            if not serializer_.is_valid():
                return Response({
                    'data' : serializer_.errors,
                    'message' : "something went wrong"
                }, status= status.HTTP_400_BAD_REQUEST
                )
            serializer_.save()
            return Response({
                "data" : serializer_.data,
                "message" : "your Post is created"
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            print(e)
            return Response({
                "data" : {},
                "message" : "Something went wrong"  
            })


    def patch(self, request):
        try:
            data = request.data
            blog = Blog.objects.filter(uid = data.get('uid'))
            if not blog.exists():
                return Response({
                    "data" : {},
                    "message" : "invalid blog id"
                }, status=status.HTTP_400_BAD_REQUEST)

            if request.user != blog[0].user:
                return Response({
                    "data" : {},
                    "message" : "You are not autherized"
                }, status=status.HTTP_400_BAD_REQUEST)

            serializer_ = BlogSerializer(blog[0], data=data, partial=True)
            if not serializer_.is_valid():
                return Response({
                    "data" : {},
                    "message" : "You are not autherized"
                }, status=status.HTTP_400_BAD_REQUEST)
            serializer_.save()
            return Response({
                    "data" : serializer_.data,
                    "message" : "Blog updated"
                }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                    "data" : {},
                    "message" : "some operation is wrong"
                }, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        try:
            data = request.data
            blog = Blog.objects.filter(uid = data.get('uid'))
            if not blog.exists():
                return Response({
                    "data" : {},
                    "message" : "invalid blog id"
                }, status=status.HTTP_400_BAD_REQUEST)
            
            if request.user != blog[0].user:
                return Response({
                    "data" : {},
                    "message" : "You are not autherized to delete this post"
                }, status=status.HTTP_400_BAD_REQUEST)
            blog[0].delete()
            return Response({
                    "data" : {},
                    "message" : "You post is delete"
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                    "data" : {},
                    "message" : "some operation is wrong"
                }, status=status.HTTP_400_BAD_REQUEST)


