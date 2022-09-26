from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Item
from .forms import ItemForm, OwnerForm
from django.contrib.auth.decorators import login_required
import redis


SERVER_IP = '127.0.0.1'
SERVER_PORT = '6379'
PASSWORD = ''
DB = 0

def home_item_list(request):
    diff_ip = False
    username = request.user.username

    client = redis.StrictRedis(host=SERVER_IP,
                               port=SERVER_PORT,
                               password=PASSWORD,
                               db=DB,
                               charset="utf-8",
                               decode_responses=True)

    # Client last ip
    last_ip = client.get(username)
    # Client current ip
    current_ip = request.META['REMOTE_ADDR']
    if current_ip != last_ip:
        client.set(username, current_ip)
        if current_ip != None:
            diff_ip = True

    context = {
        'items': Item.objects.all().order_by('created_date'),
        'error': diff_ip
    }
    return render(request, 'app/item_list.html', context)

def item_list(request):
    items = Item.objects.all().order_by('created_date')
    return render(request, 'app/item_list.html', {'items': items})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    owners = item.owner_set.all().order_by('change_date')
    return render(request, 'app/item_detail.html', {'item': item, 'owners': owners})

def item_new(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm()
    return render(request, 'app/item_edit.html', {'form': form})

def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.change_date = timezone.now()
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'app/item_edit.html', {'form': form})

def owner_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            owner = form.save(commit=False)
            owner.change_date = timezone.now()
            owner.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = OwnerForm
    return render(request, 'app/owner_edit.html', {'form': form})


