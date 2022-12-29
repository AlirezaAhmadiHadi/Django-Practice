from django.shortcuts import render
from .models import Profile
# Create your views here.


def profiles(request):
    profiles = Profile.objects.all()
    content = {'profiles': profiles}
    return render(request, 'users/profiles.html', content)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    content = {'profile': profile,
               'topSkills': topSkills,
               'otherSkills': otherSkills, }
    return render(request, 'users/user-profile.html', content)
