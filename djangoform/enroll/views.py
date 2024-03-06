from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def showformdata(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            contact=fm.cleaned_data['contact']
            country=fm.cleaned_data['country']
            city=fm.cleaned_data['city']
            print('Name:',name)
            print('Email:',email)
            print('Contact:',contact)
            print('Country:',country)
            print('City:',city)
            return render(request, 'enroll/success.html', {'nm':name})
        print(fm)
        print("Post request")

    else:
        fm=StudentRegistration()
        print("Get request")


    return render(request, 'enroll/userregistration.html', {'form':fm})
