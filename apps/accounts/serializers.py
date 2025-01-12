from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.text import slugify

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Adicionar claims customizados
        token['email'] = user.email
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        # Adiciona o id do usuário, email e phone
        data['user_id'] = self.user.id
        data['email'] = self.user.email
       # data['phone'] = self.user.phone
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'phone', 'password')
        extra_kwargs = {'password': {'write_only': True}, 'username': {'read_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = super().create(validated_data) # Cria o usuário primeiro

        # Gerar username único a partir do email após a criação do usuário
        instance.username = slugify(instance.email.split('@')[0])
        while User.objects.filter(username=instance.username).exists():
            instance.username += str(User.objects.filter(username=instance.username).count())
        
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance