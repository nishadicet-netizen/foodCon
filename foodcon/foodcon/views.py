from django.shortcuts import render

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def public_login(request):
    return render(request, 'publiclogin.html')

def public_recipe(request):
    return render(request, 'publicrecipe.html')

def public_register(request):
    return render(request, 'publicreg.html')
