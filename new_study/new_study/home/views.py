from django.shortcuts import render
from home.models import Menu 

# Create your views here.

def home(request):
    context = {}
    try:
        menu = Menu.objects.all()
    except Exception as err:
        print(err)

    if menu:
        context['menu'] = menu

    return render(request,'home/index.html', context)


def about(request):
    return render(request, 'home/index.html')

