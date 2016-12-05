from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from newbie.models import UsrContext, team

def main(request):
    return render(request, "html/main.html")

def pato(request):
    usr=UsrContext.objects.all().order_by('-pato')
    usr1=usr[0]
    usr2=usr[1]
    usr3=usr[2]
    usr4=usr[3]
    usr5=usr[4]
    ctx = { 
        "god" : usr1,
        "king" : usr2,
        "legend" : usr3,
        "normal" : usr4,
        "weak" : usr5
    }
    return render(request, "html/GanzapE.html", ctx)

def mypage(request):
    return render(request, "html/mypage.html")
def timetable(request):
    T = team.objects.all()
    ctx = { "teams" : T}
    return render(request, "html/timetable.html", ctx)

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
    	    login(request, user)
	    return redirect('/main')
    return render(request, "html/login.html")

def user_logout(request):
    if request.user.is_authenticated():
        logout(request)
    return redirect('/')

def user_signup(request):
    if request.method == 'POST':
	user = request.POST
	User.objects.create_user(username=user['username'], password=user['password'], first_name=user['first_name'], last_name=user['last_name'])
        UsrContext(name=(user['last_name']+user['first_name']), username=user['username'], pato=0, phone=user['phone']).save()
        return redirect('/')
    return render(request, "html/signup.html")

def submit1(request):
    if request.method == 'POST':
  #     timevalue = request.POST['timevalue']
        print('fuck')
        usr=UsrContext.objects.get(username=request.user.get_username())
        kingname = usr.name
        kinguser = usr.username
        kingpato = usr.pato
        kingphone = usr.phone
        destination = 'station'
        startT = request.POST['timevalue']
        team(kingname=kingname, kinguser=kinguser, kingpato=kingpato, kingphone=kingphone, startT=startT, destination=destination).save()
    
    T = team.objects.all()
    ctx = { "teams" : T}
    return render(request, "html/timetable.html", ctx)

def submit2(request):
    if request.method == 'POST':
  #      timevalue = request.POST['timevalue']
        print('fuck')
        usr=UsrContext.objects.get(username=request.user.get_username())
        kingname = usr.name
        kinguser = usr.username
        kingpato = usr.pato
        destination = 'bus1'
        kingphone = usr.phone
        startT = request.POST['timevalue']
        team(kingname=kingname, kinguser=kinguser, kingpato=kingpato, kingphone=kingphone, startT=startT, destination=destination).save()
    #return render(request, "html/timetable.html")

    T = team.objects.all()
    ctx = { "teams" : T}
    return render(request, "html/timetable.html", ctx)

def submit3(request):
    if request.method == 'POST':
  #      timevalue = request.POST['timevalue']
        print('fuck')
        usr=UsrContext.objects.get(username=request.user.get_username())
        kingname = usr.name
        kinguser = usr.username
        kingpato = usr.pato
        kingphone = usr.phone
        destination = 'bus2'
        startT = request.POST['timevalue']
        team(kingname=kingname, kinguser=kinguser, kingpato=kingpato, kingphone=kingphone, startT=startT, destination=destination).save()
#    return render(request, "html/timetable.html")

    T = team.objects.all()
    ctx = { "teams" : T}
    return render(request, "html/timetable.html", ctx)


# Create your views here.
