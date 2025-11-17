from django.shortcuts import render

def index(request):
    return render(request, 'proj/index.html')

def about(request):
    return render(request, 'proj/about.html')

def evolution(request):
    return render(request, 'proj/evolution.html')

def gamehist(request):
    return render(request, 'proj/gamehist.html')