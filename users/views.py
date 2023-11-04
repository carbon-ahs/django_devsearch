from django.shortcuts import render

def profiles(request):
    # projects = Project.objects.all()
    context = {
        'users': '',
    }
    return render(request, 'users/profiles.html', context)

# Create your views here.
