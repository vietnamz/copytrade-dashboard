from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate as authenticate
from django.contrib.auth import login as sys_login, logout as sys_logout

from .form import RegisterForm, SignInForm


def register(request):
    """
    main logic to do register a newly user to our system.
    """

    # if the request is POST, means we have the data to process further.
    if request.method == 'POST':
        print('POST form')
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print('Valid form')
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            user_name = form.cleaned_data['user_name']
            password = form.cleaned_data['password']
            
            print('Username:',user_name)
            #  authenticate the user first
            # user = authenticate(request, user_name, password)

            # create a system user.
            user = User.objects.create_user(username=user_name, email=None, password=password)

            # perform login.
            sys_login(request, user)

            # return to home url for now.
            return HttpResponseRedirect('/')
        else:
            print('Invalid form')
            for error in form.errors:
                print(error, end=':')
                print(form.errors[error])
                messages.error(request, form.errors[error])
            
            for error in form.errors:
                first_error = form.errors[error]
                break
            # validation failed, fall back to register form with a error msg.
            return render(request, 'register.html', context={'form': form, 'reg_error': first_error,})
    # this is a GET so we just display a register form.
    
    else:
        print('GET form')
        form = RegisterForm(request.POST)
        # if a GET (or any other method) we'll create a blank form
        return render(request, 'register.html', context={'form': form})


# def login(request):
#     if request.POST:
#         form = SignInForm(request.POST)
#         if form.is_valid():
#             print('Valid form')
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are now logged in as {username}")
#                 return redirect('/')
#             else:
#                 messages.error(request, "Invalid username or password.")
#         else:
#             messages.error(request, "Invalid username or password.")
#     else:
#         form = SignInForm(request.POST)
#         return render(request, 'login.html', context={'form':form})

def logout_request(request):
    sys_logout(request)
    messages.info(request, "Logged out successfully!")
    return HttpResponseRedirect('/')

def login_request(request):
    sig_error = None
    if request.POST:
        print('User login')
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('user_name')
            password = form.cleaned_data.get('password')
            print('validate user',username)
            user = authenticate(username=username, password=password)
            if user is not None:
                sys_login(request, user)
                print('User', username)
                messages.info(request, f"You are now logged in as {username}")
                return HttpResponseRedirect('/')
            else:
                print('incorrect user')
                sig_error= "Invalid username or password."
        else:
            print('Invalid user login')
            sig_error= "Invalid username or password."

        for error in form.errors:
            sig_error = form.errors[error]
            break
            
    print('login load page')

    form = SignInForm(request.POST)
    return render(request, 'login.html', context={'form':form, 'sig_error':sig_error,})
    # return render(request, 'login.html', None)

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