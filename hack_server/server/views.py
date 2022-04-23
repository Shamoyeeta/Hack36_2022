from django.shortcuts import render
from django.db import connection
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ItemSerializer, Person
from .models import Person, Items_listed, borrower

@api_view(['GET'])
def getData(request):
    personal_data= Person.objects.get()
    serializer= ItemSerializer(personal_data)
    return Response(serializer.data)

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
            details.save();
            messages.success(request, f"New User Created")
       # else:
        #    form =


def items_posted(request):
    if request.method=="POST":
        form = Items_listed(request.POST)
        if form.is_valid():
            details= Items_listed(id= request.Aadhar_id, name=request.name, address= request.address, phone= request.phone_no)
            details.save();
            messages.success(request, f"New User Created")
        #else:
         #   form =



def seller(reqest):
    with connection.cursor() as cursor:
        query= "SELECT lender_id, item_id FROM Items_listed where lender_id= id_person"
        cursor.execute(query)
        row = cursor.fetchone()
        all_count, yes_count = row



