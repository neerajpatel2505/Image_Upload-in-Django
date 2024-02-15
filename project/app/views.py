from django.shortcuts import render
from .forms import RegistartionForm
from .models import RegistrationModel

# Create your views here.
def home(request):
    if request.method=="POST":
        form = RegistartionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = RegistartionForm()
    return render(request,'app/home.html',{'form':form})

def show(request):
    data = RegistrationModel.objects.all()
    return render(request,'app/show.html',{'data':data})