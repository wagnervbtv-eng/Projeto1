from recipes.views import contact, home
from django.urls import path



urlpatterns = [
    path('', home),
    path('contact/', contact)
]