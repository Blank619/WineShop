from django.shortcuts import render,redirect
from .models import RegisterItem
import copy
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

def HomeView(request):
    return render(request, './home.html')


def view_category(request):
    items=RegisterItem.objects.all()
    list1=[]
    dict1={}
    list2=[]
    for i in items:
        print(i.name,' ',i.Price,' ',i.Category)
        list1.append(i.name)
        list1.append(i.Price)
        list1.append(i.Category)
        list1.append(i.quantity)
        list2 = copy.deepcopy(list1)
        dict1[i.id] = list2

        list1.clear()
    print(dict1)
    context={'data_items':dict1}

    return render(request, './view_category.html',context)


def View_product(request,id):
    items=RegisterItem.objects.get(pk = id)
    print(items)


def register_1(request):
    print('inside views')

    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for{username}!')
            return redirect('login')

    else:
        form=UserRegisterForm()


    return render(request,'./register.html',{'form':form})


def Update_address(request):
    return render(request, './Update_address.html')
