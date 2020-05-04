from store.models import Store
from django.shortcuts import render

# Create your views here.


def home_view(request):
    context = {
        'stores': Store.objects.all()
    }

    return render(request, 'home.html', context)


def about_view(request):
    my_context = {
        "my_text": "This is about us",
        "my_number": "202342141224",
        "my_list": ["Shrey", "Vineet", "Vignesh", "Bao", "Anirudh"]
    }
    return render(request, 'about.html', my_context)


def contact_view(request):
    return render(request, 'contact.html', {})


"""
def contact_view(request, *args, **kwargs):
    return HttpResponse('<h2>Contact View</h2>')
    """
