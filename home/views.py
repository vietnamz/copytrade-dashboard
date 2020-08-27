from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as system_Login

from .form import RegisterForm, SignInForm


def register(request):
    """
    main logic to do register a newly user to our system.
    """

    # if the request is POST, means we have the data to process further.
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            user_name = form.cleaned_data['user_name']
            password = form.cleaned_data['password']

            #  authenticate the user first
            authenticate(request, user_name, password)
            # create a system user.
            user = User.objects.create_user(username=user_name, email=None, password=password)

            # perform login.
            system_Login(request, user)

            # return to home url for now.
            return HttpResponseRedirect('/')
        else:
            # validation failed, fall back to register form with a error msg.
            return render(request, 'register.html', context={'form': form})
    # this is a GET so we just display a register form.
    else:
        form = RegisterForm(request.POST)
        # if a GET (or any other method) we'll create a blank form
        return render(request, 'register.html', context={'form': form})


def login(request):
    if request.POST:
        pass
    return render(request, 'login.html', None)


def home(request):
    import requests
    import json

    # Grab Crypto Price Data
    price_request = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
    price = json.loads(price_request.content)

    # Grab Crypto News
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    api = [data for data in api['Data'] if data['imageurl'] and data['source'] and data['title'] and data['body'] and data['url']]
    return render(request, 'home.html', {'api': api, 'price': price})


def prices(request):
    if request.method == 'POST':
        import requests
        import json
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get(
            "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote': quote, 'crypto': crypto})
    else:
        notfound = "Enter a crypto currency symbol into the form above..."
        return render(request, 'prices.html', {'notfound': notfound})