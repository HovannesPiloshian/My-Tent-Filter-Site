from django.shortcuts import render
from .models import Color, Tent

# Create your views here.

def index(request):
    # Get the list of all colors and distinct materials
    color_list = Color.objects.all()
    materials = Tent.objects.values_list('material', flat=True).distinct()

    # Initialize the tent query set
    tent_list = Tent.objects.all()

    # Check if the form has been submitted via POST
    if request.method == 'POST':
        color_id = request.POST.get('color_id')
        tent_name = request.POST.get('tent_name')
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        price = request.POST.get('price')
        capacity = request.POST.get('capacity')

        # Filter by color_id if provided
        if color_id:
            tent_list = tent_list.filter(color=color_id)

        # Filter by tent_name if provided
        if tent_name:
            tent_list = tent_list.filter(name__iexact=tent_name)

        # Filter by weight if provided
        if weight:
            tent_list = tent_list.filter(weight__lte=weight)

        # Filter by height if provided
        if height:
            tent_list = tent_list.filter(height__lte=height)

        # Filter by price if provided
        if price:
            tent_list = tent_list.filter(price__lte=price)

        # Filter by capacity if provided
        if capacity:
            tent_list = tent_list.filter(capacity__gte=capacity)

    return render(request, 'index.html', context={
        'tent_list': tent_list,
        'color_list': color_list,
        'materials': materials
    })
