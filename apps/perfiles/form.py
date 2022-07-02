from pickle import TRUE
from django import forms
from apps.usuarios.models import User

class ListForm(forms.Form):
    search = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Search alumnos",                
                "class": "form-control",
                'required' :TRUE
            }
        ))
class UsuarioForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "User Name",                
                "class": "form-control",
                'required' :TRUE
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Last name",                
                "class": "form-control",
                'required' :TRUE
            }
        ))
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "First name",                
                "class": "form-control",
                'required' :TRUE
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control",
                'required' :TRUE
            }
        ))
    is_active = forms.CharField(
        widget=forms.CheckboxInput(
            attrs={"class": "form-check-input", 
                "id": "flexSwitchCheckChecked", 
                "checked":"True","type":"checkbox"}
        ))
    rut = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Rut",                
                "class": "form-control",
                'required' :TRUE
            }
        ))
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Phone",                
                "class": "form-control" ,
                'required' :TRUE
            }
        ))
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(
            attrs={
				'class':'form-control' ,
				'type':"mail" ,
                'id':"fecha_nacimiento",
                'placeholder':"dd/mm/yyyy",
                'data-datepicker':"" ,
                'required' :TRUE}
        ))
    sexo = forms.ChoiceField(
        required=False,
        widget=forms.Select(
                    attrs={
                        "class": "form-select mb-0",
                        "name":"sexo",
                        "aria-label":"Genero",
						"required":True
                    }
                ),
        choices= (User.GENERO),
        initial=1,
    )
    tipo_sangre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Tipo de Sangre",                
                "class": "form-control",
                'required' :TRUE
            }
        ))
    direccion = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Domicilio",                
                "class": "form-control",
                'required' :TRUE
            }
        ))
    nro_direccion = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Numero",                
                "class": "form-control",
                'required' :TRUE
            }
        ))
    def save(self, request,commit=True):
        data = self.cleaned_data
        user = User(
            email=data['email'], 
            username=data['username'],
            first_name=data['first_name'],
            last_name=data['last_name'], 
            is_active=data['is_active'],)
        usuario = User(user=user,
                          rut=data['rut'],
                          phone=data['phone'],
                          fecha_nacimiento=data['fecha_nacimiento'],
                          sexo=data['sexo'],
                          domicilio=data['direccion'],)
        
        usuario = User(usuario=usuario)
        
        self.instance = usuario
        
        if commit:
            user.save()             
            usuario = usuario.save()    
        return self.instance
