from django.contrib import messages
from django.shortcuts import render
import mysql.connector




def post(request):
            connection = mysql.connector.connect(
                    host='localhost',
                    user='Moussa',
                    password='root123',
                    database='amadeus'
            )
        
            # cursor = connection.cursor()
    # if request.method == 'POST':
            name  = request.POST.get('nom')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            adr   = request.POST.get('adresse')
            date  = request.POST.get('date')
            pass1  = request.POST.get('password1')
            pass2  = request.POST.get('password2')
            vide  = '2020-01-01'
            with connection.cursor() as cursor:
                checkid = "SELECT * FROM Client WHERE telephone= %s AND email = %s"
                params = [phone, email]
                cursor.execute(checkid, params)
                results = cursor.fetchall()
                # for res in results:
                if (len(results)>0) :
                        messages.error(request, 'Cet utilisateur existe deja dans la base de Donnee')
                        return render(request, 'inscription/index.html')
                else :
                    if (pass1==pass2):
                        messages.error(request, 'Les mots de passes deonnees ne sont pas les memes')
                    query = """
                                    INSERT INTO Client (nomComplet, telephone, email, adresse,dernierTicketAchete, date_naissance, password1, password2)
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                            """
                cursor.execute(query, (name, phone, email, adr,vide, date, hash(pass1), hash(pass2) ))
                results = cursor.fetchall()
                context = {'results': results}
                connection.commit()
                connection.close()
                messages.success(request,'inscription Reussi')
                return render(request, 'inscription/index.html', context)


def mesreservations(request):
    return render(request, 'espaceClient/mesreservations.html')