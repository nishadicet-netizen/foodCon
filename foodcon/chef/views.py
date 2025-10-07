from django.shortcuts import render

# Create your views here.

def chef_add_comment(request):
    return render(request, 'chef_add_comment.html')
def chef_add_rating(request):
    return render(request, 'chef_add_rating.html')
def chef_header(request):
    return render(request, 'chef_header.html')
def chef_home(request):
    return render(request, 'chef_home.html')
def chef_upload_recipe(request):
    return render(request, 'chef_upload_recipe.html')
def chef_view_comment(request):
    return render(request, 'chef_view_comment.html')
def chef_view_other_recipe(request):
    return render(request, 'chef_view_other_recipe.html')
def chef_view_rating(request):
    return render(request, 'chef_view_rating.html')
def chef_view_recipe_detail(request):
    return render(request, 'chef_view_recipe_detail.html')
def footer(request):
    return render(request, 'footer.html')