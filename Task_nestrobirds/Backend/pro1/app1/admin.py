from django.contrib import admin
from . models import BankDetails,AddressDetails, PatientDetails

@admin.register(AddressDetails)
class AdressDetailsAdmin(admin.ModelAdmin):
    list_display=['addpatients_details_id','addpatients_linel','addpatients_line2','landmark',
                  'area','town','city','state','pincode']


@admin.register(BankDetails)
class BankdetailsAdmin(admin.ModelAdmin):
    list_display=['pancard_number','account_number','bank_name','branch_name','ifsc_code']



@admin.register(PatientDetails)
class PateintAdmin(admin.ModelAdmin):
    list_display=['patient_first_name','patient_last_name',
                  'patient_middle_name','patient_age',
                  'patient_weight','patient_height','patient_marital_status','patient_gender',
                  'patient_is_handicap','patient_date_of_birth','patient_occupation','patient_aadhar_card_number',
                  'patient_code']