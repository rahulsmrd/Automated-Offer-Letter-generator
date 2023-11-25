from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import get_user
from django.views.generic import (TemplateView,
                                  ListView,DetailView,
                                  CreateView,UpdateView,)
from home.models import *
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template

# Create your views here.

@login_required
def index(request):
    context={}
    if request.user.is_authenticated:
        if request.user.is_superuser:
            all_offerletters=offerletter_data.objects.all().order_by('pk')
            context={'offerletters':all_offerletters}
        else:
            all_offerletters=offerletter_data.objects.filter(email=request.user.email)
            context={'offerletters':all_offerletters}
    return render(request, 'home/offerletter_data_list.html',context)

@login_required
def create_offerletter(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        course=request.POST.get('course')
        join_date=request.POST.get('start_date')
        end_date=request.POST.get('end_date')
        unique_code=generator()
        date_of_creation=datetime.date.today()
        ins=offerletter_data(full_name=name, email=email, course=course, join_date=join_date, end_date=end_date, unique_code=unique_code,date_of_creation=date_of_creation,)
        ins.save()
        send_offerletter(email)
        return redirect('home:start')

    return render(request,"home/offerletter_data_form.html", {'data':{'unique_code':generator()}})

@login_required
def update_offerletter(request,pk):
    k=offerletter_data.objects.filter(pk=pk).values()
    k_update=offerletter_data.objects.get(pk=pk)
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        course=request.POST.get('course')
        join_date=request.POST.get('start_date')
        end_date=request.POST.get('end_date')
        unique_code=request.POST.get('unique_code')
        k_update.full_name,k_update.email,k_update.course,k_update.join_date,k_update.end_date,k_update.unique_code=name,email,course,join_date,end_date,unique_code
        k_update.save()
    return render(request,"home/offerletter_data_form.html",{'data':k[0],'update':True})


import datetime
def generator():
        #sfurid20231106001

    curr=str(datetime.date.today())
    s=curr.split('-')
    required_string=s[0]+s[1]+s[2]
    k=offerletter_data.objects.last()
    if not k:
        unique_code="SFURID20231106001"
    else:
        unique_code=str(k.unique_code)
    if unique_code[6:14]==required_string:
        num=int(unique_code[14:17])
        new_num=str(num+1)
        if len(new_num)==1:
            new_num='00'+new_num
        elif len(new_num)==2:
            new_num='0'+new_num
        new_code=unique_code[0:14]+new_num
    else:
        new_code=unique_code[0:6]+required_string+'000'
    return new_code

const={0:0,1:0,2:0}

import random
def otp_generator():
    if const[0]==0:
        const[1]=random.randint(10000,99999)
        const[0]=1
    elif const[0]==1:
        const[2]=random.randint(10000,99999)
        const[0]=0
    return const

def conformation(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        k=offerletter_data.objects.filter(email=email).values()
        if len(k) == 0:
            return HttpResponse('Please enter valid email address')
        return redirect('home:otp',pk=k[0]['id'])
    return render(request,"home/conform_page.html")


def otp(request,pk):
    k=offerletter_data.objects.filter(pk=pk).values()
    context={}
    context['for_otp']=True
    context['email']=k[0]['email']
    if request.method == 'POST':
        otp=request.POST.get('otp')
        if otp == str(const[1]):
            return redirect('home:preview',pk=pk)
        else:
            return HttpResponse('Please Enter Correct OTP sent to your Given Mail Id')
    otp_fg=otp_generator()
    j='OTP is '+str(otp_fg[1])

    subject ="Your One Time Password for accessing Offere Letter !!!"

    html_message = render_to_string('home/otp.html',{'otp':const[1],})
    plain_message = strip_tags(html_message)


    from_mail=settings.EMAIL_HOST_USER
    recipent=[k[0]['email']]

    message=EmailMultiAlternatives(
        subject=subject,
        body=plain_message,
        from_email=from_mail,
        to=recipent,
    )
    message.attach_alternative(html_message,"text/html")
    message.send()
    return render(request,"home/conform_page.html",context=context)

from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send(request,pk):
    k=offerletter_data.objects.filter(pk=pk).values()
    send_offerletter(k[0]['email'])
    return redirect('home:start')

def send_offerletter(email):
    
    subject ="Congratulations Your Offerletter is here !!!"


    html_message = render_to_string('home/message.html')
    plain_message = strip_tags(html_message)


    from_mail=settings.EMAIL_HOST_USER
    recipent=[email]

    message=EmailMultiAlternatives(
        subject=subject,
        body=plain_message,
        from_email=from_mail,
        to=recipent,
    )
    message.attach_alternative(html_message,"text/html")
    message.send()


def preview(request,pk):
    context=offerletter_data.objects.filter(pk=pk).values()
    return render(request,'home/preview_offerletter.html',context=context[0])