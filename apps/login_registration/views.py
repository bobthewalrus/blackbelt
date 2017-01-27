from django.shortcuts import render, HttpResponse, redirect
from models import User, Quote
from django.contrib import messages
from django.urls import reverse

# Create your views here.


def index(request):

    return render(request, "login_registration/index.html")
def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request,messages.INFO, message)

def loginvalidate(request):
    if request.method == "POST":
        print 'here'
        print request.POST['email']
        result = User.objects.loginvalidation(request.POST)
        print result

        if result[0] == False:
            print_messages(request, result[1])
            return redirect(reverse('index'))
        return login(request, result[1])
    return redirect('/')
def quotevalidate(request):
    if request.method =='POST':
        print "*****Validating quote**********"
        print request.session['user']['id']
        result = Quote.objects.quotevalidator(request.POST, request.session['user']['id'])
        if not result[0]:
            print_messages(request, result[1])
            return redirect('/success')

        return redirect('/success')

# t = TemperatureData.objects.get(id=1)
# t.value = 999  # change field
# t.save() # this will update only


    return redirect('/success')
def faveon(request):
    if request.method == 'POST':
        print "*********Adding to favorites list*******"
        favoritecheck = request.POST['onid']
        favoriteswitch = Quote.objects.get(id=favoritecheck)

        print favoritecheck
        print favoriteswitch
        print favoriteswitch.favorites
        favoriteswitch.favorites = True
        favoriteswitch.save()
        print favoriteswitch.favorites


    return redirect('/success')
def faveoff(request):
    if request.method == 'POST':
        print "*********Removing from favorites list*******"
        favoritecheck = request.POST['offid']
        print favoritecheck
        favoriteswitch = Quote.objects.get(id=favoritecheck)

        print favoritecheck
        print favoriteswitch
        print favoriteswitch.favorites
        favoriteswitch.favorites = False
        favoriteswitch.save()
        print favoriteswitch.favorites


    return redirect('/success')

def userview(request, userid):
    print "Did userid pass? ===>"+userid
    getuser = Quote.objects.filter(user=userid)
    print getuser
    userdict = {
    "userposts":getuser,
    }
    return render(request, 'login_registration/userview.html', userdict)

def registervalidate(request):
    result= User.objects.registervalidation(request.POST)

    if not result[0]:
        print_messages(request, result[1])
        return redirect('/')

    return login(request, result[1])

def success(request):
    if not 'user' in request.session:
        return redirect('/')
    quotes = Quote.objects.filter(favorites=False)
    faves= Quote.objects.filter(favorites=True)

    quotecontext = {
    "quotationlist":quotes,
    "favoriteslist":faves
    }
    return render(request, 'login_registration/success.html',quotecontext)

def login(request, user):
    print "Here at Login"
    request.session['user'] = {
    'id': user.id,
    'first_name' : user.firstname,
    'last_name' : user.lastname,
    'email' : user.email,
    }
    return redirect('/success')
def logout(request):
    request.session.clear()
    # request.session.pop('user')
    return redirect('/')
