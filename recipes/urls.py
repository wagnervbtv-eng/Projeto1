from recipes.views import home, head
from django.urls import path



urlpatterns = [
    path('', home),
    path('head/', head)  
]