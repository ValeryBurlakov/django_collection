from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import User, Coin, Collection
from .form import CoinForm, CollectionForm


def index(request):
    return HttpResponse("Hello Valera")


def get_users(request, client_id):
    user = User.objects.get(id=client_id)
    # Here, create an HTML table to display the client details
    html = f"""
    <h2>Карточка клиента</h2>
    <table>
        <tr>
            <th>ID клиента</th>
            <th>Имя пользователя</th>
        </tr>
        <tr>
            <td>{user.id}</td>
            <td>{user.username}</td>
        </tr>
    </table>
    """
    return HttpResponse(html)


def get_coin(request, coin_id):
    coin = Coin.objects.get(id=coin_id)
    return render(request, 'get_coin.html', {'coin': coin})

def add_coin(request):
    if request.method == 'POST':
        form = CoinForm(request.POST, request.FILES)
        if form.is_valid():
            coin = form.save(commit=False)
            if 'photo' in request.FILES and request.FILES['photo']:
                coin.photo = request.FILES['photo']
            else:
                coin.photo = 'collection_app/coin_photos/default_image.jpg'
            coin.save()
            return HttpResponse("success")
        else:
            return HttpResponse("invalid form")
    else:
        form = CoinForm()
    return render(request, "add_coin.html", {'form': form})


# def edit_coin(request, product_id):
#     product = get_object_or_404(Coin, pk=product_id)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES, instance=product)
#         if form.is_valid():
#             if 'photo' not in request.FILES:
#                 product.photo = 'homework_app/product_photos/default_image.jpg'
#             form.save()
#     else:
#         form = ProductForm(instance=product)
#     return render(request, 'homework_app/edit_product.html', {'form': form, 'name': product.name})
#
