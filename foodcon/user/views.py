from django.shortcuts import render

# Create your views here.

def user_chat_message(request):
    return render(request, 'user_chat_message.html')
def user_edit_profile(request):
    return render(request, 'user_edit_profile.html')
def user_header(request):
    return render(request, 'user_header.html')
def user_home(request):
    return render(request, 'user_home.html')
def user_registration(request):
    return render(request, 'user_registration.html')
def footer(request):
    return render(request, 'footer.html')
def user_view_recipe(request):
    return render(request, 'user_view_recipe.html')