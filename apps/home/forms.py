#modulo form para crear formularios
from django import forms

#funcion que permite que crear/dar de alta usuarios
#from django.contrib.auth.models import User
from apps.usuarios.models import User

class RegisterForm(forms.Form):
    username = forms.CharField( label="Usuario",
                                required=True,
                                min_length=4, max_length=50,
                                widget=forms.TextInput(attrs={
                                    'class':'form-control',
                                    'id':'username'

                                }))
                                #attrs=atributos, form-control: el campo crece, la clase widget permite dar formato
    email = forms.EmailField(label="Correo",
                            required=True,
                             widget=forms.EmailInput(attrs={
                                'class':'form-control',
                                'id':'email',
                                'placeholder':'ejemplo@hotmail.com'
                             }))
    password =  forms.CharField(label="Contraseña",
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                'class':'form-control'

                                }))

    password2 = forms.CharField(label="Confirmar Contraseña",
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                'class':'form-control'
                                    }))

    #vamos a implementar una validacion sobre el campo username
    def clean_username(self):
        username = self.cleaned_data.get('username')

        #nos permite saber si existe un usuario con el mismo nombre
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El nombre de usuario ya se encuentra en uso')

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        #nos permite saber si existe un usuario con el mismo nombre
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El correo electronico ya se encuentra en uso')

        return email

    #METODO CLEAN PARA VALIDAR CAMPOS CONTRASEÑA Y CONFIRMAR CONTRASEÑA
    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'el password no coincide')

    def save(self):
        return User.objects.create_user(
                self.cleaned_data.get('username'),
                self.cleaned_data.get('email'),
                self.cleaned_data.get('password'),
        )

#campos requeridos, minimo y maximo de caracteres
