from django import forms

from webapp.models import Product, Review


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'avatar']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text_review', 'rating']
