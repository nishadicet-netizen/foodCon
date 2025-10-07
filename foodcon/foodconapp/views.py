from django.shortcuts import render, redirect
from django.contrib import messages
from foodconapp.models import UserRegistration
from django.contrib.auth import authenticate, login

# Create your views here.

def public_home(request):
    return render(request, 'public_home.html')
def public_recipe(request):
    return render(request, 'public_recipe.html')
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
def public_chefreg(request):
    return render(request, 'public_chefreg.html')


def public_reg(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        place = request.POST.get('place')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        username = request.POST.get('uname')
        password = request.POST.get('pword')

        # Create and save user
        try:
            user = UserRegistration(
                first_name=first_name,
                last_name=last_name,
                place=place,
                phone=phone,
                email=email,
                username=username,
                password=password 
            )
            user.save()
            messages.success(request, "Registration successful!")
            return redirect('public_home')
        except Exception as e:
            messages.error(request, f"Error: {e}")
    return render(request,'public_reg.html') 


##def save_public_chefreg(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        place = request.POST.get('place')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        username = request.POST.get('uname')
        password = request.POST.get('pword')

        # Create and save user
        try:
            chef = chefRegistration(
                first_name=first_name,
                last_name=last_name,
                place=place,
                phone=phone,
                email=email,
                username=username,
            )
            chef.save()
            messages.success(request, "Registration successful!")
            return redirect('public_home')
        except Exception as e:
            messages.error(request, f"Error: {e}")
    return render(request,'public_reg.html') 




def public_login(request):
    if request.method == "POST":
        em = request.POST.get('email')
        ps = request.POST.get('password')
        
        user = authenticate(request, username=em, password=ps)
        
        if user is not None:
            login(request, user)
            request.session['email'] = em  # Only storing email in session
            messages.success(request, "WELCOME")
            return redirect('public_home')  # Ensure 'public_home' is the correct URL name
        else:
            messages.warning(request, "Try Again")
            return redirect('public_login')  # Ensure 'public_login' is the correct URL name

    return render(request, 'public_login.html')  # Render login template for GET request

