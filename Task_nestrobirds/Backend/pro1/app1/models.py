from django.db import models

class PatientDetails(models.Model):
    patient_code = models.CharField(max_length=50, default='')
    patient_first_name = models.CharField(max_length=50)
    patient_last_name = models.CharField(max_length=50)
    patient_middle_name = models.CharField(max_length=50, blank=True, null=True)  
    
    MARITAL_STATUS =[
        ('married','married'),
        ('unmarried','unmarried'),
        ('divorced','divorced'),
        ('widow','widow')
    ]
    GENDER =[
        ('male','male'),
        ('female','female'),
        ('trans','trans')
    ]
    patient_age = models.PositiveIntegerField()
    patient_weight = models.FloatField()
    patient_height = models.PositiveIntegerField()
    patient_marital_status = models.CharField(max_length=20,choices=MARITAL_STATUS,default='unmarried')
    patient_gender = models.CharField(max_length=10, choices=GENDER)
    patient_is_handicap = models.BooleanField(default=False)
    patient_date_of_birth = models.DateField()
    patient_occupation = models.CharField(max_length=50, blank=True, null=True)
    patient_aadhar_card_number = models.CharField(max_length=16)
    
    
   

    
    

class BankDetails (models.Model):
    bank_details_identifier = models.BigAutoField(primary_key=True)
    pancard_number = models.CharField(max_length=10)
    account_number = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=50)
    branch_name = models.CharField(max_length=30)
    ifsc_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.account_number}"




class AddressDetails(models.Model):                
    addpatients_details_id = models.BigAutoField(primary_key=True)
    addpatients_linel = models.CharField(max_length=50)
    addpatients_line2 = models.CharField(max_length=59)
    landmark = models.CharField(max_length=50)
    area = models.CharField(max_length=30)
    town = models.CharField(max_length=38)
    city= models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    pincode = models.IntegerField()

    def __str__(self):
        return f"{self.city}"


    

