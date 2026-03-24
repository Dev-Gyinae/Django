from django.shortcuts import render, get_object_or_404
from .models import item  

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