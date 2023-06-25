from django import forms
from django.core.exceptions import ValidationError
from .models import *
from django.forms.widgets import SelectDateWidget

from apps.usuario.models import Usuario
from apps.usuario.forms import FormularioUsuario

"""class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre','apellidos','nacionalidad','descripcion']
        labels = {
            'nombre': 'Nombre del autor',
            'apellidos': 'Apellidos del autor',
            'nacionalidad': 'Nacionalidad del autor',
            'descripcion': 'Pequeña descripción',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del autor'
                }
            ),
            'apellidos': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese los apellidos del autor'
                }
            ),
            'nacionalidad':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese una nacionalidad para el autor'
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese una pequeña descripcion para el autor'
                }
            )
        }
        """

class ReservaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['libro'].queryset = Libro.objects.filter(estado = True,cantidad__gte = 1)

    class Meta:
        model = Reserva
        fields = '__all__'
    
    def clean_libro(self):
        libro = self.cleaned_data['libro']
        if libro.cantidad < 1:
            raise ValidationError('No se puede reservar este libro, deben existir unidades disponibles.')

        return libro

class LibroForm(forms.ModelForm):
    #def __init__(self, *args, **kwargs):
     #   super().__init__(*args, **kwargs)
      #  self.fields['autor_id'].queryset = Autor.objects.filter(estado = True)
        
    class Meta:
        model = Libro
        fields = ['titulo','fecha_publicacion','descripcion','imagen','cantidad']
        label = {
            'titulo': 'Titulo del libro',
            'fecha_publicacion': 'Fecha de Publicacion del libro',
        }
        widgets = {
            'titulo':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese titulo de libro'
                }
            ),
            'fecha_publicacion': forms.SelectDateWidget(
                attrs = {
                    'class': 'form-control',
                }
            )
        }
    
class AlumnoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_usuario'].queryset = Usuario.objects.filter(is_active = True)

    class Meta:
        model = Alumno
        fields = ['dni','nombre','apellido','email','domicilio','telefono','id_usuario']
        labels = {
            'dni': 'dni del alumno',
            'nombre': 'nombre del alumno',
            'apellido': 'apellido del alumno',
            'email': 'email el alumno ',    
            'domicilio': 'domicilio del alumno',
            'telefono': 'telefono del alumno',
            'id_usuario': 'id_usuario',
        }
        widgets = {
            'dni': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el dni del alumno'
                }
            ),
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del alumno'
                }
            ),
            'apellido':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el apellido del alumno'
                }
            ),
            'email':forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el email del alumno'
                }
            ),
            'domicilio':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el domicilio del alumno'
                }
            ),            
            'telefono':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el telefono del alumno'
                }
            ),
            'id_usuario':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'readonly':'readonly'
                }
            )
        }

class Alumno2Form(forms.ModelForm):

    class Meta:
        model = Alumno
        fields = ['dni','nombre','apellido','email','domicilio','telefono']
        labels = {
            'dni': 'dni del alumno',
            'nombre': 'nombre del alumno',
            'apellido': 'apellido del alumno',
            'email': 'email el alumno ',    
            'domicilio': 'domicilio del alumno',
            'telefono': 'telefono del alumno',
        }
        widgets = {
            'dni': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el dni del alumno'
                }
            ),
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del alumno'
                }
            ),
            'apellido':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el apellido del alumno'
                }
            ),
            'email':forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el email del alumno'
                }
            ),
            'domicilio':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el domicilio del alumno'
                }
            ),            
            'telefono':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el telefono del alumno'
                }
            )
        }

class Alumno3Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['id_carrera'].queryset = Carrera.objects.filter(estado = True)
        #self.fields['id_usuario'].queryset = Usuario.objects.filter(is_active = True)

    class Meta:
        model = Alumno
        fields = ['dni','nombre','apellido','email','domicilio','telefono']
        labels = {
            'dni': 'dni del alumno',
            'nombre': 'nombre del alumno',
            'apellido': 'apellido del alumno',
            'email': 'email el alumno ',
            'domicilio': 'domicilio del alumno ',
            'telefono': 'telefono del Alumno',
        }
        widgets = {
            'dni': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'readonly':'readonly'
                }
            ),
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'readonly':'readonly'
                }
            ),
            'apellido':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'readonly':'readonly'
                }
            ),
            'email':forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el email del alumno'
                }
            ),
            'domicilio':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el domicilio del alumno'
                }
            ),
            'telefono':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    
                }
            )
        }


class Entrega_libroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_reserva'].queryset = Entrega_libro.objects.filter(estado = True)
        
    class Meta:
        model = Entrega_libro
        fields = ('id_reserva','fecha_entrega')
        label = {
            'id_reserva': 'reserva del libro',
            'fecha_entrega': 'Fecha de entrega del libro'
        }
        widgets = {
            'id_reserva': forms.Select(
                attrs = {
                    'class':'form-control',
                }
            ),
            'fecha_entrega': forms.SelectDateWidget(
                attrs = {
                    'class': 'form-control'
                }
            )
        }
    

class AdministradorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_usuario'].queryset = Usuario.objects.filter(is_active = True)


    class Meta:
        model = Administrador
        fields = ['nombre','apellido','telefono','domicilio','email','id_usuario']
        labels = {
            'nombre': 'nombre del administrador',
            'apellido': 'apellido del administrador',
            'telefono': 'telefono del administrador',
            'domicilio': 'domicilio del administrador ',
            'email': 'email del administrador',
            'id_usuario': 'id_usuario',

        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del administrador'
                }
            ),
            'apellido': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el apellido del administrador'
                }
            ),
            'telefono':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el telefono del administrador'
                }
            ),
            'domicilio':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el domicilio del administrador'
                }
            ),
            'email':forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el email del administrador'
                }
            ),
            'id_usuario':forms.Select(
                attrs = {
                    'class':'form-control',
                }
            )          
        }

class ProfesorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_usuario'].queryset = Usuario.objects.filter(is_active = True)


    class Meta:
        model = Profesor
        fields = ['dni','nombre','apellido','email','telefono','id_usuario']
        labels = {
            'dni': 'dni del profesor',
            'nombre': 'nombre del profesor',
            'apellido': 'apellido del profesor',
            'email': 'email del profesor ',
            'telefono': 'telefono del profesor ',
            'id_usuario': 'id_usuario',

        }
        widgets = {
            'dni': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el dni del profesor'
                }
            ),
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del profesor'
                }
            ),
            'apellido':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el apellido del profesor'
                }
            ),
            'email':forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el email del profesor'
                }
            ),
            'telefono':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el telefono del alumno'
                }
            ),
            'id_usuario':forms.Select(
                attrs = {
                    'class':'form-control',
                }
            )
        }

class Profesor2Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['id_usuario'].queryset = Usuario.objects.filter(is_active = True)


    class Meta:
        model = Profesor
        fields = ['dni','nombre','apellido','email','telefono']
        labels = {
            'dni': 'dni del profesor',
            'nombre': 'nombre del profesor',
            'apellido': 'apellido del profesor',
            'email': 'email del profesor ',
            'telefono': 'telefono del profesor ',

        }
        widgets = {
            'dni': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'readonly':'readonly'
                }
            ),
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'readonly':'readonly'
                }
            ),
            'apellido':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'readonly':'readonly'
                }
            ),
            'email':forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el email del profesor'
                }
            ),
            'telefono':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el telefono del alumno'
                }
            )
            
        }

class Entrega_libroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_reserva'].queryset = Reserva.objects.filter(estado = True)
        
    class Meta:
        model = Entrega_libro
        fields = ['id_reserva','fecha_entrega','estado_libro']
        label = {
            'id_reserva': 'reserva del libro',
            'fecha_entrega': 'Fecha de entreg del libro al alumno',
            'estado_libro': 'estado del libro entregado',
        }
        widgets = {
            'id_reserva': forms.Select(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'fecha_entrega': forms.SelectDateWidget(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'estado_libro':forms.Select(
                attrs = {
                    'class':'form-control',
                }
            )
        }

class Entrega_libroAdministradorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_libro'].queryset = Libro.objects.filter(estado = True, cantidad__gt =0)
        self.fields['id_usuario'].queryset = Usuario.objects.filter(is_active = True)
        
    class Meta:
        model = Entrega_libro_Administrador
        fields = ['id_usuario','id_libro','fecha_entrega','estado_libro']
        labels = {
            'id_usuario': 'nombre del usuario',
            'id_libro': 'nombre del libro',
            'fecha_entrega': 'fecha de entrega del libro',
            'estado_libro': 'estado del libro ',
        }
        widgets = {
            'id_usuario': forms.Select(
                attrs = {
                    'class':'form-control',
                }
            ),
            'id_libro': forms.Select(
                attrs = {
                    'class':'form-control',
                }
            ),
            'fecha_entrega':forms.SelectDateWidget(
                attrs = {
                    'class':'form-control',
                }
            ),
            'estado_libro':forms.Select(
                attrs = {
                    'class':'form-control',
                }
            )
        }

class Entrega_libro_Administrador2Form(forms.ModelForm):
    #def __init__(self, *args, **kwargs):
     #   super().__init__(*args, **kwargs)
      #  self.fields['id_reserva'].queryset = Reserva.objects.filter(estado = True)
        
    class Meta:
        model = Entrega_libro_Administrador
        fields = ['fecha_entrega','estado_libro']
        label = {
            'fecha_entrega': 'Fecha de entreg del libro al alumno',
            'estado_libro': 'estado del libro entregado',
        }
        widgets = {
            'fecha_entrega': forms.SelectDateWidget(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'estado_libro':forms.Select(
                attrs = {
                    'class':'form-control',
                }
            )
        }

class Entrega_libro2Form(forms.ModelForm):
    #def __init__(self, *args, **kwargs):
     #   super().__init__(*args, **kwargs)
      #  self.fields['id_reserva'].queryset = Reserva.objects.filter(estado = True)
        
    class Meta:
        model = Entrega_libro
        fields = ['fecha_entrega','estado_libro']
        label = {
            'fecha_entrega': 'Fecha de entreg del libro al alumno',
            'estado_libro': 'estado del libro entregado',
        }
        widgets = {
            'fecha_entrega': forms.SelectDateWidget(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'estado_libro':forms.Select(
                attrs = {
                    'class':'form-control',
                }
            )
        }

class Entrega_libroProfesorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_libro'].queryset = Libro.objects.filter(estado = True, cantidad__gt =0)
        self.fields['id_profesor'].queryset = Profesor.objects.filter(estado = True)
        
    class Meta:
        model = Entrega_libro_Profesor
        fields = ['id_profesor','id_libro','cantidad','fecha_entrega']
        labels = {
            'id_profesor': 'nombre del Profesor',
            'id_libro': 'nombre del libro',
            'cantidad': 'cantidad de libro ',
            'fecha_entrega': 'fecha de entrega del libro',            
        }
        widgets = {
            'id_profesor': forms.Select(
                attrs = {
                    'class':'form-control',
                }
            ),
            'id_libro': forms.Select(
                attrs = {
                    'class':'form-control',
                }
            ),
            'cantidad':forms.NumberInput(
                attrs = {
                    'class':'form-control',
                }
            ),
            'fecha_entrega':forms.SelectDateWidget(
                attrs = {
                    'class':'form-control',
                }
            )
            
        }

class Entrega_libro_Profesor2Form(forms.ModelForm):
    #def __init__(self, *args, **kwargs):
     #   super().__init__(*args, **kwargs)
      #  self.fields['id_reserva'].queryset = Reserva.objects.filter(estado = True)
        
    class Meta:
        model = Entrega_libro_Profesor
        fields = ['cantidad','fecha_entrega']
        label = {
            'cantidad': 'cantidad de libros',
            'fecha_entrega': 'Fecha de entreg del libro al alumno',
            
        }
        widgets = {
            'cantidad':forms.NumberInput(
                attrs = {
                    'class':'form-control',
                }
            ),
            'fecha_entrega': forms.SelectDateWidget(
                attrs = {
                    'class': 'form-control',
                }
            )
            
        }

class Devolucion_libroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_entrega'].queryset = Entrega_libro.objects.filter(estado = True)
        
    class Meta:
        model = Devolucion_libro
        fields = ['id_entrega','fecha_devolucion','estado_libro']
        label = {
            'id_entrega': 'Entrega del libro',
            'fecha_devolucion': 'Fecha de devolucion del libro a la biblioteca',
            'estado_libro': 'estado del libro en la devolucion',
        }
        widgets = {
            'id_entrega': forms.Select(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'fecha_devolucion': forms.SelectDateWidget(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'estado_libro':forms.Select(
                attrs = {
                    'class':'form-control',
                }
            )
        }

class Devolucion_libro2Form(forms.ModelForm):
    #def __init__(self, *args, **kwargs):
     #   super().__init__(*args, **kwargs)
      #  self.fields['id_entrega'].queryset = Entrega_libro.objects.filter(estado = True)
        
    class Meta:
        model = Devolucion_libro
        fields = ['fecha_devolucion','estado_libro']
        label = {
            'fecha_devolucion': 'Fecha de devolucion del libro a la biblioteca',
            'estado_libro': 'estado del libro en la devolucion',
        }
        widgets = {
            'fecha_devolucion': forms.SelectDateWidget(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'estado_libro':forms.Select(
                attrs = {
                    'class':'form-control',
                }
            )
        }

class Devolucion_libro_profesorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_entrega_profesor'].queryset = Entrega_libro_Profesor.objects.filter(estado = True)
        
    class Meta:
        model = Devolucion_libro_Profesor
        fields = ['id_entrega_profesor','fecha_devolucion','cantidad']
        label = {
            'id_entrega_profesor': 'Entrega del libro del profesor',
            'fecha_devolucion': 'Fecha de devolucion del libro a la biblioteca',
            'cantidad': 'cantidad de libro en la devolucion',
        }
        widgets = {
            'id_entrega_profesor': forms.Select(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'fecha_devolucion': forms.SelectDateWidget(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'cantidad':forms.NumberInput(
                attrs = {
                    'class':'form-control',
                }
            )
        }
    
class Devolucion_libro_profesor2Form(forms.ModelForm):
    #def __init__(self, *args, **kwargs):
     #   super().__init__(*args, **kwargs)
      #  self.fields['id_entrega'].queryset = Entrega_libro.objects.filter(estado = True)
        
    class Meta:
        model = Devolucion_libro_Profesor
        fields = ['fecha_devolucion']
        label = {
            'fecha_devolucion': 'Fecha de devolucion del libro a la biblioteca',
        }
        widgets = {
            'fecha_devolucion': forms.SelectDateWidget(
                attrs = {
                    'class': 'form-control',
                }
            )
        }

class Alumno_SancionadoForm(forms.ModelForm):
    #def __init__(self, *args, **kwargs):
     #   super().__init__(*args, **kwargs)
      #  self.fields['id_usuario'].queryset = Usuario.objects.filter(is_active = True)
       # self.fields['id_libro'].queryset = Libro.objects.filter(estado = True)
        
        
    class Meta:
        model = Alumno_Sancionado
        fields = ['estado_libro','descripcion']
        labels = {
            #'id_usuario': 'nombre del usuario',
            #'id_libro': 'nombre del libro',
            'estado_libro': 'estado del libro ',
            'descripcion': 'descripcion del libro',
            
        }
        widgets = {
            'estado_libro':forms.Select(
                attrs = {
                    'class':'form-control',
                }
            ),            
            'descripcion':forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese descripcion del libro dañado o perdido'
                }
            )
        }
