from .models import BankDetails,PatientDetails,AddressDetails
from rest_framework import serializers




#BankDetails Model
class BankDetailsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankDetails
        fields = '__all__'


#Patient Model
class PatientModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDetails
        fields='__all__'
        

# AddressDetailsModel        
class AddressDetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressDetails
        fields = '__all__'        