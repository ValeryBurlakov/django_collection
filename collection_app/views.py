from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import User, Coin, Collection
from .form import CoinForm, CollectionForm, GetCoinForm
from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'index.html')


@login_required
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


@login_required
def logout_view(request):
    logout(request)
    return render(request, 'index.html')


@login_required
def get_coin(request):
    if request.method == 'POST':
        form = GetCoinForm(request.POST)
        if form.is_valid():
            coin_id = form.cleaned_data['id']
            return redirect('coin_details', coin_id=coin_id)
            # return redirect('coin_details', coin_id=form.cleaned_data['id'])
    else:
        form = GetCoinForm()

    return render(request, 'get_coin.html', {'form': form})


def coin_details(request, coin_id):
    coin = Coin.objects.get(id=coin_id)
    return render(request, 'coin_details.html', {'coin': coin})


@login_required
def add_coin(request):
    if request.method == 'POST':
        form = CoinForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            coin = form.save(commit=False)
            if 'photo' in request.FILES and request.FILES['photo']:
                coin.photo = request.FILES['photo']
            else:
                coin.photo = 'collection_app/coin_photos/default_image.jpg'
            coin.save()
            messages.success(request, 'Монета успешно добавлена')  # Display success message
            return redirect('index')  # Redirect to the index page
        else:
            messages.error(request, 'Ошибка добавления монеты')  # Display error message
            return redirect('index')  # Redirect to the index page
    else:
        form = CoinForm(request.user)
    return render(request, "add_coin.html", {'form': form})


@login_required
def create_collection_view(request):
    if request.method == 'POST':
        form = CollectionForm(request.POST)
        if form.is_valid():
            collection = form.save(commit=False)
            collection.user = request.user
            collection.save()
            messages.success(request, 'Collection created successfully!')
            return HttpResponseRedirect(reverse('get_collection'))
    else:
        form = CollectionForm()
    return render(request, 'create_collection.html', {'form': form})


@login_required
def get_collection(request):
    user_collections = Collection.objects.filter(user=request.user)
    return render(request, 'collection_list.html', {'user_collections': user_collections})


@login_required
def collection_detail(request, collection_id):
    selected_collection = get_object_or_404(Collection, pk=collection_id, user=request.user)
    collection_coins = Coin.objects.filter(collection=selected_collection)
    total_value = Coin.objects.aggregate(Sum('price'))['price__sum']
    return render(request, 'collection_detail.html', {'collection': selected_collection, 'collection_coins': collection_coins, 'total_value': total_value})


@login_required
def delete_collection(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id, user=request.user)
    # Удаление всех монет, связанных с этой коллекцией
    Coin.objects.filter(collection=collection).delete()
    # Удаление самой коллекции
    collection.delete()
    return redirect('get_collection')


def update_coin(request, coin_id):
    coin = get_object_or_404(Coin, id=coin_id)
    if request.method == 'POST':
        form = CoinForm(request.user, request.POST, request.FILES, instance=coin)
        if form.is_valid():
            form.save()
            return redirect('coins_list')
    else:
        form = CoinForm(request.user, instance=coin)

    return render(request, 'update_coin.html', {'form': form})
