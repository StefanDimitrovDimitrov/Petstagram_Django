from django.shortcuts import render


# Create your views here.
def landing_page(request):
    return render(request, 'index.html')


def original(request):
    return render(request, 'landing_page.html')