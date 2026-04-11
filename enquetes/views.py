from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Entretien
from .serializers import EntretienSerializer
from django.shortcuts import render

def enquete_view(request):
    return render(request, 'enquete.html')

@api_view(['POST'])
def soumettre_entretien(request):
    serializer = EntretienSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Entretien enregistré'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def liste_entretiens(request):
    entretiens = Entretien.objects.all().order_by('-created_at')
    serializer = EntretienSerializer(entretiens, many=True)
    return Response(serializer.data)
