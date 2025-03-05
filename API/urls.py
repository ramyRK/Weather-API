from .views import weatherView
from django.urls import path,include

urlpatterns = [
    
    path('weather/', weatherView.as_view())
]
