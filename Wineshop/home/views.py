from django.shortcuts import render
from .models import RegisterItem
import copy

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
