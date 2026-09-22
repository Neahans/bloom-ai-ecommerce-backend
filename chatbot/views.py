import os

from django.http import JsonResponse
from rest_framework.decorators import api_view

from google import genai


@api_view(['POST'])
def chat(request):

    message = request.data.get('message')

    if not message:
        return JsonResponse(
            {'error': 'Message is required.'},
            status=400
        )

    api_key = os.getenv('GEMINI_API_KEY')

    if not api_key:
        return JsonResponse(
            {'error': 'Gemini API key is not configured.'},
            status=500
        )

    try:
        client = genai.Client(api_key=api_key)

        interaction = client.interactions.create(
            model="gemini-3.6-flash",
            input=message
        )

        return JsonResponse({
            'reply': interaction.output_text
        })

    except Exception as e:
        print("Gemini Error:", e)

        return JsonResponse(
            {'error': str(e)},
            status=500
        )