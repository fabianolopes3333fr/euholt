# apps/accounts/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db import transaction
from .models import User, Company
from .serializers import UserSerializer, CompanySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_queryset(self):
        # Filtra usuários pela empresa atual
        return super().get_queryset().filter(company=self.request.user.company)

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def register_company(self, request):
        """Registra uma nova empresa com usuário admin"""
        with transaction.atomic():
            # Cria a empresa
            company_serializer = CompanySerializer(data=request.data.get('company'))
            company_serializer.is_valid(raise_exception=True)
            company = company_serializer.save()

            # Cria o usuário admin
            user_data = request.data.get('user')
            user_data['company'] = company.id
            user_data['is_staff_member'] = True
            user_serializer = self.get_serializer(data=user_data)
            user_serializer.is_valid(raise_exception=True)
            user = user_serializer.save()

            return Response({
                'company': company_serializer.data,
                'user': user_serializer.data
            }, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer