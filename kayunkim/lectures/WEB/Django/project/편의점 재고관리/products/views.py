from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Store, Company, Incharge, Item
from .forms import ItemForm

# Create your views here.
def index(request):
    stores = Store.objects.all()
    context = {
        'stores':stores,
    }
    return render(request, 'products/index.html', context)

def detail(request, store_pk):
    store = Store.objects.get(id=store_pk)
    context = {
        'store':store,
    }
    return render(request, 'products/detail.html', context)

def create(request, pk):
    store = Store.objects.get(id=pk)
    if request.method=="POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products:detail', pk)
    else:
        form = ItemForm()
    context = {
        'form':form,
        'store':store
    }
    return render(request, 'products/form.html', context)


def item_detail(request, store_pk, item_pk):
    store = Store.objects.get(id=store_pk)
    item = Item.objects.get(id=item_pk)
    context = {
        'store': store,
        'item': item,
    }
    return render(request, 'products/item_detail.html', context)

def edit(request, store_pk, item_pk):
    store = Store.objects.get(id=store_pk)
    item = Item.objects.get(id=item_pk)
    if request.method=="POST":
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('products:item_detail', store_pk, item_pk)
    else:
        form = ItemForm(instance=item)
    context = {
        'form':form,
        'store':store,
    }
    return render(request, 'products/form.html', context)

def delete(request, store_pk, item_pk):
    store = Store.objects.get(id=store_pk)
    item = Item.objects.get(id=item_pk)
    item.delete()
    return redirect('products:detail', store_pk)