from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, render_to_response

# Create your views here.
from addnew.models import add,Message
from addnew.forms import addform,MessageForm
import datetime

from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/index')
    return render_to_response('smssender/login.html', context_instance=RequestContext(request))

@login_required(login_url='/login/')

def logout_user(request):
    logout(request)
    return render_to_response('smssender/login.html', context_instance=RequestContext(request))

def indexview(request):

    now=datetime.datetime.now()
    date=str(now.date())
    time=str(now.hour)+":"+str(now.minute)+":"+str(now.second)

    if request.method == 'POST':


        form1 = MessageForm(request.POST)
        if form1.is_valid():
            users=add.objects.all()
            nmessage=form1.cleaned_data.get('message')
            for user in users:
                my_model= Message()
                my_model.message= nmessage
                my_model.sentTo=user.mobile
                my_model.name=user.fname
                my_model.date=date
                my_model.time=time
                my_model.save()

        return redirect(indexview)




    else:

        form1=MessageForm()
        users=add.objects.all()
        context_data={'users':users,'form1':form1}
        return render(request,'smssender/index.html',context_data)

def delete(request, id):
    stock_to_delete = get_object_or_404(add, pk=id).delete()
    return redirect(indexview)

def edit(request, id):
    user = get_object_or_404(add, pk=id)
    if request.method == 'POST':

        form = addform(request.POST)
        if form.is_valid():


            user.fname = form.cleaned_data.get('fname')
            user.mobile = form.cleaned_data.get('mobile')

            user.email = form.cleaned_data.get('email')
            user.dob = form.cleaned_data.get('dob')
            user.marriageaniversary = form.cleaned_data.get('marriageaniversary')
            user.remarks = form.cleaned_data.get('remarks')

            user.save()
        return redirect(indexview)
    else:
        form = addform()

        context_data = {'form': form,'user':user}
        return render(request,'smssender/edit.html',context_data)

def smsview(request):
    now=datetime.datetime.now()
    date=str(now.date())
    time=str(now.hour)+":"+str(now.minute)+":"+str(now.second)
    if request.POST:
        my_model= Message()
        my_model.message= request.POST['message']
        my_model.sentTo=request.POST['mobile']
        my_model.name=request.POST['name']
        my_model.date=date
        my_model.time=time
        my_model.save()
        msg="Your message has been successfully sent."
        context_data={'msg':msg}
        return render(request,'smssender/sms.html',context_data)


    else:
        msg=""
        context_data={'msg':msg}
        return render(request,'smssender/sms.html',context_data)


def apikeyview(request):

    return render(request,'smssender/key.html')


def notifyview(request):
    users=Message.objects.all()

    return render(request,'smssender/notify.html',{'users':users})

def adduserview(request):

    if request.method == 'POST':

        form = addform(request.POST)
        if form.is_valid():

            my_model = add()
            my_model.fname = form.cleaned_data.get('fname')
            my_model.mobile = form.cleaned_data.get('mobile')
            my_model.email = form.cleaned_data.get('email')
            my_model.dob = form.cleaned_data.get('dob')
            my_model.marriageaniversary = form.cleaned_data.get('marriageaniversary')
            my_model.remarks = form.cleaned_data.get('remarks')

            my_model.save()
        return redirect(indexview)

    else:

        form = addform()
        context_data = {'form': form}
        return render(request,'smssender/add.html', context_data)


def changepassword(request,user):
    if request.POST:
        u=User.objects.get(username=user)

        newpass=request.POST['newpass']
        confpass=request.POST['confpass']

        if newpass!=confpass:
            msg="The two passwords does not match"
            return render(request,'smssender/password.html',{'msg':msg})

        u.set_password(newpass)
        u.save()
        msg="Password changed successfully"
        return render(request,'smssender/password.html',{'msg':msg})

    else:
        msg=""
        return render(request,'smssender/password.html',{'msg':msg})
