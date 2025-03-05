import json
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .redis_client import redis_client

class weatherView(APIView):
    def get(self ,request):
        city=request.query_params.get('city')

        if not city:
            return Response({'error':"Please provide a city parameter"},status=status.HTTP_400_BAD_REQUEST)
        
        cache_key=city.lower()
        cached=redis_client.get(cache_key)
        if cached:
            weather_data=json.loads(cached)
            return Response({'data':weather_data,'source':'redis'})
        
        api_key=settings.WEATHER_API_KEY
        if not api_key:
            return Response({'error':'Missing weather API key'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        try:
            response=requests.get(url,timeout=10)
            if response.status_code !=200:
                return Response({'error':'Error from external API','status_code': response.status_code,'details':response.text},status=response.status_code)
            weather_data=response.json()
            redis_client.setex(cache_key,3600,json.dumps(weather_data))
            return Response({'data':weather_data,'source':'external'})
        except requests.RequestException as e :
            return Response({'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
