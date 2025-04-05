from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category
from .forms import CategoryForm  # You'll create this below
from .models import Room
from .forms import RoomForm
from .models import Product
from .forms import ProductForm
from .models import Inventory
from .forms import InventoryForm
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/list.html', {'categories': categories})


def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'categories/form.html', {'form': form})


def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'categories/form.html', {'form': form})


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        category.delete()
        return redirect('category_list')
    return render(request, 'categories/confirm_delete.html', {'category': category})




def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/list.html', {'rooms': rooms})


def room_create(request):
    form = RoomForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('room_list')
    return render(request, 'rooms/form.html', {'form': form})


def room_update(request, pk):
    room = get_object_or_404(Room, pk=pk)
    form = RoomForm(request.POST or None, instance=room)
    if form.is_valid():
        form.save()
        return redirect('room_list')
    return render(request, 'rooms/form.html', {'form': form})


def room_delete(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('room_list')
    return render(request, 'rooms/confirm_delete.html', {'room': room})



def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'products': products})


def product_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'products/form.html', {'form': form})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'products/form.html', {'form': form})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/confirm_delete.html', {'product': product})


def inventory_list(request):
    items = Inventory.objects.select_related('product', 'room').all()
    return render(request, 'inventory/list.html', {'items': items})


def inventory_create(request):
    form = InventoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inventory_list')
    return render(request, 'inventory/form.html', {'form': form})


def inventory_update(request, pk):
    item = get_object_or_404(Inventory, pk=pk)
    form = InventoryForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('inventory_list')
    return render(request, 'inventory/form.html', {'form': form})


def inventory_delete(request, pk):
    item = get_object_or_404(Inventory, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('inventory_list')
    return render(request, 'inventory/confirm_delete.html', {'item': item})


def home(request):
    context = {
        'total_categories': Category.objects.count(),
        'total_products': Product.objects.count(),
        'total_rooms': Room.objects.count(),
        'total_inventory': Inventory.objects.count(),
    }
    return render(request, 'home.html', context)