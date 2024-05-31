from django.shortcuts import render
from rest_framework.views import APIView
from .models import BankDetails,PatientDetails,AddressDetails
from .serializers import BankDetailsModelSerializer,PatientModelSerializer,AddressDetailModelSerializer
from rest_framework import status
from rest_framework.response import Response




class BankDetailsApiView(APIView):
        def get(self,request):
            bank=BankDetails.objects.all()
            serializer=BankDetailsModelSerializer(bank,many=True)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        
        def post(self,request):
              serializer=BankDetailsModelSerializer(data=request.data)
              if serializer.is_valid():
                    serializer.save()
                    return Response(data=serializer.data)
              return Response(data=serializer.errors)
        
class PatientApiView(APIView):
    def get(self,request):
        Patient = PatientDetails.objects.all()
        serializer = PatientModelSerializer(Patient,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = PatientModelSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(data=serializer.data)
        return Response(data=serializer.errors)
    


    
    
class AddressDetailsApiView(APIView):
     def get(self,request):
        Address = AddressDetails.objects.all()
        serializer = AddressDetailModelSerializer(Address,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
     
     def post(self,request):
        serializer = AddressDetailModelSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    
    
