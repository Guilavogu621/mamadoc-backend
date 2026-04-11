from django.urls import path
from . import views

urlpatterns = [
    path('', views.enquete_view),
    path('soumettre/', views.soumettre_entretien),
    path('liste/', views.liste_entretiens),
]