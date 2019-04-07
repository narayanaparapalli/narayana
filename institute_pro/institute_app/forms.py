from django import forms
from multiselectfield import MultiSelectFormField

class Contact_form(forms.Form):
    name=forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your name'
            }
        )
    )

    mobile=forms.IntegerField(
        label="enter mobile number",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'your mobile'
            }
        )
    )

    email=forms.EmailField(
        label="enter your mail ID",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'your mail Id'
            }


        )
    )

    COURSE_CHOICES = (
        ('py', 'Python'),
        ('dj', 'django'),
        ('UI', 'UI'),
        ('api', 'Rest API')
    )

    cource=MultiSelectFormField(max_length=100, choices=COURSE_CHOICES)

    LOCATION_CHOICES = (
        ('hyd', 'Hyderabad'),
        ('bang', 'Bangalore'),
        ('pune', 'Pune'),
        ('chenni', 'chenni')
    )

    locations = MultiSelectFormField(max_length=100, choices=LOCATION_CHOICES)

    SHIFT_CHOICES = (
        ('mng', 'Morning'),
        ('aftnoon', 'AfterNoon'),
        ('evng', 'Evining'),
        ('night','night')
    )

    shifts = MultiSelectFormField(max_length=100, choices=SHIFT_CHOICES)


class InstFeedback_form(forms.Form):
     name=forms.CharField(
         label="Enter your name",
         widget=forms.TextInput(
             attrs={
                 'class':'form-control',
                 'placeholder':'your name'
             }

         )
     )

     rating=forms.IntegerField(
         label='enter your rating',
         widget=forms.NumberInput(
             attrs={
                 'class':'form-control',
                 'placeholder':'your rating'
             }
         )
     )

     feedback=forms.CharField(
         label="enter your feedback",
         widget=forms.Textarea(
             attrs={
                 'class':'form-control',
                 'placeholder':'your feedback'
             }
         )
     )