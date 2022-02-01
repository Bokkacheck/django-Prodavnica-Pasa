from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from SalonPasa.models import Pas
from .korpa import Korpa
from .forms import FormaZaDodavanjePasaUKorpu
@require_POST #dekorator za prihvatanje POST zahteva
def DodajUKorpu(request, pas_id):
    korpa = Korpa(request)
    pas = get_object_or_404(Pas, id=pas_id)
    form = FormaZaDodavanjePasaUKorpu(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        korpa.Dodaj(pas=pas,
        kolicina=cd['kolicina'],
        dodati_na_kolicinu=cd['dodati_na_kolicinu'])
    return redirect('Korpa:DetaljiKorpe')
@require_POST
def UkloniIzKorpe(request, pas_id):
    korpa = Korpa(request)
    pas = get_object_or_404(Pas, id=pas_id)
    korpa.Ukloni(pas)
    return redirect('Korpa:DetaljiKorpe')

def DetaljiKorpe(request):
    korpa = Korpa(request)
    for stavka in korpa:
        stavka['formazaazuriranjekolicine'] = FormaZaDodavanjePasaUKorpu(initial={'kolicina': 1, 'dodati_na_kolicinu': True})
    return render(request, 'Korpa/detail.html', {'korpa': korpa})
