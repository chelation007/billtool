from django.forms import ModelForm
from .models import Product

class addproductform(ModelForm):
    class Meta:
        model = Product
        fields = ['name','hsn_nbr','mfg_date','exp_date','rate','mrp','total_stock']
