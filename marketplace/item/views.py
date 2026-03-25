from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import item, category
from item.forms import NewItemForm, EditItemForm

def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)  # Changed to 'category' for better naming
    categories = category.objects.all()
    
    # Start with all unsold items
    items = item.objects.filter(is_sold=False)
    
    # Filter by category if selected
    if category_id and category_id != '0' and category_id != 0:
        items = items.filter(category_id=category_id)
    
    # Filter by search query if provided
    if query:
        items = items.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query)
        )
    
    # Convert category_id to int for template
    try:
        category_id = int(category_id)
    except ValueError:
        category_id = 0

    return render(request, 'item/items.html', {
        'items': items, 
        'categories': categories,
        'query': query,
        'category_id': category_id,
    })

def detail(request, pk):
    current_item = get_object_or_404(item, pk=pk)
    related_items = item.objects.filter(
        category=current_item.category,
        is_sold=False
    ).exclude(pk=pk)[0:2]
    
    return render(request, 'item/detail.html', {
        'item': current_item,
        'related_items': related_items,
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.created_by = request.user
            new_item.save()
            return redirect('item:detail', pk=new_item.id)
    else:
        form = NewItemForm()
    return render(request, 'item/form.html', {'form': form, 'title': 'New Item'})

@login_required
def edit(request, pk):
    item_to_edit = get_object_or_404(item, pk=pk, created_by=request.user)
    
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item_to_edit)
        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=item_to_edit.id)
    else:
        form = EditItemForm(instance=item_to_edit)
    
    return render(request, 'item/form.html', {'form': form, 'title': 'Edit Item'})

@login_required
def delete(request, pk):
    item_to_delete = get_object_or_404(item, pk=pk, created_by=request.user)
    item_to_delete.delete()
    return redirect('dashboard:index')