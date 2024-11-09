from django.shortcuts import render



def home_view(request):
    return render(request,'_layouts/home.html')