from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Item

def item_list(request):
    items = Item.objects.filter().order_by('created_date')
    return render(request, 'app/item_list.html', {'items': items})
