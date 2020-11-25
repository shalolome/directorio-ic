from django import forms
from .models import Persona, Especialidad, EstadoCivil

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        exclude = ('validacion',)
        widgets = {'fecha_nacimiento': forms.DateInput(attrs={'type':'date'})}
    
    '''def clean_segundo_nombre(self): 
        return self.cleaned_data['segundo_nombre'] or None'''

class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = '__all__'

class EstadoCivilForm(forms.ModelForm):
    class Meta:
        model = EstadoCivil
        fields = '__all__'

