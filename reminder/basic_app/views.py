from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse
from .models import truck
import datetime
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse_lazy,reverse
from .forms import truck_form
from django.views.generic import CreateView,RedirectView
from django.contrib import messages
# Create your views here.

def index(request):
    data=truck.objects.all
    return render(request,"basic_app/index.html",context={"data":data})


#view for creating details of a truck*-
class createtruck(CreateView):
    model=truck
    form_class =truck_form
    success_url =reverse_lazy("truck list")


def truck_view(request,pk=None):
    truck_id=pk
    detail=get_object_or_404(truck,pk=pk)
    lic_date=detail.licence_exp
    fit_date=detail.fitness_exp
    rem_licence=(lic_date-datetime.date.today()).days
    rem_fitness=(fit_date-datetime.date.today()).days

    rem=1
    return render(request,"basic_app/details.html",context={"detail":detail,'truck_id':truck_id,
                                                            "days_rem_licence":rem_licence,"days_rem_fitness":rem_fitness,
                                                            "rem":rem})
def Read(request,pk=None):
    trucks=get_object_or_404(truck,pk=pk)
    if trucks.read is False:
        trucks.read = True
        trucks.save()

    data=truck.objects.all
    return render(request,'basic_app/index.html',context={'data':data})




