from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,  login, logout
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse


# Create your views here.
def home(request):
    if request.method == 'POST':
        sendername = request.POST['sendername']
        recivername = request.POST['recivername']
        senderemail  = request.POST['senderemail']
        reciveremail  = request.POST['reciveremail']
        senderphone  = request.POST['senderphone']
        reciverphone = request.POST['reciverphone']
        senderaddress = request.POST['senderaddress']
        reciveraddress  = request.POST['reciveraddress']
        senderlocation  = request.POST['senderlocation']
        reciverlocation  = request.POST['reciverlocation']
        parcel = request.POST['parcel']
        message = request.POST['message']
        
        
        pickup = Pickup(sendername=sendername,  recivername=recivername, senderemail =senderemail, reciveremail=reciveremail ,senderphone =senderphone, reciverphone =reciverphone, senderaddress =senderaddress, reciveraddress =reciveraddress, senderlocation =senderlocation, reciverlocation =reciverlocation, parcel =parcel, message=message)
        pickup.save()

        return render(request,'emailsent.html')
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return render(request,'emailsent.html')
    context={'form':form}
    return render(request,'contact.html')


def search(request):
    pick = Pickup.objects.order_by('-request_date')
    if 'uuid' in request.GET:
        uuid = request.GET['uuid']
        if uuid:
            pickups = Pickup.objects.filter(uuid__iexact=uuid)
            
    

    context={'pickups':pickups,'pick':pick}
    return render(request,'search.html',context)

    
def tracking(request):
    return render(request,'tracking.html')

def faq(request):
    return render(request,'faq.html')

@login_required(login_url='login')
def rider(request):
    return render(request,'rider.html')

@login_required(login_url='login')
def assignment(request):
  assigns=RiderAssignment.objects.all()
  paginator = Paginator(assigns, 6)
  page = request.GET.get('page')
  paged_assigns = paginator.get_page(page)
  context={'assigns':paged_assigns}
  return render(request,'assignment.html',context)

def register(request):
  if request.method == 'POST':
    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password == password2:
      # Check username
      if User.objects.filter(username=username).exists():
        messages.error(request, 'That username is taken')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'That email is being used')
          return redirect('register')
        else:
          # Looks good
          user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
          # Login after register
          # auth.login(request, user)
          # messages.success(request, 'You are now logged in')
          # return redirect('index')
          user.save()
          messages.success(request, 'You are now registered and can log in')
          return redirect('login')
    else:
      messages.error(request, 'Passwords do not match')
      return redirect('register')
  else:
    return render(request, 'register.html')


def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('rider')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

