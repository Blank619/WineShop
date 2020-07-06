from django.shortcuts import render,redirect
from .models import RegisterItem,cust_details,Cart
import copy
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
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
    i=RegisterItem.objects.get(pk = id)

    print(i.name)
    print(i.Price)
    print(i.quantity)
    print(i.Category)
    dict1={

    'name':i.name,
    'Price':i.Price,
    'quantity':i.quantity,
    'Category':i.Category,
    'id':i.id

    }
    context={
    'data':dict1
    }
    print(dict1)
    print(request.user.username)
    print(request.user.id)
    return render(request,'./view_product.html',context)

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

@login_required
def view_address(request):
    cust_details1=cust_details.objects.get(username=request.user.username)
    print(cust_details1)
    print(cust_details1.username)
    print(cust_details1.address)
    print(cust_details1.number)
    dict1={
    'user':cust_details1.username,
    'address':cust_details1.address,
    'num':cust_details1.number
    }
    context={
    'data':dict1
    }
    return render(request, './view_address.html',context)

def cart(request,id):
    print('inside cart ',id)
    print(request.GET.get('quantity', None))
    quan=request.GET.get('quantity', None)
    print(request.user.username)
    cart_data=Cart(username=request.user.username,user_id=request.user.id,product_id=id,quantity=quan)
    cart_data.save()
    return render(request,'./view_product.html')


def update_address_1(request):
    print(request.POST.get('textarea'))
    print(request.POST.get('number'))
    add=cust_details(username=request.user.username,address=request.POST.get('textarea'),number=request.POST.get('number'))
    add.save()
    return render(request,'./update_address.html')

def view_cart(request):
    cart_data=Cart.objects.filter(username=request.user.username)
    print(cart_data)
    for i in cart_data:
        print(i.username)
        print(i.user_id)
        print(i.product_id)
        print(i.quantity)
    return render(request,'./viewcart.html')
