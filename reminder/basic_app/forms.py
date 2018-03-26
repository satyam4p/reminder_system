from .models import truck
from django.forms import ModelForm


class truck_form(ModelForm):

    class Meta():
        model=truck
        fields=("truck_number","licance_id","licence_exp","fitness_id","fitness_exp")
