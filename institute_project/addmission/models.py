from django.db import models
from django.urls import reverse


# Create your models here.
class addmission_details(models.Model):
    student=models.ForeignKey('student.student_personal_info',on_delete=models.CASCADE, related_name="addmissions")
    date_of_addmission=models.DateField()
    course=models.OneToOneField('course.course_master',on_delete=models.CASCADE,related_name="addmissions")
    start_time=models.TimeField()
    end_time=models.TimeField()
    #receipt_id_or_object_of_payment_details=models.IntegerField()
    start_date=models.DateField()
    end_date=models.DateField()
    scan_copy_of_id_proof=models.FileField(upload_to='documents')
    fees=models.IntegerField()
    status=models.CharField(max_length=10,choices=[('Active','Active'),('Deactive','Deactive'),('Close','Close')])
    no_of_days=models.IntegerField()
    remarks=models.CharField(max_length=20)
    #addmission_timing_table_id=models.IntegerField()
    pending_fees=models.IntegerField()

    def __str__(self):
        return f"{self.student_id}"

    def get_absolute_url(self):
        return reverse('addmission-view')

