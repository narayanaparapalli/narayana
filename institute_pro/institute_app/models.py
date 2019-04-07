from django.db import models
from multiselectfield import MultiSelectField

# this modal class
class InstContact_Data(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=100)


    COURSE_CHOICES=(
        ('py','Python'),
        ('dj','django'),
        ('UI','UI'),
        ('api','Rest API')
    )
    cources=MultiSelectField(max_length=200,choices=COURSE_CHOICES)


    LOCATION_CHOICES=(
        ('hyd','Hyderabad'),
        ('bang','Bangalore'),
        ('pune','Pune'),
        ('chenni','chenni')
    )

    locations=MultiSelectField(max_length=200,choices=LOCATION_CHOICES)


    SHIFT_CHOICES=(
        ('mng','Morning'),
        ('aftnoon','Afternoon'),
        ('evng','Evining'),
        ('night','night')
    )

    shifts=MultiSelectField(max_length=200,choices=SHIFT_CHOICES)



class InstFeedback_Data(models.Model):
    name=models.CharField(max_length=100)
    rating=models.IntegerField()
    date=models.DateField()
    feedback=models.TextField(max_length=1000)
