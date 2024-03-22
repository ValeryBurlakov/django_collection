from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
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


# @login_required
# def get_coin(request, coin_id):
#     coin = Coin.objects.get(id=coin_id)
#     return render(request, 'get_coin.html', {'coin': coin})
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


@login_required
def create_collection_view(request):
    if request.method == 'POST':
        form = CollectionForm(request.POST)
        if form.is_valid():
            collection = form.save(commit=False)
            collection.user = request.user
            collection.save()
            messages.success(request, 'Collection created successfully!')
            return HttpResponseRedirect(reverse('index'))  # Replace 'index' with the actual name of your index view
    else:
        form = CollectionForm()
    return render(request, 'create_collection.html', {'form': form})


@login_required
def get_collection(request):
    user_collections = Collection.objects.filter(user=request.user)
    return render(request, 'get_collections.html', {'user_collections': user_collections})
