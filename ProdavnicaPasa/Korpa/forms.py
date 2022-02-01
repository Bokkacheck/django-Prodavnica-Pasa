from django import forms
IZBOR_BROJA_PASA = [(i, str(i)) for i in range(1, 11)]
class FormaZaDodavanjePasaUKorpu(forms.Form):
    kolicina = forms.TypedChoiceField( choices=IZBOR_BROJA_PASA,
empty_value=1,coerce=int ) # prebaci u int
    dodati_na_kolicinu = forms.BooleanField(required=False, initial=True,
widget=forms.HiddenInput)
