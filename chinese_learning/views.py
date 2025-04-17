# chinese_learning/views.py
from rest_framework import generics, permissions
from .models import Vocabulary
from .serializers import VocabularySerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import requests
import json
from django.conf import settings  # To access settings variables

class VocabularyListView(generics.ListAPIView):
    queryset = Vocabulary.objects.all()
    serializer_class = VocabularySerializer
    permission_classes = [permissions.IsAuthenticated]

class VocabularyDetailView(generics.RetrieveAPIView):
    queryset = Vocabulary.objects.all()
    serializer_class = VocabularySerializer
    permission_classes = [permissions.IsAuthenticated]
    # Define your RapidAPI key and host in Django settings for security
RAPIDAPI_KEY = getattr(settings, 'RAPIDAPI_KEY', 'f719920766msh1c71f3cf11aac91p1e441fjsn0f85b440aa46')
RAPIDAPI_HOST = 'chinese-word-segmenter-with-custom-dictionary.p.rapidapi.com'
SEGMENTATION_API_URL = 'https://chinese-word-segmenter-with-custom-dictionary.p.rapidapi.com/pureCut'

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def segment_chinese_text(request):
    text_to_segment = request.data.get('text')

    if not text_to_segment:
        return Response({'error': 'Missing "text" in the request body.'}, status=400)

    headers = {
        'X-Rapidapi-Key': RAPIDAPI_KEY,
        'X-Rapidapi-Host': RAPIDAPI_HOST,
        'Content-Type': 'application/json'
    }

    payload = {
        'text': text_to_segment
    }

    try:
        response = requests.post(SEGMENTATION_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        segmentation_result = response.json()
        return Response(segmentation_result)
    except requests.exceptions.RequestException as e:
        return Response({'error': f'Error during segmentation API call: {e}'}, status=503)
    except json.JSONDecodeError:
        return Response({'error': 'Error decoding segmentation API response.'}, status=500)