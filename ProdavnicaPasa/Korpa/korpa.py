from decimal import Decimal
from django.conf import settings
from SalonPasa.models import Pas
class Korpa(object):
    def __init__(self, request):
        self.sesija = request.session #tekuca sesija
        korpa = self.sesija.get(settings.KORPA_ZA_KUPOVINU_SESSION_KEY)
        #uzeti korpu iz tekuce sesije, ako je nema kreirati je
        if not korpa:
            korpa = self.sesija[settings.KORPA_ZA_KUPOVINU_SESSION_KEY] = {}
        self.korpa = korpa
    def __iter__(self): # za view i sablone
        psi_ids = self.korpa.keys()
        psi = Pas.objects.filter(id__in=psi_ids)
        korpakopija = self.korpa.copy()
        for pas in psi:
            korpakopija[str(pas.id)]['pas'] = pas
        for stavka in korpakopija.values():
            stavka['cena'] = Decimal(stavka['cena'])
            stavka['ukupna_cena'] = stavka['cena'] * stavka['kolicina']
            yield stavka # vraca generator
    def __len__(self):
        return sum(stavka['kolicina'] for stavka in self.korpa.values())

    def Dodaj(self, pas, kolicina=1, dodati_na_kolicinu=True):
        pas_id = str(pas.id)
        if pas_id not in self.korpa:
            self.korpa[pas_id] = {'kolicina': 0,
                                    'cena': str(pas.cena)}
        if dodati_na_kolicinu:
            self.korpa[pas_id]['kolicina'] += kolicina
        else:
            self.korpa[pas_id]['kolicina'] = kolicina
        self.sesija.modified = True

    # da Django "zna" da je sesija modifikovana te da je snimi
    def Ukloni(self, pas):
        pas_id = str(pas.id)

        if pas_id in self.korpa:
            del self.korpa[pas_id]
        self.sesija.modified = True

    def ObrisiJeIzSesije(self):  # uklanjanje korpe iz sesije
        del self.sesija[settings.KORPA_ZA_KUPOVINU_SESSION_KEY]
        self.sesija.modified = True

    def UzmiUkupnuCenu(self):  # ukupna cena u korpi
        return sum(Decimal(stavka['cena']) * stavka['kolicina'] for stavka in
                   self.korpa.values())
