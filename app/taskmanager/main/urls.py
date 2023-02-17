from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='home'),
    path('diseases', views.DiseasesListView.as_view(), name='diseases'),
    path('symptoms', views.SymptomsListView.as_view(), name='symptoms'),
    path('disease/<int:disease_id>/', views.DiseaseDetailView.as_view(), name='disease_detail'),
    path('symptom/<int:symptom_id>/', views.SymptomDetailView.as_view(), name='symptom_detail'),
    path('send_question', views.QuestionView.as_view(), name='send_question')
]

