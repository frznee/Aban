from django.shortcuts import render, redirect
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
from .forms import CommentForm


base_url = 'AbanGasPart'


def home(request):
    items = Item.objects.all().order_by('created_at')

    return render(request, f'{base_url}/home.html', {
        'items': items,
        'category_list': Item.CATEGOTY_LIST
    })


def technicians_list(request):
    provinces = Province.objects.all()
    selected_province_id = request.GET.get("province")
    selected_city_id = request.GET.get("city")

    technicians = []
    cities = []

    if selected_province_id:
        cities = City.objects.filter(province_id=selected_province_id)
    if selected_city_id:
        technicians = City.objects.get(id=selected_city_id).technicians.all()

    return render(request, f'{base_url}/technicians_list.html', {
        "provinces": provinces,
        "cities": cities,
        "technicians": technicians,
        "selected_province_id": selected_province_id,
        "selected_city_id": selected_city_id,
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
    # Fetch latest 10 comments
    comments = Comment.objects.order_by('-created_at')[:10]
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')

    return render(request, f'{base_url}/about.html', {
        'form': form,
        'comments': comments,
    })
