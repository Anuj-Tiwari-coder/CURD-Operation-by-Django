from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    context= {'page':'home'}
    return render(request, 'home.html', context)

@login_required(login_url='/login/')
def recipe_page(request):
    if request.method == "POST":
        data= request.POST
        name= data.get('name')
        ingredients= data.get('ingredients')
        instructions= data.get('instructions')
        description= data.get('description')
        image= request.FILES.get('image')
        
        Recipe.objects.create(name = name,
                                ingredients = ingredients,
                                instructions = instructions,
                                description = description,
                                image = image)
        return redirect('/recipe_page/')
    qureyset= Recipe.objects.all()
        
    context = {'recipes': qureyset}
    return render(request, 'recipe_page.html', context)


@login_required(login_url='/login/')
def delete_recipe(request,id):
    queryset=Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipe_page/')

@login_required(login_url='/login/')
def update_recipe(request, id):
    queryset=Recipe.objects.get(id=id)
    if request.method == "POST":
        data= request.POST
        name= data.get('name')
        ingredients= data.get('ingredients')
        instructions= data.get('instructions')
        description= data.get('description')
        image= request.FILES.get('image')

        queryset.name = name
        queryset.ingredients = ingredients
        queryset.instructions = instructions
        queryset.description = description
        if image:
            queryset.image = image
        
        queryset.save()
        return redirect('/recipe_page/')
    context= {'recipes': queryset}
    return render(request, 'Update_page.html', context)

def login_page(request):
    if request.method == "POST":
        username= request.POST.get("username")
        password= request.POST.get("password")
        
        if not User.objects.filter(username=username).exists():
            messages.info(request, "User Already exist.")
            return redirect('/login/')
        
        user= authenticate(username = username, password = password )
        if user is None:
            messages.error(request, "Invalid username or password")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/recipe_page/')
        

    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect ('/login/')

def register_page(request):
    if request.method == "POST":
        first_name= request.POST.get("first_name")
        last_name= request.POST.get("last_name")
        username= request.POST.get("username")
        password= request.POST.get("password")

        user= User.objects.filter(username = username)
        if user.exists():
            messages.info(request, "Oops Username Already Taken please! Select New One.")
            return redirect('/register/')
        
        user=User.objects.create(
                                first_name = first_name,
                                last_name = last_name,
                                username = username)
        
        user.set_password(password)
        user.save()
        messages.info(request, "Account Created Successfully.")
        return redirect('/register/')
    return render(request, 'register.html')