

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm

def item_list(request):
    items = Item.objects.all()
    return render(request, 'Cruds/item_list.html', {'items': items})

def item_create(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('item_list')
    return render(request, 'Cruds/item_form.html', {'form': form})

def item_update(request, id):
    item = get_object_or_404(Item, id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('item_list')
    return render(request, 'Cruds/item_form.html', {'form': form})

def item_delete(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'Cruds/item_confirm_delete.html', {'item': item})
