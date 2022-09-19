from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from doctor.views import appointments
from .models import chatMessages
from django.contrib.auth import get_user_model
from  hospital.models import User as UserModel
from hospital.models import Patient
from doctor.models import Doctor_Information  , Appointment  
from django.db.models import Q
import json,datetime
from django.core import serializers
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request,pk):
    if request.user.is_patient:
            User = get_user_model()
            users = User.objects.all()
            patients = Patient.objects.get(user_id=pk)
            #doctor = Doctor_Information.objects.all()
            appointments = Appointment.objects.filter(patient=patients).filter(appointment_status='confirmed')
            doctor= Doctor_Information.objects.filter(appointment__in=appointments)
            
            chats = {}
            if request.method == 'GET' and 'u' in request.GET:
                # chats = chatMessages.objects.filter(Q(user_from=request.user.id & user_to=request.GET['u']) | Q(user_from=request.GET['u'] & user_to=request.user.id))
                chats = chatMessages.objects.filter(Q(user_from=request.user.id, user_to=request.GET['u']) | Q(user_from=request.GET['u'], user_to=request.user.id))
                chats = chats.order_by('date_created')
                doc = Doctor_Information.objects.get(user_id=request.GET['u'])
                
                context = {
                "page":"home",
                "users":users,
                "chats":chats,
                "patient":patients,
                "doctor":doctor,
                "doc":doc,
                "app":appointments,
                
                "chat_id": int(request.GET['u'] if request.method == 'GET' and 'u' in request.GET else 0)
            }
            elif request.method == 'GET' and 'search' in request.GET:
                query = request.GET.get('search')
                doctor= Doctor_Information.objects.filter(Q(user__first_name__icontains=query) | Q(user__last_name__icontains=query))
                #chats = chatMessages.objects.filter(Q(user_from=request.user.id, user_to=request.GET['u']) | Q(user_from=request.GET['u'], user_to=request.user.id))
                #chats = chats.order_by('date_created')
                #doc = Doctor_Information.objects.get(username=request.GET['search'])
                context = {
                "page":"home",
                "users":users,
                
                "patient":patients,
                
                "doctor":doctor,
                
            }
            else:
            
            
                context = {
                    "page":"home",
                    "users":users,
                    "chats":chats,
                    "patient":patients,
                    "doctor":doctor,
                    "app":appointments,
                    "chat_id": int(request.GET['u'] if request.method == 'GET' and 'u' in request.GET else 0)
                }
            print(request.GET['u'] if request.method == 'GET' and 'u' in request.GET else 0)
            return render(request,"chat.html",context)
    elif request.user.is_doctor:
            User = get_user_model()
            users = User.objects.all()
            #patients = Patient.objects.all()
            doctor = Doctor_Information.objects.get(user_id=pk)
            appointments = Appointment.objects.filter(doctor=doctor).filter(appointment_status='confirmed')
            patients= Patient.objects.filter(appointment__in=appointments)

            chats = {}
            if request.method == 'GET' and 'u' in request.GET:
                # chats = chatMessages.objects.filter(Q(user_from=request.user.id & user_to=request.GET['u']) | Q(user_from=request.GET['u'] & user_to=request.user.id))
                chats = chatMessages.objects.filter(Q(user_from=request.user.id, user_to=request.GET['u']) | Q(user_from=request.GET['u'], user_to=request.user.id))
                chats = chats.order_by('date_created')
                pat = Patient.objects.get(user_id=request.GET['u'])
                
                context = {
                "page":"home",
                "users":users,
                "chats":chats,
                "patient":patients,
                "doctor":doctor,
                "pat":pat,
                "app":appointments,
                
                "chat_id": int(request.GET['u'] if request.method == 'GET' and 'u' in request.GET else 0)
            }
            elif request.method == 'GET' and 'search' in request.GET:
                query = request.GET.get('search')
                patients= Patient.objects.filter(Q(user__first_name__icontains=query) | Q(user__last_name__icontains=query))
                #chats = chatMessages.objects.filter(Q(user_from=request.user.id, user_to=request.GET['u']) | Q(user_from=request.GET['u'], user_to=request.user.id))
                #chats = chats.order_by('date_created')
                #doc = Doctor_Information.objects.get(username=request.GET['search'])
                context = {
                "page":"home",
                "users":users,
                
                "patient":patients,
                "app":appointments,
                "doctor":doctor,
                
            }
            
                
            
            else:
            
                context = {
                    "page":"home",
                    "users":users,
                    "chats":chats,
                    "patient":patients,
                    "doctor":doctor,
                    "chat_id": int(request.GET['u'] if request.method == 'GET' and 'u' in request.GET else 0)
                }
            print(request.GET['u'] if request.method == 'GET' and 'u' in request.GET else 0)
            return render(request,"chat-doctor.html",context)

@csrf_exempt
@login_required
def profile(request):
    context = {
        "page":"profile",
    }
    return render(request,"chat/profile.html",context)

@csrf_exempt
@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def get_messages(request):
    chats = chatMessages.objects.filter(Q(id__gt=request.POST['last_id']),Q(user_from=request.user.id, user_to=request.POST['chat_id']) | Q(user_from=request.POST['chat_id'], user_to=request.user.id))
    new_msgs = []
    for chat in list(chats):
        data = {}
        data['id'] = chat.id
        data['user_from'] = chat.user_from.id
        data['user_to'] = chat.user_to.id
        data['message'] = chat.message
        data['date_created'] = chat.date_created.strftime("%b-%d-%Y %H:%M")
        print(data)
        new_msgs.append(data)
    return HttpResponse(json.dumps(new_msgs), content_type="application/json")

@csrf_exempt
@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def send_chat(request):
    resp = {}
    User = get_user_model()
    if request.method == 'POST':
        post =request.POST
        
        u_from = User.objects.get(id=post['user_from'])
        u_to = User.objects.get(id=post['user_to'])
        insert = chatMessages(user_from=u_from,user_to=u_to,message=post['message'])
        try:
            insert.save()
            resp['status'] = 'success'
        except Exception as ex:
            resp['status'] = 'failed'
            resp['mesg'] = ex
    else:
        resp['status'] = 'failed'

    return HttpResponse(json.dumps(resp), content_type="application/json")




       