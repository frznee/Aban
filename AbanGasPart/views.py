from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
import requests
from django.contrib import admin
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .models import *



base_url = 'AbanGasPart'


def home(request):
    items = Item.objects.all().order_by('created_at')

    return render(request, f'{base_url}/home.html', {
        'items': items,
        'category_list': Item.CATEGOTY_LIST
    })


def items(request, category):
    if category == "all":
        items = Item.objects.all()
    else:
        items = Item.objects.filter(category=category)
        
    paginator = Paginator(items, 6)  
    page_number = request.GET.get('page')
    page_items = paginator.get_page(page_number)

    return render(request, f'{base_url}/items.html', {
        'items': items,
        'page_items': page_items,
        'category_list': Item.CATEGOTY_LIST
        })


def item_page(request, item_title):
    item = Item.objects.get(title=item_title)
    
    
    return render(request, f'{base_url}/item-page.html', {
        'item': item,
        'category_list': Item.CATEGOTY_LIST
    })


def about_page(request):
    
    
    return render(request, f'{base_url}/about.html', {
        'category_list': Item.CATEGOTY_LIST
    })
