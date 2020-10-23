from django.shortcuts import render, redirect

# Create your views here.


def view_shopping_bag(request):
    """A view to render the shopping bag list"""

    return render(request, 'shoppingbag/shopping_bag.html')


def add_to_shopping_bag(request, item_id):
    """ Add items and their quantity to shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shopping_bag = request.session.get('shopping_bag', {})

    if item_id in list(shopping_bag.keys()):
        shopping_bag[item_id] += quantity
    else:
        shopping_bag[item_id] = quantity

    request.session['shopping_bag'] = shopping_bag
    return redirect(redirect_url)
