from django.shortcuts import render,redirect
from .models import todo
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='signup')
def home(request):
    if request.method == "POST" :
        name=request.POST.get('name')
        if name is not None :
            en=todo(todo_name=name,user=request.user)
            en.save()
        else :
            redirect(home)


    data=todo.objects.filter(user=request.user)

    if request.method == "GET":
        search=request.GET.get('search')
        if search is not None:
            data=todo.objects.filter(todo_name__icontains=search)
        
    return render(request,"index.html",{'datas':data})

def delete(request,id):
    try:
        todos=todo.objects.get(id=id)
        todos.delete()
    except todo.DoesNotExist:
        pass

    return redirect(home)  


def mark_as_complete(request,id):

    try:
        todos=todo.objects.get(id=id)
        todos.is_complete=True
        todos.save()
    except todo.DoesNotExist:
        pass

    return redirect(home)  


def Unmark_as_complete(request,id):

    try:
        todos=todo.objects.get(id=id)
        todos.is_complete=False
        todos.save()
    except todo.DoesNotExist:
        pass

    return redirect(home)      

def signin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            messages.info(request,"Do not have an account")
            return redirect('signin')     
    else:
        return render(request,'signin.html')


def signup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password1=request.POST.get('password1')

        if password == password1 :
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
                return redirect(signup)

            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
                return redirect(signup) 

            else:
                en=User.objects.create_user(username=username,email=email,password=password)
                en.save()
                messages(request,"Account have been created successfully ")
                return redirect(signup)       
        else:
            messages.info(request,"password are not same")
            return redirect(signup) 
    else:
        return render(request,'signup.html') 

def logout(request):
    auth.logout(request)
    return redirect('home')          
