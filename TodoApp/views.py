from rest_framework import views , response, status
from rest_framework import generics
from . import serializer as user_serializer
from . import services
from . import models
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenViewBase
from django.shortcuts import get_object_or_404

class RegisterApi(views.APIView):
    def post(self, request):
        serializer = user_serializer.UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data=serializer.validated_data
        serializer.instance=services.create_user(user_dc=data)

        return response.Response(data=serializer.data)

class ChangePassword(generics.UpdateAPIView):
    serializer_class = user_serializer.ChangePasswordSerializer
    model = models.User
    permission_classes = (IsAuthenticated,)

    def get_object(self,queryset=None):
        obj = self.request.user
        return obj

class TokenObtainPairView(TokenViewBase):
    serializer_class = user_serializer.MyTokenObtainPairSerializer

class TodoGetView(generics.ListAPIView):
	serializer_class = user_serializer.TodoSerializer
	permission_classes = (IsAuthenticated, )

	def get_queryset(self):
		user = self.request.user
		status = self.request.query_params.get('status')
		if status:
			return models.Todo.objects.filter(user=user).filter(status=status)
		else:
			return models.Todo.objects.filter(user=user)

class TodoCreateView(views.APIView):
	permission_classes = (IsAuthenticated, )

	def post(self, request, format=None):
		user = request.user
		empty_fields = {}
		message = "field value not provided"
		keys = ['name']
		for key in keys:
			if key not in request.data:
				empty_fields[key] = message
		if len(empty_fields) != 0:
			return response.Response(status=status.HTTP_400_BAD_REQUEST, data=empty_fields)
		todo = models.Todo.objects.create(
			name=request.data["name"],
            description=request.data["description"],
			user=user,
            userid = user.id
		)
		todo.save()
		return response.Response(data={"detail": "created"}, status=status.HTTP_200_OK)

class TodoUpdateView(views.APIView):
	permission_classes = (IsAuthenticated, )

	def put(self, request, id, format=None):
		user = request.user
		todo = get_object_or_404(models.Todo, id=id, user=user)
		if 'name' in request.data:
			todo.name = request.data['name']
		if 'description' in request.data:
			todo.description = request.data['description']
		if 'status' in request.data:
			todo.status = request.data['status']	

		todo.save()
		return response.Response(data={"detail": "updated"}, status=status.HTTP_200_OK)
	
	def delete(self, request, id, format=None):
		user = request.user
		todo = get_object_or_404(models.Todo, id=id, user=user)
		todo.delete()
		return response.Response(data={"detail": "deleted"}, status=status.HTTP_200_OK)
