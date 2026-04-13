from django.urls import path
from . import views

urlpatterns = [
    path('', views.enquete_view),
    path('soumettre/', views.soumettre_entretien),
    path('liste/', views.liste_entretiens),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('detail/<int:pk>/', views.entretien_detail_view, name='entretien_detail'),
]