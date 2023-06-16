from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.


def indexpage(request):
        return render(request, 'mainpage/index.html')
    
def seConnecter(request):
    if request.method == "POST":
        username = request.POST["User_Email"]
        password = request.POST["User_Password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("indexpage"))
            
        else:
            return render(request, 'mainpage/login.html', {
                "errors": "Nom d utilisateur et/ou mot de passe incorrect(s)."
            })
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('indexpage'))
        else:
            return render(request, 'mainpage/login.html')
    
def seDeconnecter(request):
    logout(request)
    return HttpResponseRedirect(reverse("indexpage"))

def sInscrire(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "mainpage/inscription.html", {
                "errors": "Les mots de passe ne sont pas Conformes"
            })

        try:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=fname, last_name=lname)
            user.first_name = fname
            user.last_name = lname
            user.save()
            if email :
                subject = 'BitMasters'
                message = 'Bienvenue'+fname+' '+lname+' Dans votre site de Reservation BitMasters'
                defaultmail='moseesjoof42@gmail.com'
            send_mail(
                subject,
                message,
                defaultmail,
                [email],
                fail_silently=False,
            )
            messages.success(request, " Email envoyez avec succes...")
            # query = """    INSERT INTO auth_user (password, last_login, is_superuser, username,  first_name, last_name , email, is_staff, is_active, date_joined )
            #                  VALUES (%s, %s, %d, %s, %s, %s, %s, %d,  %d, %s)
            #          """
            # cursor.execute(query, (pass1, date, userid, username, fname, lname, email, userid, userid, date))
            # results = cursor.fetchall()
        except:
            return render(request, "mainpage/inscription.html", {
                "errors": "Cet utilisateur est deja enregistre."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("indexpage"))
    else:
        return render(request, "mainpage/inscription.html")
    
def contact(request):
        template_name = "mainpage/contact.html"
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if subject == '':
            subject = "BitMasters Contact"

        if message and email :
            send_mail(
                subject,
                message,
                email,
                ['dioufm65@yahoo.com'],
                fail_silently=False,
            )
        messages.success(request, " Email envoyez avec succes...")

        return render(request, template_name)