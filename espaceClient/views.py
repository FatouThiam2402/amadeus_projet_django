from django.shortcuts import render, redirect
import mysql.connector
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages, auth

connection = mysql.connector.connect(
        host='localhost',
        user='Moussa',
        password='root123',
        database='amadeus'
)
# Create your views here.
def login(request) :
 	return render(request, 'espaceClient/login.html')


def acceuil(request):
    return  render(request, '/')

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.save()
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=user.username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'auth/signup.html', { 'form' : form })
# from django.http import HttpResponseRedirect
# return HttpResponseRedirect(reverse('app:view', kwargs={'bar':FooBar}))
#
def logout(request) : 
    template_name = 'hotel/index.html'
    auth.logout(request)
    # connected = None
    return render(request, template_name)

def seConnecter(request):
    user = ''
    passw = ''
    cursor = connection.cursor()
    if request.POST:
        user = request.POST['User_Email']
        template_name = 'reservation/paiement.html'
        passw = request.POST['User_Password']
        userelt = auth.authenticate(username=user,password=passw)
        query = "select * from Client WHERE email = %s and password1=%s"
        parameters=[user,passw]
        cursor.execute(query, parameters)
        connected = cursor.fetchall()
        if (len(connected)>0) :
            if userelt is not None:
                auth.login(request,userelt)
                return render (request,'espaceClient/login.html', {'error':'Username or password is incorrect!'})
            else:
                return render (request,'espaceClient/login.html', {'error':'Username or password is incorrect!'})
    return render(request,template_name)

        # print(connected)
        # context = {'connected': connected}
        # if (len(connected)>0) : 
        #     return render(request, template_name , context)
        # else:
        #     messages.error(request, 'Nom d utilisateur ou mot de passe Incorrect')
        #     return render(request, 'espaceClient/login.html', context)
        
        

# from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
# from django.contrib import auth

# def signup(request):
#     if request.method == "POST":
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 User.objects.get(username = request.POST['username'])
#                 return render (request,'accounts/signup.html', {'error':'Username is already taken!'})
#             except User.DoesNotExist:
#                 user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
#                 auth.login(request,user)
#                 return redirect('home')
#         else:
#             return render (request,'accounts/signup.html', {'error':'Password does not match!'})
#     else:
#         return render(request,'accounts/signup.html')

# def login(request):
#     if request.method == 'POST':
#         user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
#         if user is not None:
#             auth.login(request,user)
#             return redirect('home')
#         else:
#             return render (request,'accounts/login.html', {'error':'Username or password is incorrect!'})
#     else:
#         return render(request,'accounts/login.html')

# def logout(request):
#     if request.method == 'POST':
#         auth.logout(request)
#     return redirect('acceuil')

