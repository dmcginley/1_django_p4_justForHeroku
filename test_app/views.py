from django.shortcuts import render


# Create your views here.
def home(request):
    context = {
        "calculated": 123 * 4565 * 73
    }
    return render(request, "index.html", context)
