from rest_framework import generics, filters
from .models import Patient, Counsellor, Appointment
from .serializers import PatientSerializer, CounsellorSerializer, AppointmentSerializer

class PatientListCreate(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class CounsellorListCreate(generics.ListCreateAPIView):
    queryset = Counsellor.objects.all()
    serializer_class = CounsellorSerializer

class AppointmentListCreate(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class ActivePatientsList(generics.ListAPIView):
    queryset = Patient.objects.filter(is_active=True)
    serializer_class = PatientSerializer

class ActiveCounsellorsList(generics.ListAPIView):
    queryset = Counsellor.objects.filter(is_active=True)
    serializer_class = CounsellorSerializer

class ActiveAppointmentsList(generics.ListAPIView):
    queryset = Appointment.objects.filter(is_active=True)
    serializer_class = AppointmentSerializer

class AppointmentsForUser(generics.ListAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        user_type = self.request.query_params.get('user_type', None)
        user_id = self.request.query_params.get('user_id', None)

        if user_type == 'patient':
            return Appointment.objects.filter(patient__id=user_id)
        elif user_type == 'counsellor':
            return Appointment.objects.filter(counsellor__id=user_id)
        else:
            return Appointment.objects.none()

class DateRangeAppointmentsList(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['-appointment_date']

    def get_queryset(self):
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)

        if start_date and end_date:
            return Appointment.objects.filter(appointment_date__range=[start_date, end_date], is_active=True)
        else:
            return Appointment.objects.none()