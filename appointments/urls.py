from django.urls import path
from .views import (ActivePatientsList, ActiveCounsellorsList, ActiveAppointmentsList,
                    AppointmentsForUser, DateRangeAppointmentsList, PatientListCreate,
                    CounsellorListCreate, AppointmentListCreate)

urlpatterns = [
    path('patients/', PatientListCreate.as_view(), name='patient-list-create'),
    path('counsellors/', CounsellorListCreate.as_view(), name='counsellor-list-create'),
    path('appointments/', AppointmentListCreate.as_view(), name='appointment-list-create'),
    path('active-patients/', ActivePatientsList.as_view(), name='active-patients-list'),
    path('active-counsellors/', ActiveCounsellorsList.as_view(), name='active-counsellors-list'),
    path('active-appointments/', ActiveAppointmentsList.as_view(), name='active-appointments-list'),
    path('appointments-for-user/', AppointmentsForUser.as_view(), name='appointments-for-user'),
    path('appointments-date-range/', DateRangeAppointmentsList.as_view(), name='appointments-date-range'),
]
