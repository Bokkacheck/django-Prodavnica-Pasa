from django.urls import path
from . import views

app_name = 'korpa'

urlpatterns = [
    path('', views.DetaljiKorpe, name='DetaljiKorpe'),
    path('dodaj/<int:pas_id>/',
            views.DodajUKorpu, name='DodajUKorpu'),
    path('ukloni/<int:pas_id>/',
            views.UkloniIzKorpe, name='UkloniIzKorpe'),
]