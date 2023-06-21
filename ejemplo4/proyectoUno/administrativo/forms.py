from django.forms import ModelForm
from administrativo.models import Estudiante
from administrativo.models import NumeroTelefonico


class EstudianteForm(ModelForm): 
    class Meta:
        model = Estudiante 
        fields = ['nombre', 'apellido', 'cedula'] 




