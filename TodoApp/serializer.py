from rest_framework import serializers
from . import services
from .models import Todo
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)
    created_timestamp = serializers.DateTimeField(read_only=True)
    updated_timestamp = serializers.DateTimeField(read_only=True)

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        return services.UserDataClass(**data)

class ChangePasswordSerializer(serializers.Serializer):    
    password = serializers.CharField(write_only=True)
    updated_timestamp = serializers.DateTimeField(read_only=True)

    def update(self,instance,validated_data):
        instance.set_password(validated_data['password'])        
        instance.save()
        return instance

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self,attrs):
        data=super(MyTokenObtainPairSerializer, self).validate(attrs)
        data.update({'User id':self.user.id})
        return data

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            "id","name","description","status","userid","created_timestamp","updated_timestamp"
        )