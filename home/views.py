from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate as authenticate
from django.contrib.auth import login as sys_login, logout as sys_logout

from .form import RegisterForm, SignInForm

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def user_exist(request):
    if not request.GET.get('username'): return JsonResponse(False, safe=False)
    user_name = request.GET.get('username')
    logger.error("user_name %s", user_name)
    if len(User.objects.filter(username=user_name)) > 0:
        return JsonResponse(True, safe=False)
    return JsonResponse(False, safe=False)


def register(request):
    """
    main logic to do register a newly user to our system.
    """
    # if the request is POST, means we have the data to process further.
    if request.method == 'POST':
        logger.info('POST form')
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            logger.info('Valid form')
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            user_name = form.cleaned_data['id_username_r']
            password = form.cleaned_data['id_password_r']
            
            logger.info('Username:', user_name)
            #  authenticate the user first
            # user = authenticate(request, user_name, password)

            # create a system user.
            user = User.objects.create_user(username=user_name, email=None, password=password)

            # perform login.
            sys_login(request, user)

            # return to home url for now.
            return HttpResponseRedirect('/')
        return render(request, '404.html', None)


def logout_request(request):
    sys_logout(request)
    logger.info(request, "Logged out successfully!")
    return HttpResponseRedirect('/')


def login_request(request):
    sig_error = None
    if request.POST:
        logger.info('User login')
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('user_name')
            password = form.cleaned_data.get('password')
            logger.info('validate user',username)
            user = authenticate(username=username, password=password)
            if user is not None:
                sys_login(request, user)
                logger.info('User', username)
                messages.info(request, f"You are now logged in as {username}")
                return HttpResponseRedirect('/')
            else:
                logger('incorrect user')
                sig_error= "Invalid username or password."
        else:
            logger.info('Invalid user login')
            sig_error= "Invalid username or password."

        for error in form.errors:
            sig_error = form.errors[error]
            break
            
    logger.info('login load page')

    form = SignInForm(request.POST)
    return render(request, 'login.html', context={'form':form, 'sig_error':sig_error,})


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
    #return render(request, 'home.html', {'api': api, 'price': price})
    if request.user.is_authenticated:
        return  render(request, 'index.html', None)
    return render(request, 'get-started.html', None)


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


def user_profile(request):
    return render(request, 'profile.html', None)