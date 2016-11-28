""" Views """
from django.views.generic import ListView
from .models import Product


class ProductListView(ListView):
    """ Genereic Product List """
    model = Product
    template_name = 'product_list.html'

    def dispatch(self, *args, **kwargs):
        return super(ProductListView, self).dispatch(*args, **kwargs)
    
