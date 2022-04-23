from rest_framework.serializers import ModelSerializer
from server.models import Person, Items_listed, borrower
from django.contrib.auth.models import User


class createPersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = ('Aadhar_id','email', 'password', 'name', 'address', 'phone_no')


class listPersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = ('Aadhar_id','email', 'password', 'name', 'address', 'phone_no')


class createListSerializer(ModelSerializer):
    class Meta:
        model = Items_listed
        fields = ('lender_id', 'Item_id', 'name', 'description', 'price', 'location', 'status')


class listListSerializer(ModelSerializer):
    class Meta:
        model = Items_listed
        fields = ('lender_id', 'Item_id', 'name', 'description', 'price', 'location', 'status')


class updateListSerializer(ModelSerializer):
    class Meta:
        model = Items_listed
        fields = ('lender_id', 'Item_id', 'name', 'description', 'price', 'location', 'status')


class createBorrowerSerializer(ModelSerializer):
    class Meta:
        model = borrower
        fields = ('item_id', 'borrower_id', 'amount', 'borrowDate', 'returnDate')


class listBorrowerSerializer(ModelSerializer):
    class Meta:
        model = borrower
        fields = ('item_id', 'borrower_id', 'amount', 'borrowDate', 'returnDate')
