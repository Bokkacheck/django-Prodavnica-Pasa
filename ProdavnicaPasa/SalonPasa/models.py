from django.db import models
from django.urls import reverse

class TipPsa(models.Model):
    naziv = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    class Meta:
        ordering = ('naziv',)
        verbose_name = 'Tip psa'
        verbose_name_plural = 'Tipovi psa'
    def __str__(self): return self.naziv
    def ApsolutniURL(self): return reverse('SalonPasa:ListaPasaPoTipu', args=[self.slug])



class Pas(models.Model):
    tipPsa = models.ForeignKey(TipPsa, related_name='psi',
on_delete=models.CASCADE)
    naziv = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    slika = models.ImageField(upload_to='pas/%Y/%m/%d', blank=True)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    raspoloziv = models.BooleanField(default=True)
    kreiran = models.DateTimeField(auto_now_add=True)
    azuriran = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('naziv',)
        index_together = (('id', 'slug'),)
        verbose_name_plural = 'psi'
    def __str__(self): return self.naziv
    def ApsolutniURL(self): return reverse('SalonPasa:DetaljiPsa', args=[self.id, self.slug])
