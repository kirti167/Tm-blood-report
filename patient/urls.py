from django.contrib import admin
from django.urls import path
from .views import PatientUpdateView,home,PatientCreateView, DocumentCreateView,PatientProfileView,DocumentUploadView,DisplayResponseView
urlpatterns = [
    path('',home,name='home'),
    path('create/',PatientCreateView.as_view(),name='patient_create'),
    path('detail/<int:pk>', PatientProfileView.as_view(), name='patient_detail'),
    path('update/<int:pk>', PatientUpdateView.as_view(), name='patient_update'),
    path('upload/<int:pk>', DocumentUploadView.as_view(), name='document_upload'),
    #path('document/', DocumentCreateView.as_view(), name='document_upload')
    path('response/<int:patient_id>/<int:document_id>',DisplayResponseView.as_view(),name='response')
]
