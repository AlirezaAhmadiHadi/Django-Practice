from django.shortcuts import render

# Create your views here.

def profiles(request):
    content = {}
    return render(request, 'users/profiles.html', content)