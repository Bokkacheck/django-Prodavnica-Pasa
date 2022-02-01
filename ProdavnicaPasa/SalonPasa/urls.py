from django.urls import path
from . import views
app_name = 'salonpasa'
urlpatterns = [ path('', views.ListaPasa, name='ListaPasa'),
    path('<slug:tipPsa_slug>/', views.ListaPasa,
    name='ListaPasaPoTipu'),
    path('<int:id>/<slug:slug>/', views.DetaljiPsa,
    name='DetaljiPsa'), ]
