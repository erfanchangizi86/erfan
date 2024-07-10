from django import forms
from  .models import Brands

class BrandForm(forms.Form):
    brand_name = forms.ModelMultipleChoiceField(queryset=Brands.objects.all(),
                                                widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-label',
                                                                                           'id': 'brand_id'}),
                                                required=False)

