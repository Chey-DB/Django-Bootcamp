from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'my_app/index.html', {})

def about(request):
    return render(request, 'my_app/about.html', {})

def hello(request, first_name):
    return HttpResponse(f"Hello, {first_name}")

def add(request, num1, num2):
    return HttpResponse(f"{num1} + {num2} = {num1 + num2}")

def movies(request):
    context = {
        "movies": ["Shutter Island", "Inception", "The Dark Knight", "The Prestige"]
    }
    return render(request, 'my_app/index.html', context)

def about(request):
    return render(request, 'my_app/about.html', {})
