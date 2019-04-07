from django.shortcuts import render
from .models import InstContact_Data,InstFeedback_Data
from .forms import InstFeedback_form,Contact_form
import datetime as dt
date1=dt.datetime.now()

# Create your views here.
def home_view(request):
    return render(request,'inst_home.html')

def contact_view(request):
    if request.method == "POST":
        cform=Contact_form(request.POST)
        if cform.is_valid():
            name=cform.cleaned_data.get('name','')
            mobile=cform.cleaned_data.get('mobile','')
            email=cform.cleaned_data.get('email','')
            course=cform.cleaned_data.get('cource','')
            locations=cform.cleaned_data.get('locations','')
            shifts=cform.cleaned_data.get('shifts','')

            data=InstContact_Data(
                name=name,
                mobile=mobile,
                email=email,
                cources=course,
                locations=locations,
                shifts=shifts,

            )
            data.save()
            cform=Contact_form()
            return render(request,'inst_contact.html',{'cform':cform})
    else:

        cform=Contact_form()
        return render(request,'inst_contact.html',{'cform':cform})

def services_view(request):
    return render(request,'inst_services.html')

def feedback_view(request):
    if request.method == "POST":
        fform=InstFeedback_form(request.POST)
        if fform.is_valid():
            name=request.POST.get('name','')
            rating=request.POST.get('rating','')
            feedback=request.POST.get('feedback','')

            data=InstFeedback_Data(
                name=name,
                rating=rating,
                date=date1,
                feedback=feedback
            )
            data.save()
            fform=InstFeedback_form()
            output=InstFeedback_Data.objects.all()
            return render(request,'inst_feedback.html',{'output':output,'fform':fform})
    else:
        fform = InstFeedback_form()
        output = InstFeedback_Data.objects.all()
        return render(request, 'inst_feedback.html', {'output': output, 'fform': fform})

def gallery_view(request):
    return render(request,'inst_galary.html')
