from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm
from webapp.models import Product
from webapp.views.base_views import SearchView


class IndexView(ListView):
    template_name = 'product/index.html'
    context_object_name = 'products'
    model = Product


class ProductView(DetailView):
    template_name = 'product/product_view.html'
    model = Product


class ProductCreateView(CreateView):
    template_name = 'product/product_create.html'
    form_class = ProductForm
    model = Product

    # permission_required = 'webapp.add_product'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductUpdateVIew(UpdateView):
    template_name = 'product/product_update.html'
    model = Product
    form_class = ProductForm
    # permission_required = 'webapp.change_product'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    template_name = 'product/product_delete.html'
    model = Product
    success_url = reverse_lazy('webapp:index')
    # permission_required = 'webapp.delete_product'