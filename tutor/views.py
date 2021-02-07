from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from .models import User,Class,Connect,Connect_Message,Connect_Message_Attach, Reports, TicketStat
from .serializers import UserSerializer,ClassSerializer,ConnectSerializer,CnctMsgSerializer,CMAttachSerializer, supportTrack, ReportsSerializer
from django import template
# Create your views here.


# HomePage
def home(request):
    return render( request , 'home.html')

# LoginPage
def login(request):
    return render( request , 'login.html')

# User Table
@api_view(['GET','POST','PUT','DELETE'])
def user_api(request,pk=None):
    if request.method =='GET':
        id = pk
        if id is not None:
            usr = User.objects.get(user_id=id)
            serializer= UserSerializer(usr)
            return Response(serializer.data)
        usr= User.objects.all()
        serializer=UserSerializer(usr,many=True)
        return Response(serializer.data)

    if request.method== 'POST':
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Create'})
        return Response(serializer.errors)

    if request.method=='PUT':
        id = pk
        usr = User.objects.get(user_id=id)
        serializer= UserSerializer(usr,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors)

    if request.method== 'DELETE':
        id = pk
        usr= User.objects.get(user_id=id)
        usr.delete()
        return Response({'msg':'Data deleted'})

@api_view(['GET','POST','PUT'])
def task(request):
    if request.method == 'GET':
        usr = User.objects.all()
        serializer = UserSerializer(usr,many=True)
        return Response(serializer.data)

    if request.method== 'POST':
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Create'})
        return Response(serializer.errors)

    if request.method=='PUT':
        id = request.data.get('user_id')
        usr = User.objects.get(user_id=id)
        serializer= UserSerializer(usr,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)

# Class table

@api_view(['GET', 'POST', 'DELETE'])
def class_api(request,pk=None):
    if request.method =='GET':
        id = pk
        if id is not None:
            Clss = Class.objects.get(class_id=id)
            serializer= ClassSerializer(Clss)
            return Response(serializer.data)
    if request.method == 'POST':
        serializer = Class.objects.get(data=request.data)
        print(serializer)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response({'msg': 'Created'})
        # return Response(serializer.errors)


    if request.method== 'DELETE':
        id = pk
        clss= Class.objects.get(class_id=id)
        #serializer = ClassSerializer(clss)
        #return Response(serializer.data)
        clss.delete()
        return Response({'msg':'Data deleted'})




@api_view(['GET','POST','PUT'])
def class_task(request):
    if request.method == 'GET':
        clss = Class.objects.all()
        serializer = ClassSerializer(clss,many=True)
        return Response(serializer.data)

    if request.method== 'POST':
        serializer=ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Create'})
        return Response(serializer.errors)

    if request.method=='PUT':
        id = request.data.get('class_id')
        clss = Class.objects.get(class_id=id)
        serializer= ClassSerializer(clss,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)

#Connect table

@api_view(['GET','DELETE'])
def connect_api(request,pk=None):
    if request.method =='GET':
        id = pk
        if id is not None:
            cnct = Connect.objects.get(connect_id=id)
            serializer= ConnectSerializer(cnct)
            return Response(serializer.data)

    if request.method== 'DELETE':
        id = pk
        cnct= Connect.objects.get(connect_id=id)
        #serializer = ConnectSerializer(cnct)
        #return Response(serializer.data)
        cnct.delete()
        return Response({'msg':'Data deleted'})



@api_view(['GET','POST','PUT'])
def connect_task(request):
    if request.method == 'GET':
        cnct = Connect.objects.all()
        serializer = ConnectSerializer(cnct,many=True)
        return Response(serializer.data)

    if request.method== 'POST':
        serializer=ConnectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Create'})
        return Response(serializer.errors)

    if request.method=='PUT':
        id = request.data.get('connect_id')
        cnct = Connect.objects.get(connect_id=id)
        serializer= ConnectSerializer(cnct,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)

#Connect_Massage Table
@api_view(['GET','DELETE'])
def connect_msgapi(request,pk=None):
    if request.method =='GET':
        id = pk
        if id is not None:
            cnctmsg = Connect_Message.objects.get(connect_message_id=id)
            serializer= CnctMsgSerializer(cnctmsg)
            return Response(serializer.data)

    if request.method== 'DELETE':
        id = pk
        cnctmsg= Connect_Message.objects.get(connect_message_id=id)
        #serializer = CnctMsgSerializer(cnctmsg)
        #return Response(serializer.data)
        cnctmsg.delete()
        return Response({'msg':'Data deleted'})



@api_view(['GET','POST','PUT'])
def connect_msgtask(request):
    if request.method == 'GET':
        cnctmsg = Connect_Message.objects.all()
        serializer = CnctMsgSerializer(cnctmsg,many=True)
        return Response(serializer.data)

    if request.method== 'POST':
        serializer=CnctMsgSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Create'})
        return Response(serializer.errors)

    if request.method=='PUT':
        id = request.data.get('connect_message_id')
        cnctmsg = Connect_Message.objects.get(connect_message_id=id)
        serializer= CnctMsgSerializer(cnctmsg,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)

# Connect_message_attach

@api_view(['GET','DELETE'])
def connect_msg_Attachapi(request,pk=None):
    if request.method =='GET':
        id = pk
        if id is not None:
            cma = Connect_Message_Attach.objects.get(id=id)
            serializer= CMAttachSerializer(cma)
            return Response(serializer.data)

    if request.method=='DELETE':
        id = pk
        cma= Connect_Message_Attach.objects.get(id=id)
        #serializer = CMAttachSerializer(cma)
        #return Response(serializer.data)
        cma.delete()
        return Response({'msg':'Data deleted'})



@api_view(['GET','POST','PUT'])
def connect_msg_attachtask(request):
    if request.method == 'GET':
        cma = Connect_Message_Attach.objects.all()
        serializer = CMAttachSerializer(cma,many=True)
        return Response(serializer.data)

    if request.method== 'POST':
        serializer=CMAttachSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Create'})
        return Response(serializer.errors)

    if request.method=='PUT':
        id = request.data.get('connect_message_id')
        cma = Connect_Message_Attach.objects.get(connect_message_id=id)
        serializer= CMAttachSerializer(cma,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)

#creating classes
def create_class(request):
    if request.method == 'POST':
        name = request.POST['title']
        desc = request.POST['desc']

        new_class = Class(class_name=name, class_details=desc)
        new_class.save()

        context = {'class_name': name, 'class_desc': desc}
        return render(request, 'my_classes.html', context)
    else:
        return render(request, 'create_class.html')

#Support
def my_ticket(request):
    if request.method == 'POST':
        # tk_details = request.POST['details']
        # tk_choices = request.POST.get('javascript', 'python')
        # tk_desc = request.POST['desc']

        # new_tk = TicketStat(ticket_details=tk_details, category=tk_choices, ticket_desc=tk_desc)
        # new_tk.save()

        # context = {'user_id': TicketStat.ticket_id}

        return render(request, 'my_tik.html')
    else:
        return render(request, 'support.html')


# List of all support
@api_view(['GET', 'POST', 'PUT'])
def my_ticket_view(request):
    if request.method =='GET':
        usr= TicketStat.objects.all()
        serializer=supportTrack(usr)
        return Response(serializer.data)
    if request.method== 'POST':
        serializer=supportTrack(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Create'})
        return Response(serializer.errors)

    if request.method == 'PUT':
        token = request.method.get('ticket_id')
        trans = TicketStat.objects.get(ticket_id=token)
        serializer = supportTrack(trans, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Report Updated'})
        return Response(serializer.errors)

#List of user<id> support
@api_view(['GET','PUT'])
def my_ticket_view_api(request,pk=None):
    if request.method =='GET':
        id = pk
        if id is not None:
            usr = TicketStat.objects.get(user_id=id)
            serializer= supportTrack(usr)
            return Response(serializer.data)
        usr= TicketStat.objects.all()
        serializer=supportTrack(usr,many=True)
        return Response(serializer.data)

    if request.method=='PUT':
        id = pk
        usr = TicketStat.objects.get(user_id=id)
        serializer= supportTrack(usr,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors)

# List of individual Report user<id>
@api_view(['GET'])
def my_report_api(request,pk=None):
    if request.method =='GET':
        id = pk
        if id is not None:
            usr = Reports.objects.get(user_id=id)
            serializer= ReportsSerializer(usr)
            return Response(serializer.data)
        usr= Reports.objects.all()
        serializer=ReportsSerializer(usr,many=True)
        return Response(serializer.data)

    # if request.method== 'POST':
    #     serializer=ReportsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg':'Data Create'})
    #     return Response(serializer.errors)
    #
    # if request.method=='PUT':
    #     id = pk
    #     usr = Reports.objects.get(user_id=id)
    #     serializer= ReportsSerializer(usr,data=request.data,partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response(serializer.errors)

# All Reports Table
@api_view(['GET'])
def my_reports(request):
    if request.method == 'GET':
        transactions = Reports.objects.all()
        serializer = ReportsSerializer(transactions, many=True)
        return Response(serializer.data)
    # if request.method == 'POST':
    #     serializer = ReportsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg': 'New Report Created'})
    # if request.method == 'PUT':
    #     id = request.method.get('report_id')
    #     transactions = Reports.objects.get(report_id=id)
    #     serializer = ReportsSerializer(transactions, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg':'Report Updated'})
    #     return Response(serializer.errors)
