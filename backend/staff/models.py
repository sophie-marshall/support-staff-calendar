from django.db import models
import uuid
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class StaffMember(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class StaffAvailability(models.Model):

    SUNDAY_CLASSES = [
        ("9:00AM", "9:00AM"), 
        ("10:00AM", "10:00AM"), 
    ]

    MONDAY_CLASSES = [
        ("6:00AM", "6:00AM"), 
        ("7:00AM", "7:00AM"), 
        ("8:00AM", "8:00AM"), 
        ("12:00PM", "12:00PM"),
        ("5:00PM", "5:00PM"), 
        ("6:30PM", "6:30PM") 
    ]

    TUESDAY_CLASSES = [
        ("6:00AM", "6:00AM"), 
        ("7:00AM", "7:00AM"), 
        ("8:00AM", "8:00AM"), 
        ("12:00PM", "12:00PM"),
        ("5:00PM", "5:00PM"), 
        ("6:30PM", "6:30PM") 
    ]

    THURSDAY_CLASSES = [
        ("6:00AM", "6:00AM"), 
        ("7:00AM", "7:00AM"), 
        ("8:00AM", "8:00AM"), 
        ("12:00PM", "12:00PM"),
        ("5:00PM", "5:00PM"), 
        ("6:30PM", "6:30PM") 
    ]

    WEDNESDAY_CLASSES = [
        ("6:00AM", "6:00AM"), 
        ("7:00AM", "7:00AM"), 
        ("12:00PM", "12:00PM"),
        ("5:00PM", "5:00PM"), 
        ("6:30PM", "6:30PM") 
    ]

    FRIDAY_CLASSES = [
        ("6:00AM", "6:00AM"), 
        ("7:00AM", "7:00AM"), 
        ("12:00PM", "12:00PM"),
        ("5:00PM", "5:00PM"), 
        ("6:30PM", "6:30PM") 
    ]

    SATURDAY_CLASSES = [
        ("8:30AM", "8:30AM"), 
        ("10:00AM", "10:00AM"), 
    ]

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    staff_member_id = models.ForeignKey(
        StaffMember, 
        on_delete=models.CASCADE, 
        to_field='uuid', 
        db_column='staff_member_id'
    )
    sunday = ArrayField(models.CharField(max_length=10, choices=SUNDAY_CLASSES), blank=True, null=True)
    monday = ArrayField(models.CharField(max_length=10, choices=MONDAY_CLASSES), blank=True, null=True)
    tuesday = ArrayField(models.CharField(max_length=10, choices=TUESDAY_CLASSES), blank=True, null=True)
    wednesday = ArrayField(models.CharField(max_length=10, choices=WEDNESDAY_CLASSES), blank=True, null=True)
    thursday = ArrayField(models.CharField(max_length=10, choices=THURSDAY_CLASSES), blank=True, null=True)
    friday = ArrayField(models.CharField(max_length=10, choices=FRIDAY_CLASSES), blank=True, null=True)
    saturday = ArrayField(models.CharField(max_length=10, choices=SATURDAY_CLASSES), blank=True, null=True)
    

    @property
    def staff_member_name(self):
         return f"{self.staff_member_id.first_name} {self.staff_member_id.last_name}"
    
    def __str__(self):
        return f"{self.staff_member_id.first_name} {self.staff_member_id.last_name}'s Availability"



