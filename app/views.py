from django.db.models import Q
from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()

    # Dynamic filters
    name = request.GET.get('name')
    category = request.GET.get('category')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    # Build a Q object for filtering
    filter_criteria = Q()

    if name:
        filter_criteria &= Q(name__icontains=name)
    if category:
        filter_criteria &= Q(category__icontains=category)
    if min_price:
        filter_criteria &= Q(price__gte=min_price)
    if max_price:
        filter_criteria &= Q(price__lte=max_price)

    # Apply filters
    products = products.filter(filter_criteria)

    return render(request, 'index.html', {'products': products})
