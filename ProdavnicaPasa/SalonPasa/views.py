from django.shortcuts import render, get_object_or_404
from .models import TipPsa, Pas
from Korpa.korpa import Korpa
from Korpa.forms import FormaZaDodavanjePasaUKorpu


def ListaPasa(request, tipPsa_slug=None): # vraca katalog kao html
    tipPsa = None
    tipoviPsa = TipPsa.objects.all()
    psi = Pas.objects.filter(raspoloziv=True)
    if tipPsa_slug:
        tipPsa = get_object_or_404(TipPsa, slug=tipPsa_slug)
        psi = psi.filter(tipPsa=tipPsa)
    korpa = Korpa(request)
    return render(request, 'SalonPasa/pas/list.html',
        {'tipPsa': tipPsa, 'tipoviPsa': tipoviPsa,
        'psi': psi
         , 'korpa':korpa
         })

def DetaljiPsa(request, id, slug):

    pas = get_object_or_404(Pas, id=id, slug=slug,
    raspoloziv=True)
    korpa = Korpa(request)
    formazadodavanjepasaukorpu = FormaZaDodavanjePasaUKorpu()
    return render(request, 'SalonPasa/pas/detail.html',{'pas': pas
        ,  'formazadodavanjepasaukorpu': formazadodavanjepasaukorpu, 'korpa':korpa
})