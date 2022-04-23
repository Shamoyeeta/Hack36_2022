from rest_framework.generics import ListAPIView, CreateAPIView
from server.models import Person, Items_listed, borrower
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView
from django.shortcuts import render
from django.db import connection
from rest_framework.response import Response
from rest_framework.decorators import api_view

from server.models import Person, Items_listed,borrower
# from server.serializers import ItemSerializer

from .serializer import (createPersonSerializer, listPersonSerializer, listListSerializer, updateListSerializer,
                         createListSerializer, listBorrowerSerializer, createBorrowerSerializer)


class listPersonAPIView(ListAPIView):
    serializer_class = listPersonSerializer
    queryset = Person.objects.all()

    def get_queryset(self):
        print(self.request.user.username)
        return Person.objects.filter(username=self.request.user.username)


class createPersonAPIView(CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = createPersonSerializer


class listListAPIView(ListAPIView):
    serializer_class = listListSerializer
    queryset = Person.objects.all()

    def get_queryset(self):
        print(self.request.user.username)
        return Person.objects.filter(username=self.request.user.username)


class createListAPIView(CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = createListSerializer


class updateListAPIView(RetrieveUpdateAPIView):
    # permission_classes = import_string_list(drfr_settings.PROFILE_PERMISSION_CLASSES)
    queryset = Items_listed.objects.all()
    serializer_class = updateListSerializer
    lookup_field = 'username'


class listborrowAPIView(ListAPIView):
    serializer_class = listBorrowerSerializer
    queryset = borrower.objects.all()

    def get_queryset(self):
        print(self.request.user.username)
        return borrower.objects.filter(username=self.request.user.username)


class createBorrowAPIView(CreateAPIView):
    queryset = borrower.objects.all()
    serializer_class = createBorrowerSerializer


# @api_view(['GET'])
# def getData(request):
#     personal_data= Person.objects.get()
#     serializer= ItemSerializer(personal_data)
#     return Response(serializer.data)

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return render(request,'home')

#@login_required
def personal_info(request):
    if request.method=="POST":
        form = Person(request.POST)
        if form.is_valid():
            details= Person(id= request.Aadhar_id, name=request.name, address= request.address, phone= request.phone_no)
            details.save()

    # else:
        #    form =


def items_posted(request):
    if request.method=="POST":
        form = Items_listed(request.POST)
        if form.is_valid():
            details= Items_listed(id= request.Aadhar_id, name=request.name, address= request.address, phone= request.phone_no)
            details.save()

        #else:
         #   form =


def customer(request):
    with connection.cursor() as cursor:
        query= "SELECT Aadhar_id,email,name, address, phone_no FROM Person where lender_id= user.request.Aadhar_id"
        cursor.execute(query)
        row = cursor.fetchone()



def seller(reqest):
    with connection.cursor() as cursor:
        query= "SELECT item_id,name, description FROM Items_listed where lender_id= user.request.Aadhar_id"
        cursor.execute(query)
        row = cursor.fetchone()
        all_count, yes_count = row

def items_available(reqest):
    with connection.cursor() as cursor:
        query= "SELECT item_id,name, description, loaction, price status FROM Items_listed"
        cursor.execute(query)
        row = cursor.fetchone()
        all_count, yes_count = row


def borrowed(reqest):
    with connection.cursor() as cursor:
        query= "SELECT item_id,name, borrow_date, return_date, amount FROM borrower where borrow_id= user.request.Aadhar_id"
        cursor.execute(query)
        row = cursor.fetchone()
        all_count, yes_count = row


def itembyname(request):
    with connection.cursor() as cursor:
        query= "SELECT borrower.item_id, name, amount, FROM borrower,Items_listed where name=user.request.name AND borrower.item_id=Items_listed.item_id"
        cursor.execute(query)
        row = cursor.fetchone()
        all_count, yes_count = row

