from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'recipes/pages/home.html', context = {
    'name' : 'Wagner Vinicius'
    })


def head(request):
    return render(request, 'recipes/partials/head.html')

