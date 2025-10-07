from django.shortcuts import render

# Create your views here.

def admin_header(request):
    return render(request, 'admin_header.html')
def admin_home(request):
    return render(request, 'admin_home.html')
def admin_send_replay(request):
    return render(request, 'admin_send_replay.html')
def admin_view_chef(request):
    return render(request, 'admin_view_chef.html')
def admin_view_complaint(request):
    return render(request, 'admin_view_complaint.html')
def admin_view_rating(request):
    return render(request, 'admin_view_rating.html')
def admin_view_recipe(request):
    return render(request, 'admin_view_recipe.html')
def admin_view_user(request):
    return render(request, 'admin_view_user.html')
def footer(request):
    return render(request, 'footer.html')