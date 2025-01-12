from datetime import datetime, timedelta
from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(source='service.name', read_only=True)
    client_name = serializers.CharField(
        source='client.get_full_name',
        read_only=True
    )
    professional_name = serializers.CharField(
        source='professional.get_full_name',
        read_only=True
    )

    class Meta:
        model = Appointment
        fields = '__all__'
        
    def validate(self, data):
        # Calcula horário de término baseado na duração do serviço
        if 'start_time' in data and 'service' in data:
            service_duration = data['service'].duration
            start_datetime = datetime.combine(
                data['date'],
                data['start_time']
            )
            end_datetime = start_datetime + timedelta(minutes=service_duration)
            data['end_time'] = end_datetime.time()

        # Valida disponibilidade do profissional
        if all(k in data for k in ('professional', 'date', 'start_time')):
            conflicts = Appointment.objects.filter(
                professional=data['professional'],
                date=data['date'],
                status__in=['scheduled', 'confirmed', 'in_progress']
            )
            
            if self.instance:
                conflicts = conflicts.exclude(id=self.instance.id)

            for appointment in conflicts:
                if (data['start_time'] < appointment.end_time and 
                    data['end_time'] > appointment.start_time):
                    raise serializers.ValidationError(
                        'Profissional não está disponível neste horário'
                    )

        return data