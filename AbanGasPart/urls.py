from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name="home"), 
    path("items/<category>/", views.items, name="items"), 
    path("item/<item_title>/", views.item_page, name="itempage"), 
    path("about/", views.about_page, name="about"),
    path("technicians/", views.technicians_list, name="technicians_list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
