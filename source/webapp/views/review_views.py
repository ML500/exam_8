from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import ReviewForm
from webapp.models import Review, Product


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/review_create.html'
    # permission_required = 'webapp.add_review'

    # def has_permission(self):
    #     self.product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
    #     return super().has_permission() and self.request.user in self.product.user.all()

    def dispatch(self, request, *args, **kwargs):
        self.product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['product'] = self.product
        kwargs['author'] = self.request.user
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.product = self.product
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.product.pk})