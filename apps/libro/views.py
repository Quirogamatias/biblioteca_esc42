import json
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.views.generic import View,TemplateView,ListView,UpdateView,CreateView,DeleteView,DetailView
from apps.usuario.mixins import *
from apps.usuario.models import Usuario
from apps.usuario.forms import FormularioUsuario
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.conf import settings
import datetime
from django.db.models import Q

#from flask import request

class InicioAlumno(ValidarAdministrador, TemplateView):
    template_name = 'libro/alumno/listar_alumno.html'
    permission_required = ('libro.view_alumno', 'libro.add_alumno',
                           'libro.delete_alumno', 'libro.change_alumno')

class InicioAlumnosSancionados(ValidarAdministrador, TemplateView):
    template_name = 'libro/alumnos_sancionados.html'
    permission_required = ('libro.view_alumno_sancionado', 'libro.add_alumno_sancionado',
                           'libro.delete_alumno_sancionado', 'libro.change_alumno_sancionado')

class InicioAlumnop(ValidarProfesorP, TemplateView):
    template_name = 'libro/alumno/listar_alumnop.html'
    permission_required = ('libro.view_alumno', 'libro.add_alumno',
                           'libro.delete_alumno', 'libro.change_alumno')

class InicioAlumnos(ValidarAlumno, TemplateView):
    template_name = 'libro/alumno/estado_alumno.html'
    permission_required = ('libro.view_alumno', 'libro.add_alumno',
                           'libro.delete_alumno', 'libro.change_alumno')

class InicioAdministrador(ValidarAdministrador, TemplateView):
    template_name = 'libro/administrador/listar_administrador.html'
    permission_required = ('libro.view_administrador', 'libro.add_administrador',
                           'libro.delete_administrador', 'libro.change_administrador')
            
class InicioProfesor(ValidarAdministrador, TemplateView):
    template_name = 'libro/profesor/listar_profesor.html'
    permission_required = ('libro.view_profesor', 'libro.add_profesor',
                           'libro.delete_profesor', 'libro.change_profesor')

class InicioProfesorP(ValidarProfesorP, TemplateView):
    template_name = 'libro/profesor/estado_profesor.html'
    permission_required = ('libro.view_profesor', 'libro.add_profesor',
                           'libro.delete_profesor', 'libro.change_profesor')


class InicioEntrega(ValidarAdministrador, TemplateView):
    template_name = 'libro/entrega/listar_entrega_libro.html'
    permission_required = ('libro.view_entrega_libro', 'libro.add_entrega_libro',
                           'libro.delete_entrega_libro', 'libro.change_entrega_libro')
            
class InicioEntregaProfesor(ValidarAdministrador, TemplateView):
    template_name = 'libro/entrega_profesor/listar_entrega_libro_profesor.html'
    permission_required = ('libro.view_entrega_libro_profesor', 'libro.add_entrega_libro_profesor',
                           'libro.delete_entrega_libro_profesor', 'libro.change_entrega_libro_profesor')

class InicioEntregaAdministrador(ValidarAdministrador, TemplateView):
    template_name = 'libro/entrega/listar_entrega_libro_administrador.html'
    permission_required = ('libro.view_entrega_libro_administrador', 'libro.add_entrega_libro_administrador',
                           'libro.delete_entrega_libro_administrador', 'libro.change_entrega_libro_administrador')

class InicioDevolucion(ValidarAdministrador, TemplateView):
    template_name = 'libro/devolucion/listar_devolucion_libro.html'
    permission_required = ('libro.view_devolucion_libro', 'libro.add_devolucion_libro',
                           'libro.delete_devolucion_libro', 'libro.change_devolucion_libro')

class InicioDevolucionProfesor(ValidarAdministrador, TemplateView):
    template_name = 'libro/devolucion_profesor/listar_devolucion_libro_profesor.html'
    permission_required = ('libro.view_devolucion_libro_profesor', 'libro.add_devolucion_libro_profesor',
                           'libro.delete_devolucion_libro_profesor', 'libro.change_devolucion_libro_profesor')


"""class InicioAutor(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name = 'libro/autor/listar_autor.html'
    permission_required = ('libro.view_autor','libro.add_autor',
                            'libro.delete_autor','libro.change_autor')

class ListadoAutor(LoginYSuperStaffMixin, ValidarPermisosMixin,ListView):
    Contiene la logica para el listado de autores.

    :parametro model: Modelo a utilizar
    :type model: Model
    :parametro form_class: Form de Django referente a model
    :type form_class: DjangoForm
    :parametro template_name: Template a utilizar en la clase
    :type templete_name: str
    

    model = Autor
    permission_required = ('libro.view_autor', 'libro.add_autor',
                           'libro.delete_autor', 'libro.change_autor')
    
    def get_queryset(self):
        Retorna una consulta a utilizar en la clase.
        Esta funcion se encuentra en toda la vista basada en clase, se utiliza internamente por django para
        generar las consultas de acuerdo a los valores que se definen en la clase, valor como MODEL_FORM_CLASS

        :return: una consulta
        :rtype: Queryset        
        

        return self.model.objects.filter(estado = True)  

    def get_context_data(self,**kwargs):
        Retorna un contexto a enviar a template.
        Aqui definimos todas las variables que necesitamos enviar a nuestro template definido en TEMPLATE_NAME,
        se agrega a un diccionario general para poder ser enviados en la funcion RENDER.

        :return: un contexto
        :rtype: dict        
        

        contexto= {}
        contexto ['autores'] = self.get_queryset() #agregamos la consulta al contexto
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        Renderiza un template con un contexto dado.
        Se encarga de manejar toda peticion enviada del navegador a Django a travez del metodo GET
        del protocolo HTTP, en este caso renderiza un template definido en TEMPLATE_NAME junto con
        el contexto definido en GET_CONTEXT_DATA.

        :return: render
        :rtype: func        
        
        if request.is_ajax():            
            return HttpResponse(serialize('json',self.get_queryset()), 'application/json')
        else:
            return redirect('libro:inicio_autor')

        #return render(request,self.template_name,self.get_context_data())

class ActualizarAutor(LoginYSuperStaffMixin, ValidarPermisosMixin,UpdateView):
    Contiene la logica para edicion de un Autor

    :parametro model: Modelo a utilizar
    :type model: Model
    :parametro form_class: Form de Django referente a model
    :type form_class: DjanoForm
    :parametro template_name: Template a utilizar en la clase
    :type template_name: str
    :paramtro success_url: Url de redireccionado al actualizar
    :type success_url: URL
    

    model = Autor
    form_class = AutorForm
    template_name = 'libro/autor/autor.html'
    permission_required = ('libro.view_autor', 'libro.add_autor',
                           'libro.delete_autor', 'libro.change_autor')
    #success_url = reverse_lazy('libro:listar_autor')

    #def get_context_data(self, **kwargs):
        
        #context = super().get_context_data(**kwargs)
        #context['autores'] = Autor.objects.filter(estado=True)
        #return context
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else: 
            return redirect('libro:inicio_autor')

class CrearAutor(LoginYSuperStaffMixin, ValidarPermisosMixin,CreateView):
    Contiene la logica para crear un Autor

    :parametro model: Modelo a utilizar
    :type model: Model
    :parametro form_class: Form de Django referente a model
    :type form_class: DjangoForm
    :parametro template_name: Template a utilizar en la clase
    :type template_name: str
    :parametro success_url: Url derediccionado al actualizar
    :type success_url: URL    
    
    model = Autor
    form_class = AutorForm
    template_name = 'libro/autor/crear_autor.html'   
    permission_required = ('libro.view_autor', 'libro.add_autor',
                           'libro.delete_autor', 'libro.change_autor') 
    #success_url = reverse_lazy('libro:listar_autor')
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                nuevo_autor = Autor(
                nombre=form.cleaned_data.get('nombre'),
                apellidos=form.cleaned_data.get('apellidos'),
                nacionalidad=form.cleaned_data.get('nacionalidad'),
                descripcion=form.cleaned_data.get('descripcion')
                )
                nuevo_autor.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else:
            return redirect('libro:inicio_autor')

class EliminarAutor(LoginYSuperStaffMixin, ValidarPermisosMixin,DeleteView):
    Contiene la logica para eliminar un Autor

    :parametro model: Modelo a utilizar
    :type model: Model    
    
    model = Autor
    template_name = 'libro/autor/eliminar_autor.html'
    permission_required = ('libro.view_autor', 'libro.add_autor',
                           'libro.delete_autor', 'libro.change_autor')

    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            autor = self.get_object()
            autor.estado = False
            autor.save()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        return redirect('libro:inicio_autor')

        Elimina logicamente un objeto.
        Se encarga de manejar las peticiones de tipo POST enviadas del navegador a Django.

        :parametro pk: Clave primaria
        :type pk: int
        :parametro request: peticion enviada del navegador
        :type request: request
        :return: redirect
        :rtype: func        
        
        #object = Autor.objects.get(id = pk)
        #object.estado = False
        #object.save()
        #return redirect('libro:listar_autor')
        """

class InicioLibro(ValidarAdministrador, TemplateView):
    template_name = 'libro/libro/listar_libro.html'
    permission_required = ('libro.view_libro', 'libro.add_libro',
                           'libro.delete_libro', 'libro.change_libro')

class InicioLibrosNuevos( LoginMixin, TemplateView):
    template_name = 'libro/libro/listar_libros_nuevos.html'
    permission_required = ('libro.view_libro', 'libro.add_libro',
                           'libro.delete_libro', 'libro.change_libro')

class InicioLibroMasPedido(ValidarAdministrador, TemplateView):
    template_name = 'libro/libro_mas_pedido.html'
    permission_required = ('libro.view_libro', 'libro.add_libro',
                           'libro.delete_libro', 'libro.change_libro')

class InicioLibroMenosPedido(ValidarAdministrador, TemplateView):
    template_name = 'libro/libro_menos_pedido.html'
    permission_required = ('libro.view_libro', 'libro.add_libro',
                           'libro.delete_libro', 'libro.change_libro')

class InicioReserva(ValidarAdministrador, TemplateView):
    template_name = 'libro/libros_reservados.html'
    permission_required = ('libro.view_reserva', 'libro.add_reserva',
                           'libro.delete_reserva', 'libro.change_reserva')
        
class InicioReservaVencida(ValidarAdministrador, TemplateView):
    template_name = 'libro/reservas_vencidas.html'
    permission_required = ('libro.view_reservas_vencidas', 'libro.add_reservas_vencidas',
                           'libro.delete_reservas_vencidas', 'libro.change_reservas_vencidas')


class CrearLibro(ValidarAdministrador,CreateView):
    """Contiene la logica para crear un Autor

    :parametro model: Modelo a utilizar
    :type model: Model
    :parametro form_class: Form de Django referente a model
    :type form_class: DjangoForm
    :parametro template_name: Template a utilizar en la clase
    :type template_name: str
    :parametro success_url: Url derediccionado al actualizar
    :type success_url: URL    
    """
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/crear_libro.html'
    permission_required = ('libro.view_libro', 'libro.add_libro',
                           'libro.delete_libro', 'libro.change_libro')
    #success_url = reverse_lazy('libro:inicio_libros')
    

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES)
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else:
            return  redirect ( 'libro: inicio_libro' )
            
class ListadoLibros(ValidarAdministrador,View):
    """Contiene la logica para el listado de libros.

    :parametro model: Modelo a utilizar
    :type model: Model
    :parametro form_class: Form de Django referente a model
    type form_class DjangoForm
    :parametro template_name Template a utilizar en la clase
    :type templete_name: str
    """
    model = Libro
    permission_required = ('libro.view_libro', 'libro.add_libro',
                           'libro.delete_libro', 'libro.change_libro')  

    def get_queryset(self):
        """Retorna una consulta a utilizar en la clase.
        Esta funcion se encuentra en toda la vista basada en clase, se utiliza internamente por django para
        generar las consultas de acuerdo a los valores que se definen en la clase, valor como MODEL_FORM_CLASS

        :return: una consulta
        :rtype: Queryset        
        """
        return self.model.objects.filter(estado = True)  

    def get_context_data(self,**kwargs):
        """Retorna un contexto a enviar a template.
        Aqui definimos todas las variables que necesitamos enviar a nuestro template definido en TEMPLATE_NAME,
        se agrega a un diccionario general para poder ser enviados en la funcion RENDER.

        :return: un contexto
        :rtype: dict        
        """
        
        contexto= {}
        contexto ['libros'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        """Renderiza un template con un contexto dado.
        Se encarga de manejar toda peticion enviada del navegador a Django a travez del metodo GET
        del protocolo HTTP, en este caso renderiza un template definido en TEMPLATE_NAME junto con
        el contexto definido en GET_CONTEXT_DATA.

        :return: render
        :rtype: func        
        """
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('libro:inicio_libros')
        #return render(request,self.template_name,self.get_context_data())
    

class ActualizarLibro(ValidarAdministrador,UpdateView):
    """Contiene la logica para edicion de un Libro

    :parametro model: Modelo a utilizar
    :type model: Model
    :parametro form_class: Form de Django referente a model
    :type form_class: DjanoForm
    :parametro template_name: Template a utilizar en la clase
    :type template_name: str
    :paramtro success_url: Url de redireccionado al actualizar
    :type success_url: URL
    """
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/libro.html'
    permission_required = ('libro.view_libro', 'libro.add_libro',
                           'libro.delete_libro', 'libro.change_libro')
    #success_url = reverse_lazy('libro:listado_libros')

    #def get_context_data(self, **kwargs):

        #context = super().get_context_data(**kwargs)
        #context['libros'] = Libro.objects.filter(estado=True)
        #return context
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else: 
            return redirect('libro:inicio_libros')
    

class EliminarLibro(ValidarAdministrador,DeleteView):
    """Contiene la logica para eliminar un Libro

    :parametro model: Modelo a utilizar
    :type model: Model    
    """
    model = Libro
    second_model = Reserva
    third_model = Entrega_libro
    template_name = 'libro/libro/eliminar_libro.html'
    permission_required  = ( 'libro.view_libro' , 'libro.add_libro' ,
                           'libro.delete_libro' , 'libro.change_libro' )

    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            reserva = self.second_model.objects.all()
            entrega = self.third_model.objects.all()
            libro = self.get_object()
            
            for j in range(len(reserva)):
                if reserva[j].estado == True:
                    if reserva[j].libro == libro:                        
                        mensaje = f'{self.model.__name__} no se ha podido eliminar porque existe una reserva con el libro que quiere eliminar!'
                        error = 'Error!'
                        response = JsonResponse({'mensaje':mensaje,'error':error})
                        response.status_code = 400
                        return response

            for j in range(len(entrega)):
                if entrega[j].estado == True:
                    for i in range(len(reserva)):                        
                        if entrega[j].id_reserva == reserva[i]:
                            if reserva[i].libro == libro:
                                mensaje = f'{self.model.__name__} no se ha podido eliminar porque se hizo entrega una con ese libro!'
                                error = 'Error!'
                                response = JsonResponse({'mensaje':mensaje,'error':error})
                                response.status_code = 400
                                return response

            libro.estado = False 
            libro.save() 
            mensaje = f'{self.model.__name__} eliminacion correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje':mensaje,'error':error})
            response.status_code = 201
            return response            
        else: 
            return redirect('libro:inicio_libros')

    #def post(self,request,pk,*args,**kwargs):
        """Elimina logicamente un objeto.
        Se encarga de manejar las peticiones de tipo POST enviadas del navegador a Django.

        :parametro pk: Clave primaria
        :type pk: int
        :parametro request: peticion enviada del navegador
        :type request: request
        :return: redirect
        :rtype: func        
        """
       #object = Libro.objects.get(id = pk)
        #object.estado = False
        #object.save()
        #return redirect('libro:listado_libros')

class ListadoLibrosDisponibles(LoginMixin,ListView):
    model = Libro
    paginate_by = 6
    template_name = 'libro/libros_disponibles.html'

    def get_queryset(self):
        queryset =self.request.GET.get("buscar")
        
        if queryset is None:
            
            queryset = self.model.objects.filter(estado = True,cantidad__gte = 1)
           
            return queryset
        else:
            
            libro = self.model.objects.filter(estado = True,cantidad__gte = 1)
            
            if queryset:
                libro = Libro.objects.filter(
                    Q(titulo__icontains = queryset), #|
                    #Q(descripcion_icontains = queryset),
                    estado = True,
                    cantidad__gte = 1,
                ).distinct()  
                return libro
            return libro

        #queryset = self.model.objects.filter(estado = True,cantidad__gte = 1)
        #return queryset
    


class DetalleLibroDiponible(LoginMixin,DetailView):
    model = Libro
    template_name = 'libro/detalle_libro_disponible.html'

    def get(self,request,*agrs,**kwargs):
        #libro = self.get_object()
        if self.get_object().cantidad >= 0:            
            return render(request,self.template_name,{'object':self.get_object()})
        else:
            return redirect('libro:listado_libros_disponibles')

        return redirect('libro:listado_libros_disponibles')


class ListadoLibrosReservados(LoginMixin,ListView):
    model = Reserva
    permission_required = ('libro.view_reserva', 'libro.add_reserva',
                           'libro.delete_reserva', 'libro.change_reserva')  

    def get_queryset(self):
        return self.model.objects.filter(estado = True)  

    def get_context_data(self,**kwargs):
        
        contexto= {}
        contexto ['reservas'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('libro:inicio_reservas')

class RegistrarReserva(LoginMixin,CreateView):
    model = Reserva
    second_model = Libro
    success_url = reverse_lazy('libro:listado_libros_disponibles')

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            libro = Libro.objects.filter(id = request.POST.get('libro')).first()
            usuario = Usuario.objects.filter(id = request.POST.get('usuario')).first()
            if libro and usuario:
                if libro.cantidad > 0:
                    nueva_reserva = self.model(
                        libro = libro,
                        usuario = usuario
                    )
                    libro.cant_pedido = libro.cant_pedido + 1
                    libro.cantidad = libro.cantidad - 1
                    libro.save()

                    nueva_reserva.save()
                    mensaje = f'{self.model.__name__} registrada correctamente!'
                    error = 'No hay error!'
                    response = JsonResponse({'mensaje': mensaje, 'error': error,'url':self.success_url})
                    response.status_code = 201
                    return response
        return redirect('libro:listado_libros_disponibles')

class Reservas(LoginMixin,ListView):
    model = Reserva

    def get_queryset(self):
        return self.model.objects.filter(estado = True,usuario = self.request.user)

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('libro:listado_libros_reservados')

class EliminarReserva(ValidarAdministrador,DeleteView):
    """Contiene la logica para eliminar un Libro

    :parametro model: Modelo a utilizar
    :type model: Model    
    """
    model = Reserva
    second_model = Libro
    template_name = 'libro/eliminar_reserva.html'
    permission_required = ('libro.view_reservas_vencidas', 'libro.add_reservas_vencidas',
                           'libro.delete_reservas_vencidas', 'libro.change_reservas_vencidas')  


    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            libro = self.second_model.objects.all()
            reserva = self.get_object()
            
            for j in range(len(libro)):
                if libro[j].estado == True:
                    if libro[j] == reserva.libro:
                        libro[j].cantidad = libro[j].cantidad + 1
                        libro[j].cant_pedido = libro[j].cant_pedido - 1
                        libro[j].save() 
                        reserva.estado = False 
                        reserva.save()  
                        #entrega_libro_profesor.estado = False
                        #entrega_libro_profesor.save()
                        mensaje = f'{self.model.__name__} eliminacion correctamente!'
                        error = 'No hay error!'
                        response = JsonResponse({'mensaje':mensaje,'error':error})
                        response.status_code = 201
                        return response 
          
        else: 
            return redirect('libro:listado_libros_reservados')

class ListadoReservasVencias(LoginMixin,TemplateView):
    model = Reserva
    permission_required = ('libro.view_reservas_vencidas', 'libro.add_reservas_vencidas',
                           'libro.delete_reservas_vencidas', 'libro.change_reservas_vencidas')  

           
    def get_queryset(self):

        reserva = self.model.objects.all() 
        ahora = datetime.date.today()
        ayer = ahora - datetime.timedelta(days=7) 
        mañana = ahora + datetime.timedelta(days=7)

        #contexto =[]
        print ("entro")
        reserva = self.model.objects.filter(estado = True,cantidad_dias__gte = ahora)
           
        return reserva   
 

    def get_context_data(self,**kwargs):
        
        contexto= {}
        contexto ['reservas'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('libro:inicio_reservas_vencidas')

class ReservasVencidas(LoginMixin,ListView):
    model = Reserva

    def get_queryset(self):

        reserva = self.model.objects.all() 
        ahora = datetime.date.today()
        ayer = ahora - datetime.timedelta(days=7) 
        mañana = ahora + datetime.timedelta(days=7)

        #contexto =[]
        reserva = self.model.objects.filter(estado = True,fecha_vencimiento__lte = ahora)
        
        return reserva 
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('libro:inicio_reservas_vencidas')

class EliminarReservaVencida(ValidarAdministrador,DeleteView):
    """Contiene la logica para eliminar un Libro

    :parametro model: Modelo a utilizar
    :type model: Model    
    """
    model = Reserva
    second_model = Libro
    template_name = 'libro/eliminar_recerva_vencida.html'
    permission_required = ('libro.view_reservas_vencidas', 'libro.add_reservas_vencidas',
                           'libro.delete_reservas_vencidas', 'libro.change_reservas_vencidas')  


    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            libro = self.second_model.objects.all()
            reserva = self.get_object()
            
            for j in range(len(libro)):
                if libro[j].estado == True:
                    if libro[j] == reserva.libro:
                        libro[j].cantidad = libro[j].cantidad + 1
                        libro[j].cant_pedido = libro[j].cant_pedido - 1
                        libro[j].save() 
                        reserva.estado = False 
                        reserva.save()  
                        #entrega_libro_profesor.estado = False
                        #entrega_libro_profesor.save()
                        mensaje = f'{self.model.__name__} eliminacion correctamente!'
                        error = 'No hay error!'
                        response = JsonResponse({'mensaje':mensaje,'error':error})
                        response.status_code = 201
                        return response 
          
        else: 
            return redirect('libro:inicio_reservas_vencidas')

class ListadoAlumnos(ValidarAdministrador,View):
    model = Alumno
    permission_required = ('libro.view_alumno', 'libro.add_alumno',
                           'libro.delete_alumno', 'libro.change_alumno') 

    def get_queryset(self):
        return self.model.objects.filter(estado = True)  

    def get_context_data(self,**kwargs):
        contexto= {}
        contexto ['alumnos'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('libro:inicio_alumno')

class ListadoAlumnop(ValidarProfesorP,View):
    model = Alumno
    permission_required = ('libro.view_alumno', 'libro.add_alumno',
                           'libro.delete_alumno', 'libro.change_alumno')  

    def get_queryset(self):
        return self.model.objects.filter(estado = True)  

    def get_context_data(self,**kwargs):
        contexto= {}
        contexto ['alumnos'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('libro:inicio_alumnop')

class ActualizarAlumno(ValidarAlumnoA,UpdateView):
    model = Alumno
    form_class = Alumno2Form
    second_model = Profesor
    third_model = Usuario
    fourth_model = Administrador
    template_name = 'libro/alumno/alumno.html'
    permission_required = ('libro.view_alumno', 'libro.add_alumno',
                           'libro.delete_alumno', 'libro.change_alumno') 
    
    def get_context_data(self, **kwargs):
        context = super(ActualizarAlumno, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self,request,*args,**kwargs):
        a=0
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES,instance = self.get_object())
            if form.is_valid():
                nuevo= Alumno(
                    id_alumno=form.instance.id_alumno,
                    dni=form.cleaned_data.get('dni'),
                    email=form.cleaned_data.get('email'),                    
                    nombre=form.cleaned_data.get('nombre'),
                    apellido=form.cleaned_data.get('apellido')                                      
                )
                alumno = self.model.objects.all()
                profesor = self.second_model.objects.all()
                usuario = self.third_model.objects.all()
                administrador = self.fourth_model.objects.all()

                for k in range(len(administrador)):
                    if administrador[k].estado == True:
                        if nuevo.email == administrador[k].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response
                
                for i in range(len(profesor)):
                    if profesor[i].estado == True:
                        if nuevo.dni == profesor[i].dni or nuevo.email == profesor[i].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response    

                for j in range(len(alumno)):
                    if alumno[j].estado == True:
                        if nuevo.dni == alumno[j].dni or nuevo.email == alumno[j].email: 
                                                      
                            if nuevo.id_alumno == alumno[j].id_alumno:
                                a=0
                            else:
                                a=1
                                mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                                error = form.errors
                                response = JsonResponse({'mensaje':mensaje,'error':error})
                                response.status_code = 400
                                return response           

                if a==0:
                    #form.save()   
                    alum = self.model.objects.all()
                    usua = self.third_model.objects.all()
                    for i in range(len(alum)):
                        if alum[i].estado == True: 
                            if nuevo.id_alumno == alum[i].id_alumno:
                                for j in range(len(usua)):
                                    if usua[j].is_active == True:                                            
                                        if alum[i].email ==usua[j].email:  
                                            usua[j].email=nuevo.email
                                            usua[j].nombre=nuevo.nombre
                                            usua[j].apellido=nuevo.apellido                                             
                                            usua[j].save()   
                                            form.save() 
                                            mensaje = f'{self.model.__name__} registrado correctamente!'
                                            error = 'No hay error!'
                                            response = JsonResponse({'mensaje':mensaje,'error':error})
                                            response.status_code = 201
                                            return response
                        
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else: 
            return redirect('libro:inicio_alumno')

class ActualizarAlumno2(ValidarAlumno,UpdateView):
    model = Alumno
    form_class = Alumno3Form
    second_model = Profesor
    third_model = Usuario
    fourth_model = Administrador
    template_name = 'libro/alumno/alumno2.html'
    permission_required = ('libro.view_alumno', 'libro.add_alumno',
                           'libro.delete_alumno', 'libro.change_alumno') 
    
    def get_context_data(self, **kwargs):
        context = super(ActualizarAlumno2, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self,request,*args,**kwargs):
        a=0
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES,instance = self.get_object())
            if form.is_valid():
                nuevo= Alumno(
                    id_alumno=form.instance.id_alumno,
                    dni=form.cleaned_data.get('dni'),
                    email=form.cleaned_data.get('email'),                    
                    nombre=form.cleaned_data.get('nombre'),
                    notificacion=form.cleaned_data.get('notificacion'),
                    apellido=form.cleaned_data.get('apellido')                                      
                )
                alumno = self.model.objects.all()
                profesor = self.second_model.objects.all()
                usuario = self.third_model.objects.all()
                administrador = self.fourth_model.objects.all()

                for k in range(len(administrador)):
                    if administrador[k].estado == True:
                        if nuevo.email == administrador[k].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response
                
                for i in range(len(profesor)):
                    if profesor[i].estado == True:
                        if nuevo.dni == profesor[i].dni or nuevo.email == profesor[i].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response    

                for j in range(len(alumno)):
                    if alumno[j].estado == True:
                        if nuevo.dni == alumno[j].dni or nuevo.email == alumno[j].email: 
                                                      
                            if nuevo.id_alumno == alumno[j].id_alumno:
                                a=0
                            else:
                                a=1
                                mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                                error = form.errors
                                response = JsonResponse({'mensaje':mensaje,'error':error})
                                response.status_code = 400
                                return response           

                if a==0:
                    #form.save()   
                    alum = self.model.objects.all()
                    usua = self.third_model.objects.all()
                    for i in range(len(alum)):
                        if alum[i].estado == True: 
                            if nuevo.id_alumno == alum[i].id_alumno:
                                for j in range(len(usua)):
                                    if usua[j].is_active == True:                                            
                                        if alum[i].email ==usua[j].email:  
                                            usua[j].email=nuevo.email
                                            usua[j].nombre=nuevo.nombre
                                            usua[j].apellido=nuevo.apellido                                             
                                            usua[j].save()   
                                            form.save() 
                                            mensaje = f'{self.model.__name__} registrado correctamente!'
                                            error = 'No hay error!'
                                            response = JsonResponse({'mensaje':mensaje,'error':error})
                                            response.status_code = 201
                                            return response
                #otra forma de guarda es volviendo a llamar al form una vez guardado la primera vez, para tener los datos acualizados y despues guardar el usuario
                        
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else: 
            return redirect('libro:inicio_alumnos')

class CrearAlumno(ValidarAdministrador,CreateView):
    model = Alumno
    second_model = Profesor
    form_class = AlumnoForm
    third_model = Usuario
    third_form_class = FormularioUsuario
    fourth_model = Administrador
    fourth_form_class = AdministradorForm
    template_name = 'libro/alumno/crear_alumno.html'
    permission_required = ('libro.view_alumno', 'libro.add_alumno',
                           'libro.delete_alumno', 'libro.change_alumno') 
    
    def get_context_data(self, **kwargs):
        context = super(CrearAlumno, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.third_form_class(self.request.GET)
        return context

    def post(self,request,*args,**kwargs):
        a=0
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES)
            form2 = self.third_form_class(data = request.POST,files = request.FILES)
            if form.is_valid() and form2.is_valid():
                nuevo= Alumno(
                    dni=form.cleaned_data.get('dni'),
                    email=form.cleaned_data.get('email'),                    
                    nombre=form.cleaned_data.get('nombre'),
                    apellido=form.cleaned_data.get('apellido')                                       
                )

                alumno = self.model.objects.all()
                profesor = self.second_model.objects.all()
                usuario = self.third_model.objects.all()
                administrador = self.fourth_model.objects.all()

                for k in range(len(administrador)):
                    if administrador[k].estado == True:
                        if nuevo.email == administrador[k].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response

                for j in range(len(alumno)):
                    if alumno[j].estado == True:
                        if nuevo.dni == alumno[j].dni or nuevo.email == alumno[j].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response

                for i in range(len(profesor)):
                    if profesor[i].estado == True:
                        if nuevo.dni == profesor[i].dni or nuevo.email == profesor[i].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response                

                if a==0:
                    form.save()
                    form2.save()    

                    alum = self.model.objects.all()
                    usua = self.third_model.objects.all()
                    for j in range(len(usua)):
                        if usua[j].is_active == True:
                            if nuevo.email == usua[j].email:
                                for i in range(len(alum)):
                                    if alum[i].estado == True:                                                       
                                        if nuevo.email == alum[i].email:
                                            alum[i].id_usuario = usua[j]
                                            alum[i].notificacion = True
                                            usua[j].tipo = 'Alumno'  
                                            usua[j].save()                                       
                                            alum[i].save()                                          
                                            mensaje = f'{self.model.__name__} registrado correctamente!'
                                            error = 'No hay error!'
                                            response = JsonResponse({'mensaje':mensaje,'error':error})
                                            response.status_code = 201
                                            return response
                    
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        return  redirect ( 'libro: inicio_alumno' )

class EliminarAlumno(ValidarAdministrador,DeleteView):
    model = Alumno
    template_name = 'libro/alumno/eliminar_alumno.html'
    permission_required = ('libro.view_alumno', 'libro.add_alumno',
                           'libro.delete_alumno', 'libro.change_alumno') 

    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            alumno = self.get_object()
            alumno.estado = False
            alumno.save()
            mensaje = f'{self.model.__name__} eliminacion correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje':mensaje,'error':error})
            response.status_code = 201
            return response            
        else: 
            return redirect('libro:inicio_alumno')

class EstadoAlumno(ValidarAlumno,View):
    model = Alumno
    #second_model = Usuario
    permission_required = ('institucion.view_alumno', 'institucion.add_alumno',
                           'institucion.delete_alumno', 'institucion.change_alumno')  
    
    def get_queryset(self):
        return self.model.objects.filter(id_usuario=self.request.user,estado = True)  

    def get_context_data(self):
        pk = self.kwargs.get('pk')
        alumno = self.model.objects.get(pk= pk)
        return alumno
    #def get_context_data(self,**kwargs):
     #   contexto= {}
      #  contexto ['alumnos'] = self.get_queryset()
       # contexto['form'] = self.form_class
        #return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('institucion:inicio_alumnos')

class ActualizarAlumnoA(ValidarAlumno,UpdateView):
    model = Alumno
    form_class = Alumno3Form
    second_model = Profesor
    third_model = Usuario
    fourth_model = Administrador
    template_name = 'libro/alumno/alumnoA.html'
    permission_required = ('institucion.view_alumno', 'institucion.add_alumno',
                           'institucion.delete_alumno', 'institucion.change_alumno')
    
    def get_context_data(self, **kwargs):
        context = super(ActualizarAlumnoA, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self,request,*args,**kwargs):
        a=0
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES,instance = self.get_object())
            if form.is_valid():
                nuevo= Alumno(
                    id_alumno=form.instance.id_alumno,
                    dni=form.cleaned_data.get('dni'),
                    email=form.cleaned_data.get('email'),                    
                    nombre=form.cleaned_data.get('nombre'),
                    apellido=form.cleaned_data.get('apellido')                                      
                )
                alumno = self.model.objects.all()
                profesor = self.second_model.objects.all()
                usuario = self.third_model.objects.all()
                administrador = self.fourth_model.objects.all()

                for k in range(len(administrador)):
                    if administrador[k].estado == True:
                        if nuevo.email == administrador[k].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response
                
                for i in range(len(profesor)):
                    if profesor[i].estado == True:
                        if nuevo.dni == profesor[i].dni or nuevo.email == profesor[i].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response    

                for j in range(len(alumno)):
                    if alumno[j].estado == True:
                        if nuevo.dni == alumno[j].dni or nuevo.email == alumno[j].email: 
                                                      
                            if nuevo.id_alumno == alumno[j].id_alumno:
                                a=0
                            else:
                                a=1
                                mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                                error = form.errors
                                response = JsonResponse({'mensaje':mensaje,'error':error})
                                response.status_code = 400
                                return response           

                if a==0:
                    #form.save()   
                    alum = self.model.objects.all()
                    usua = self.third_model.objects.all()
                    for i in range(len(alum)):
                        if alum[i].estado == True: 
                            if nuevo.id_alumno == alum[i].id_alumno:
                                for j in range(len(usua)):
                                    if usua[j].is_active == True:                                            
                                        if alum[i].email ==usua[j].email:  
                                            usua[j].email=nuevo.email
                                            usua[j].nombre=nuevo.nombre
                                            usua[j].apellido=nuevo.apellido                                             
                                            usua[j].save()   
                                            form.save() 
                                            mensaje = f'{self.model.__name__} registrado correctamente!'
                                            error = 'No hay error!'
                                            response = JsonResponse({'mensaje':mensaje,'error':error})
                                            response.status_code = 201
                                            return response
                #otra forma de guarda es volviendo a llamar al form una vez guardado la primera vez, para tener los datos acualizados y despues guardar el usuario
                        
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else: 
            return redirect('institucion:inicio_alumnos')


class ListadoAdministradores(ValidarAdministrador,ListView):

    model = Administrador
    permission_required = ('libro.view_administrador', 'libro.add_administrador',
                           'libro.delete_administrador', 'libro.change_administrador')

    def get_queryset(self):
        return self.model.objects.filter(estado = True)  

    def get_context_data(self,**kwargs):
        contexto= {}
        contexto ['administradores'] = self.get_queryset() #agregamos la consulta al contexto
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json',self.get_queryset()), 'application/json')
        else:
            return redirect('libro:inicio_administrador')

class ActualizarAdministrador(ValidarAdministrador,UpdateView):
    model = Administrador
    form_class = AdministradorForm
    second_model = Alumno
    third_model = Profesor
    fourth_model = Usuario
    fourth_form_class = FormularioUsuario
    template_name = 'libro/administrador/administrador.html'
    permission_required = ('libro.view_administrador', 'libro.add_administrador',
                           'libro.delete_administrador', 'libro.change_administrador')

    def post(self,request,*args,**kwargs):
        a=0
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES,instance = self.get_object())
            if form.is_valid():
                nuevo = Administrador(
                    id_administrador=form.instance.id_administrador,
                    nombre=form.cleaned_data.get('nombre'),
                    apellido=form.cleaned_data.get('apellido'),
                    telefono=form.cleaned_data.get('telefono'),
                    domicilio=form.cleaned_data.get('domicilio'),
                    email=form.cleaned_data.get('email')
                )
                administrador = self.model.objects.all()
                alumno = self.second_model.objects.all()
                profesor = self.third_model.objects.all()
                
                for j in range(len(alumno)):
                    if alumno[j].estado == True:
                        if nuevo.email == alumno[j].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response
                
                for i in range(len(profesor)):
                    if profesor[i].estado == True:
                        if nuevo.email == profesor[i].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response 

                for k in range(len(administrador)):
                    if administrador[k].estado == True:
                        if nuevo.email == administrador[k].email:
                            if nuevo.id_administrador == administrador[k].id_administrador:
                                a=0
                            else:
                                a=1
                                mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                                error = form.errors
                                response = JsonResponse({'mensaje':mensaje,'error':error})
                                response.status_code = 400
                                return response 
              
                if a==0:
                    admin = self.model.objects.all()
                    usua = self.fourth_model.objects.all()
                    for i in range(len(admin)):
                        if admin[i].estado == True:  
                            if nuevo.id_administrador == admin[i].id_administrador:
                                for j in range(len(usua)):
                                    if usua[j].is_active == True:
                                        if admin[i].email ==usua[j].email:                                                                            
                                            usua[j].email=nuevo.email
                                            usua[j].nombre=nuevo.nombre
                                            usua[j].apellido=nuevo.apellido                                             
                                            usua[j].save() 
                                            form.save()                                         
                                            mensaje = f'{self.model.__name__} registrado correctamente!'
                                            error = 'No hay error!'
                                            response = JsonResponse({'mensaje':mensaje,'error':error})
                                            response.status_code = 201
                                            return response               
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else: 
            return redirect('libro:inicio_administrador')

class CrearAdministrador(ValidarAdministrador,CreateView):
    model = Administrador
    form_class = AdministradorForm
    second_model = Alumno
    third_model = Profesor
    #second_form_class = AlumnoForm
    fourth_model = Usuario
    fourth_form_class = FormularioUsuario
    template_name = 'libro/administrador/crear_administrador.html'
    permission_required = ('libro.view_administrador', 'libro.add_administrador',
                           'libro.delete_administrador', 'libro.change_administrador')
    
    def get_context_data(self, **kwargs):
        context = super(CrearAdministrador, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.fourth_form_class(self.request.GET)
        return context

    def post(self,request,*args,**kwargs):
        a=0
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES)
            form2 = self.fourth_form_class(data = request.POST,files = request.FILES)         
            if form.is_valid() and form2.is_valid():
                nuevo = Administrador(
                    nombre=form.cleaned_data.get('nombre'),
                    apellido=form.cleaned_data.get('apellido'),
                    telefono=form.cleaned_data.get('telefono'),
                    domicilio=form.cleaned_data.get('domicilio'),
                    email=form.cleaned_data.get('email')
                )
                administrador = self.model.objects.all()
                alumno = self.second_model.objects.all()
                profesor = self.third_model.objects.all()
                #usuario = self.third_model.objects.all()

                for k in range(len(administrador)):
                    if administrador[k].estado == True:
                        if nuevo.email == administrador[k].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response

                for j in range(len(alumno)):
                    if alumno[j].estado == True:
                        if nuevo.email == alumno[j].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response

                for i in range(len(profesor)):
                    if profesor[i].estado == True:
                        if nuevo.email == profesor[i].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response
                if a==0:
                    form.save()
                    form2.save()    

                    admin = self.model.objects.all()
                    usua = self.fourth_model.objects.all()
                    for j in range(len(usua)):
                        if usua[j].is_active == True:
                            if nuevo.email == usua[j].email:
                                for i in range(len(admin)):
                                    if admin[i].estado == True:                                                       
                                        if nuevo.email == admin[i].email:
                                            admin[i].id_usuario = usua[j]
                                            admin[i].notificacion = True
                                            usua[j].tipo = 'Administrador'  
                                            usua[j].save()                                       
                                            admin[i].save()                                          
                                            mensaje = f'{self.model.__name__} registrado correctamente!'
                                            error = 'No hay error!'
                                            response = JsonResponse({'mensaje':mensaje,'error':error})
                                            response.status_code = 201
                                            return response
                
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else: 
            return redirect('libro:inicio_administrador')

class EliminarAdministrador(ValidarAdministrador,DeleteView):    
    model = Administrador
    template_name = 'libro/administrador/eliminar_administrador.html'
    permission_required = ('libro.view_administrador', 'libro.add_administrador',
                           'libro.delete_administrador', 'libro.change_administrador')

    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            administrador = self.get_object()
            administrador.estado = False
            administrador.save()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        return redirect('libro:inicio_administrador')


class ListadoProfesores(ValidarAdministrador,ListView):
    model = Profesor
    #second_model = InscripcionProfesor
    #third_model = Materia
    #form_class = ProfesorForm
    #second_form_class = InscripcionProfesorForm
    permission_required = ('libro.view_profesor', 'libro.add_profesor',
                           'libro.delete_profesor', 'libro.change_profesor')  
    

    def get_queryset(self):
        return self.model.objects.filter(estado = True)  

    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('libro:inicio_profesor')

class EstadoProfesor(ValidarProfesorP,View):
    model = Profesor
    permission_required = ('institucion.view_profesor', 'institucion.add_profesor',
                           'institucion.delete_profesor', 'institucion.change_profesor')  
    
    def get_queryset(self):
        return self.model.objects.filter(id_usuario=self.request.user,estado = True)  

    def get_context_data(self):
        pk = self.kwargs.get('pk')
        profesor = self.model.objects.get(pk= pk)
        return profesor


class ActualizarProfesor(ValidarAdministrador,UpdateView):
    model = Profesor
    form_class = ProfesorForm
    second_model = Alumno
    third_model = Usuario
    fourth_model = Administrador
    template_name = 'libro/profesor/profesor.html'
    permission_required = ('libro.view_profesor', 'libro.add_profesor',
                           'libro.delete_profesor', 'libro.change_profesor') 

    def post(self,request,*args,**kwargs):
        a=0
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES,instance = self.get_object())
            if form.is_valid():
                nuevo= Profesor(
                    id_profesor=form.instance.id_profesor,
                    dni=form.cleaned_data.get('dni'),
                    email=form.cleaned_data.get('email'),
                    nombre=form.cleaned_data.get('nombre'),
                    apellido=form.cleaned_data.get('apellido')
                )

                profesor = self.model.objects.all()
                alumno = self.second_model.objects.all()
                administrador = self.fourth_model.objects.all()

                for k in range(len(administrador)):
                    if administrador[k].estado == True:
                        if nuevo.email == administrador[k].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response

                for j in range(len(alumno)):
                    if alumno[j].estado == True:
                        if nuevo.dni == alumno[j].dni or nuevo.email == alumno[j].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response
                
                for i in range(len(profesor)):
                    if profesor[i].estado == True:
                        if nuevo.dni == profesor[i].dni or nuevo.email == profesor[i].email:
                            if nuevo.id_profesor == profesor[i].id_profesor:
                                a=0
                            else:
                                a=1
                                mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                                error = form.errors
                                response = JsonResponse({'mensaje':mensaje,'error':error})
                                response.status_code = 400
                                return response 

                
               
                if a==0:
                    prof = self.model.objects.all()
                    usua = self.third_model.objects.all()
                    for i in range(len(prof)):
                        if prof[i].estado == True:  
                            if nuevo.id_profesor == prof[i].id_profesor:   
                                for j in range(len(usua)):
                                    if usua[j].is_active == True:  
                                        if prof[i].email ==usua[j].email:                                           
                                            usua[j].email=nuevo.email
                                            usua[j].nombre=nuevo.nombre
                                            usua[j].apellido=nuevo.apellido                                             
                                            usua[j].save() 
                                            form.save()                                           
                                            mensaje = f'{self.model.__name__} registrado correctamente!'
                                            error = 'No hay error!'
                                            response = JsonResponse({'mensaje':mensaje,'error':error})
                                            response.status_code = 201
                                            return response
                                
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else: 
            return redirect('libro:inicio_profesor')

class ActualizarProfesorP(ValidarProfesorP,UpdateView):
    model = Profesor
    form_class = Profesor2Form
    second_model = Alumno
    third_model = Usuario
    fourth_model = Administrador
    template_name = 'libro/profesor/profesorP.html'
    permission_required = ('libro.view_profesor', 'libro.add_profesor',
                           'libro.delete_profesor', 'libro.change_profesor') 

    def post(self,request,*args,**kwargs):
        a=0
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES,instance = self.get_object())
            if form.is_valid():
                nuevo= Profesor(
                    id_profesor=form.instance.id_profesor,
                    dni=form.cleaned_data.get('dni'),
                    email=form.cleaned_data.get('email'),
                    nombre=form.cleaned_data.get('nombre'),
                    apellido=form.cleaned_data.get('apellido')
                )

                profesor = self.model.objects.all()
                alumno = self.second_model.objects.all()
                administrador = self.fourth_model.objects.all()

                for k in range(len(administrador)):
                    if administrador[k].estado == True:
                        if nuevo.email == administrador[k].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response

                for j in range(len(alumno)):
                    if alumno[j].estado == True:
                        if nuevo.dni == alumno[j].dni or nuevo.email == alumno[j].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response
                
                for i in range(len(profesor)):
                    if profesor[i].estado == True:
                        if nuevo.dni == profesor[i].dni or nuevo.email == profesor[i].email:
                            if nuevo.id_profesor == profesor[i].id_profesor:
                                a=0
                            else:
                                a=1
                                mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                                error = form.errors
                                response = JsonResponse({'mensaje':mensaje,'error':error})
                                response.status_code = 400
                                return response 

                
               
                if a==0:
                    prof = self.model.objects.all()
                    usua = self.third_model.objects.all()
                    for i in range(len(prof)):
                        if prof[i].estado == True:  
                            if nuevo.id_profesor == prof[i].id_profesor:   
                                for j in range(len(usua)):
                                    if usua[j].is_active == True:  
                                        if prof[i].email ==usua[j].email:                                           
                                            usua[j].email=nuevo.email
                                            usua[j].nombre=nuevo.nombre
                                            usua[j].apellido=nuevo.apellido                                             
                                            usua[j].save() 
                                            form.save()                                           
                                            mensaje = f'{self.model.__name__} registrado correctamente!'
                                            error = 'No hay error!'
                                            response = JsonResponse({'mensaje':mensaje,'error':error})
                                            response.status_code = 201
                                            return response
                                
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else: 
            return redirect('libro:inicio_profesores')            

class CrearProfesor(ValidarAdministrador,CreateView):
    model = Profesor
    second_model = Alumno
    form_class = ProfesorForm
    third_model = Usuario
    third_form_class = FormularioUsuario
    fourth_model = Administrador
    fourth_form_class = AdministradorForm
    template_name = 'libro/profesor/crear_profesor.html'
    permission_required = ('libro.view_profesor', 'libro.add_profesor',
                           'libro.delete_profesor', 'libro.change_profesor') 
    

    def get_context_data(self, **kwargs):
        context = super(CrearProfesor, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.third_form_class(self.request.GET)
        return context

    def post(self,request,*args,**kwargs):
        a=0
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES)
            form2 = self.third_form_class(data = request.POST,files = request.FILES)
            if form.is_valid() and form2.is_valid():
                nuevo= Profesor(
                    dni=form.cleaned_data.get('dni'),
                    email=form.cleaned_data.get('email')
                )

                profesor = self.model.objects.all()
                alumno = self.second_model.objects.all()
                administrador = self.fourth_model.objects.all()

                for k in range(len(administrador)):
                    if administrador[k].estado == True:
                        if nuevo.email == administrador[k].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response

                for i in range(len(profesor)):
                    if profesor[i].estado == True:
                        if nuevo.dni == profesor[i].dni or nuevo.email == profesor[i].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response

                for j in range(len(alumno)):
                    if alumno[j].estado == True:
                        if nuevo.dni == alumno[j].dni or nuevo.email == alumno[j].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response
               
                if a==0:
                    form.save()
                    form2.save()    

                    prof = self.model.objects.all()
                    usua = self.third_model.objects.all()
                    for j in range(len(usua)):
                        if usua[j].is_active == True:
                            if nuevo.email == usua[j].email:
                                for i in range(len(prof)):
                                    if prof[i].estado == True:                                                       
                                        if nuevo.email == prof[i].email:
                                            prof[i].id_usuario = usua[j]
                                            prof[i].notificacion = True
                                            usua[j].tipo = 'Profesor'  
                                            usua[j].save()                                       
                                            prof[i].save()                                          
                                            mensaje = f'{self.model.__name__} registrado correctamente!'
                                            error = 'No hay error!'
                                            response = JsonResponse({'mensaje':mensaje,'error':error})
                                            response.status_code = 201
                                            return response
                
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else:
            return  redirect ( 'libro: inicio_profesor' )

class EliminarProfesor(ValidarAdministrador,DeleteView):
    model = Profesor
    template_name = 'libro/profesor/eliminar_profesor.html'
    permission_required = ('libro.view_profesor', 'libro.add_profesor',
                           'libro.delete_profesor', 'libro.change_profesor') 

    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            profesor = self.get_object()
            profesor.estado = False
            profesor.save()
            mensaje = f'{self.model.__name__} eliminacion correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje':mensaje,'error':error})
            response.status_code = 201
            return response            
        else: 
            return redirect('libro:inicio_profesor')


class CrearEntrega(ValidarAdministrador,CreateView):
    model = Entrega_libro
    form_class = Entrega_libroForm
    second_model = Reserva
    #third_form_class = FormularioUsuario
    template_name = 'libro/entrega/crear_entrega_libro.html'
    permission_required = ('libro.view_entrega_libro', 'libro.add_entrega_libro',
                           'libro.delete_entrega_libro', 'libro.change_entrega_libro')
    
    def get_context_data(self, **kwargs):
        context = super(CrearEntrega, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        #if 'form2' not in context:
         #   context['form2'] = self.third_form_class(self.request.GET)
        return context

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES)
            
            if form.is_valid():
                nuevo= Entrega_libro(
                    id_reserva=form.cleaned_data.get('id_reserva'),                                    
                )
                reserva = self.second_model.objects.all()
                for i in range(len(reserva)):
                    if reserva[i] == nuevo.id_reserva:
                        reserva[i].estado = False
                        reserva[i].save()
                        form.save() 
                
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else:
            return  redirect ( 'libro: Inicio_entrega' )

class CrearEntregaAdministrador(ValidarAdministrador,CreateView):
    model = Entrega_libro_Administrador
    form_class = Entrega_libroAdministradorForm
    second_model = Libro
    third_model = Usuario 
    fourth_model = Reserva
    fifth_model= Entrega_libro

    template_name = 'libro/entrega/crear_entrega_libro_administrador.html'
    permission_required = ('libro.view_entrega_libro_administrador', 'libro.add_entrega_libro_administrador',
                           'libro.delete_entrega_libro_administrador', 'libro.change_entrega_libro_administrador')
    
    def get_context_data(self, **kwargs):        
        context = super(CrearEntregaAdministrador, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        #if 'form2' not in context:
         #   context['form2'] = self.third_form_class(self.request.GET)
        return context    
    
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES)
            
            if form.is_valid():
                nuevo= Entrega_libro_Administrador(
                    id_usuario=form.cleaned_data.get('id_usuario'),
                    id_libro=form.cleaned_data.get('id_libro'),
                    fecha_entrega=form.cleaned_data.get('fecha_entrega'),                                    
                    estado_libro=form.cleaned_data.get('estado_libro')
                )
                nuevo_reserva= Reserva(                    
                    libro=form.cleaned_data.get('id_libro'),
                    usuario=form.cleaned_data.get('id_usuario')
                )
                
                libro = self.second_model.objects.all()
                reserva = self.fourth_model.objects.all()
                #entrega_libro = self.fifth_model.objects.all()
                for i in range(len(libro)):
                    if libro[i] == nuevo.id_libro:
                        libro[i].cantidad = libro[i].cantidad - 1
                        libro[i].cant_pedido = libro[i].cant_pedido + 1
                        libro[i].save()
                        form.save() 
                        nuevo_reserva.save()               
                  
                        
                for j in range(len(reserva)):
                    if reserva[j].estado == True:
                        if reserva[j] == nuevo_reserva:
                            nuevo_entrega_libro= Entrega_libro(
                                id_reserva=reserva[j],
                                fecha_entrega=form.cleaned_data.get('fecha_entrega'),
                                estado_libro=form.cleaned_data.get('estado_libro')
                            )
                            nuevo_entrega_libro.save()
                            reserva[j].estado = False
                            reserva[j].save()                           
                
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else:
            return  redirect ( 'libro: inicio_entrega' )

class ListadoEntrega(ValidarAdministrador,View):    
    model = Entrega_libro
    permission_required = ('libro.view_entrega_libro', 'libro.add_entrega_libro',
                           'libro.delete_entrega_libro', 'libro.change_entrega_libro')
 

    def get_queryset(self):
        
        return self.model.objects.filter(estado = True)  

    def get_context_data(self,**kwargs):
        
        
        contexto= {}
        contexto ['entrega_libro'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('libro:inicio_entrega')   

class ListadoEntregaAdministrador(ValidarAdministrador,View):    
    model = Entrega_libro_Administrador
    permission_required = ('libro.view_entrega_libro_administrador', 'libro.add_entrega_libro_administrador',
                           'libro.delete_entrega_libro_administrador', 'libro.change_entrega_libro_administrador')

    def get_queryset(self):
        
        return self.model.objects.filter(estado = True)  

    def get_context_data(self,**kwargs):
        
        
        contexto= {}
        contexto ['entrega_libro_administrador'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('libro:inicio_entrega_administrador')         

class ActualizarEntrega(ValidarAdministrador,UpdateView):
    
    model = Entrega_libro
    form_class = Entrega_libro2Form
    second_model = Reserva

    third_model = Usuario    
    #fourth_model = Inscripcion
    #fifth_model= Alumno
    #sixth_model=InscripcionExamen
    #seventh_model = Profesor
    #eighth_model = InscripcionProfesor
    #nineth_model = Materia

    template_name = 'libro/entrega/entrega_libro.html'
    permission_required = ('libro.view_entrega_libro', 'libro.add_entrega_libro',
                           'libro.delete_entrega_libro', 'libro.change_entrega_libro')
    
    #reserva=self.second_model.objects.filter(usuario=self.request.user,estado = True)
    
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES,instance = self.get_object())
            if form.is_valid():
                nuevo= Entrega_libro(
                    #id_entrega_libro = form.instance.id,
                    #id_reserva=form.cleaned_data.get('id_reserva'),
                    fecha_entrega=form.cleaned_data.get('fecha_entrega'), 
                    estado_libro=form.cleaned_data.get('estado_libro')                                 
                )
                print(form.instance.id)
                """aux = self.model.objects.all()
                reserva = self.second_model.objects.all()
                for j in range(len(aux)):
                    if aux[j].id == form.instance.id:
                        for i in range(len(reserva)):
                            if reserva[i] == aux[j].id_reserva:
                                reserva[i].estado = True
                                reserva[i].save()

                for i in range(len(reserva)):
                    if reserva[i] == nuevo.id_reserva:
                        reserva[i].estado = False
                        reserva[i].save()
                        #form.save()"""

                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else: 
            return redirect('libro:inicio_entrega')

class ActualizarEntregaAdministrador(ValidarAdministrador,UpdateView):
    
    model = Entrega_libro_Administrador
    form_class = Entrega_libro_Administrador2Form
    second_model = Reserva
    fifth_model= Entrega_libro
    form_class2 = Entrega_libroForm

    third_model = Usuario    
    #fourth_model = Inscripcion
    #fifth_model= Alumno
    #sixth_model=InscripcionExamen
    #seventh_model = Profesor
    #eighth_model = InscripcionProfesor
    #nineth_model = Materia

    template_name = 'libro/entrega/entrega_libro_administrador.html'
    permission_required = ('libro.view_entrega_libro_administrador', 'libro.add_entrega_libro_administrador',
                           'libro.delete_entrega_libro_administrador', 'libro.change_entrega_libro_administrador')
    
    #reserva=self.second_model.objects.filter(usuario=self.request.user,estado = True)
    def get_context_data(self, **kwargs):
        context = super(ActualizarEntregaAdministrador, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context 

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES,instance = self.get_object())
            if form.is_valid():
                nuevo= Entrega_libro(
                    fecha_entrega=form.cleaned_data.get('fecha_entrega'), 
                    estado_libro=form.cleaned_data.get('estado_libro')                                 
                )

                form.save()
                #form2.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else: 
            return redirect('libro:inicio_entrega_administrador')
    
class EliminarEntrega(ValidarAdministrador,DeleteView):
    
    model = Entrega_libro
    template_name = 'libro/entrega/eliminar_entrega_libro.html'
    permission_required = ('libro.view_entrega_libro', 'libro.add_entrega_libro',
                           'libro.delete_entrega_libro', 'libro.change_entrega_libro')

    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            entrega_libro = self.get_object()
            entrega_libro.estado = False
            entrega_libro.save()
            mensaje = f'{self.model.__name__} eliminacion correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje':mensaje,'error':error})
            response.status_code = 201
            return response            
        else: 
            return redirect('libro:inicio_entrega')

class EliminarEntregaAdministrador(ValidarAdministrador,DeleteView):
    
    model = Entrega_libro_Administrador
    template_name = 'libro/entrega/eliminar_entrega_libro_administrador.html'
    permission_required = ('libro.view_entrega_libro_administrador', 'libro.add_entrega_libro_administrador',
                           'libro.delete_entrega_libro_administrador', 'libro.change_entrega_libro_administrador')

    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            entrega_libro_administrador = self.get_object()
            entrega_libro_administrador.estado = False
            entrega_libro_administrador.save()
            mensaje = f'{self.model.__name__} eliminacion correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje':mensaje,'error':error})
            response.status_code = 201
            return response            
        else: 
            return redirect('libro:inicio_entrega_administrador')

class CrearEntregaProfesor(ValidarAdministrador,CreateView):
    model = Entrega_libro_Profesor
    form_class = Entrega_libroProfesorForm
    second_model = Libro
    third_model = Profesor 
    fourth_model = Reserva
    fifth_model= Entrega_libro

    template_name = 'libro/entrega_profesor/crear_entrega_libro_profesor.html'
    permission_required = ('libro.view_entrega_libro_profesor', 'libro.add_entrega_libro_profesor',
                           'libro.delete_entrega_libro_profesor', 'libro.change_entrega_libro_profesor')
    
    def get_context_data(self, **kwargs):        
        context = super(CrearEntregaProfesor, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context    
    
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES)
            
            if form.is_valid():
                nuevo= Entrega_libro_Profesor(
                    id_profesor=form.cleaned_data.get('id_profesor'),
                    id_libro=form.cleaned_data.get('id_libro'),
                    cantidad=form.cleaned_data.get('cantidad'),                                    
                    fecha_entrega=form.cleaned_data.get('fecha_entrega')
                )
                
                libro = self.second_model.objects.all()
                for i in range(len(libro)):
                    if libro[i] == nuevo.id_libro:
                        if libro[i].cantidad >= nuevo.cantidad:
                            libro[i].cantidad = libro[i].cantidad - nuevo.cantidad
                            libro[i].cant_pedido = libro[i].cant_pedido + nuevo.cantidad
                            libro[i].save()
                            form.save() 
                        else:
                            mensaje = f'no se ha podido registrar la entrega porque no tiene suficientes libros!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response      
                                          
                
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else:
            return  redirect ( 'libro: inicio_entrega_profesor' )

class ListadoEntregaProfesor(ValidarAdministrador,View):    
    model = Entrega_libro_Profesor
    permission_required = ('libro.view_entrega_libro_profesor', 'libro.add_entrega_libro_profesor',
                           'libro.delete_entrega_libro_profesor', 'libro.change_entrega_libro_profesor')
 

    def get_queryset(self):        
        return self.model.objects.filter(estado = True)  

    def get_context_data(self,**kwargs):       
        contexto= {}
        contexto ['entrega_libro_profesor'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('libro:inicio_entrega_profesor')  

class ActualizarEntregaProfesor(ValidarAdministrador,UpdateView):    
    model = Entrega_libro_Profesor
    form_class = Entrega_libro_Profesor2Form
    second_model = Libro

    template_name = 'libro/entrega_profesor/entrega_libro_profesor.html'
    permission_required = ('libro.view_entrega_libro_profesor', 'libro.add_entrega_libro_profesor',
                           'libro.delete_entrega_libro_profesor', 'libro.change_entrega_libro_profesor')
    
    
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES,instance = self.get_object())
            if form.is_valid():
                nuevo= Entrega_libro_Profesor(
                    cantidad=form.cleaned_data.get('cantidad'), 
                    fecha_entrega=form.cleaned_data.get('fecha_entrega')                                 
                )
                id_entrega_libro = form.instance.id
                
                entrega_profesor = self.model.objects.all()
                libro = self.second_model.objects.all()

                for i in range(len(entrega_profesor)):
                    if entrega_profesor[i].estado == True:
                        if entrega_profesor[i].id == id_entrega_libro:
                            for j in range(len(libro)):
                                if libro[j].estado == True:
                                    if libro[j] == entrega_profesor[i].id_libro:
                                        if entrega_profesor[i].cantidad < nuevo.cantidad:
                                            aux = libro[j].cantidad + entrega_profesor[i].cantidad
                                            aux2 = libro[j].cant_pedido - entrega_profesor[i].cantidad
                                            if aux >= nuevo.cantidad:
                                                libro[j].cantidad = aux - nuevo.cantidad
                                                libro[j].cant_pedido = aux2 + nuevo.cantidad
                                                libro[j].save()
                                                form.save()  
                                                mensaje = f'{self.model.__name__} actualizado correctamente!'
                                                error = 'No hay error!'
                                                response = JsonResponse({'mensaje':mensaje,'error':error})
                                                response.status_code = 201
                                                return response
                                            else: 
                                                mensaje = f'{self.model.__name__} no se ha podido actualizar porque la cantidad de libros no son suficentes!'
                                                error = form.errors
                                                response = JsonResponse({'mensaje':mensaje,'error':error})
                                                response.status_code = 400
                                                return response

                                        if entrega_profesor[i].cantidad > nuevo.cantidad:
                                            aux3 = libro[j].cantidad + entrega_profesor[i].cantidad
                                            aux4 = libro[j].cant_pedido - entrega_profesor[i].cantidad
                                            if aux3 >= nuevo.cantidad:
                                                libro[j].cantidad = aux3 - nuevo.cantidad
                                                libro[j].cant_pedido = aux4 + nuevo.cantidad
                                                libro[j].save()
                                                form.save()
                                                mensaje = f'{self.model.__name__} actualizado correctamente!'
                                                error = 'No hay error!'
                                                response = JsonResponse({'mensaje':mensaje,'error':error})
                                                response.status_code = 201
                                                return response                                                                    

                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else: 
            return redirect('libro:inicio_entrega_profesor')

class EliminarEntregaProfesor(ValidarAdministrador,DeleteView):
    
    model = Entrega_libro_Profesor
    second_model = Libro
    template_name = 'libro/entrega_profesor/eliminar_entrega_libro_profesor.html'
    permission_required = ('libro.view_entrega_libro_profesor', 'libro.add_entrega_libro_profesor',
                           'libro.delete_entrega_libro_profesor', 'libro.change_entrega_libro_profesor')

    def delete(self,request,pk,*args,**kwargs):
        
        if request.is_ajax():
            entrega_libro_profesor = self.get_object()
            libro = self.second_model.objects.all()

            for j in range(len(libro)):
                if libro[j].estado == True:
                    if libro[j] == entrega_libro_profesor.id_libro:
                        libro[j].cantidad = libro[j].cantidad + entrega_libro_profesor.cantidad
                        libro[j].cant_pedido = libro[j].cant_pedido - entrega_libro_profesor.cantidad
                        libro[j].save()    
                        entrega_libro_profesor.estado = False
                        entrega_libro_profesor.save()
                        mensaje = f'{self.model.__name__} eliminacion correctamente!'
                        error = 'No hay error!'
                        response = JsonResponse({'mensaje':mensaje,'error':error})
                        response.status_code = 201
                        return response            
        else: 
            return redirect('libro:inicio_entrega_profesor')

class CrearDevolucion(ValidarAdministrador,CreateView):
    model = Devolucion_libro
    form_class = Devolucion_libroForm
    second_model = Entrega_libro
    third_model = Reserva
    fourth_model = Usuario
    fifth_model = Libro
    sixth_model = Alumno_Sancionado
    #second_form_class = AlumnoForm
    #third_model = Usuario
    #third_form_class = FormularioUsuario
    template_name = 'libro/devolucion/crear_devolucion_libro.html'
    permission_required = ('libro.view_devolucion_libro', 'libro.add_devolucion_libro',
                           'libro.delete_devolucion_libro', 'libro.change_devolucion_libro')
    
    def get_context_data(self, **kwargs):
        context = super(CrearDevolucion, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        #if 'form2' not in context:
         #   context['form2'] = self.third_form_class(self.request.GET)
        return context
    

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES) 
            #form = self.form_class(data = request.POST,files = request.FILES)
            #form2 = self.third_form_class(data = request.POST,files = request.FILES)           
            if form.is_valid():
                nuevo= Devolucion_libro(
                    id_entrega=form.cleaned_data.get('id_entrega'),
                    fecha_devolucion=form.cleaned_data.get('fecha_devolucion'),
                    estado_libro=form.cleaned_data.get('estado_libro')                                     
                )
                devolucion_libro = self.model.objects.all()
                entrega_libro = self.second_model.objects.all()
                reserva = self.third_model.objects.all()
                usuario = self.fourth_model.objects.all()
                libro = self.fifth_model.objects.all()
                for k in range(len(entrega_libro)):
                    if entrega_libro[k].estado == True:
                        if nuevo.id_entrega == entrega_libro[k]:
                            for i in range(len(reserva)):
                                if entrega_libro[k].id_reserva == reserva[i]:
                                    for j in range(len(usuario)):
                                        if usuario[j].is_active == True:
                                            if reserva[i].usuario == usuario[j]:
                                                for l in range(len(libro)):
                                                    if libro[l].estado == True:
                                                        if libro[l] == reserva[i].libro:
                                                            if usuario[j].tipo == "Alumno":
                                                                alumno_sancionado= Alumno_Sancionado(
                                                                    id_usuario=usuario[j],
                                                                    id_libro=libro[l],
                                                                    estado_libro=nuevo.estado_libro                                     
                                                                )
                                                                if entrega_libro[k].estado_libro == nuevo.estado_libro:
                                                                    libro[l].cantidad = libro[l].cantidad + 1
                                                                    libro[l].save()
                                                                    entrega_libro[k].estado=False
                                                                    entrega_libro[k].save()
                                                                    form.save()
                                                                    print("entro al mismo estado de libro")
                                                                    mensaje = f'{self.model.__name__} registrado correctamente!'
                                                                    error = 'No hay error!'
                                                                    response = JsonResponse({'mensaje':mensaje,'error':error})
                                                                    response.status_code = 201
                                                                    return response

                                                                if entrega_libro[k].estado_libro == "Buena" and nuevo.estado_libro == "Mala" or nuevo.estado_libro == "Perdido":
                                                                    alumno_sancionado.save()
                                                                    libro[l].cantidad = libro[l].cantidad + 1
                                                                    libro[l].save()
                                                                    entrega_libro[k].estado=False
                                                                    entrega_libro[k].save()
                                                                    form.save()
                                                                    print("entro al bueno y malo o perdido")
                                                                    mensaje = f'{self.model.__name__} registrado correctamente y el alumno sara notificado por no devolver el libro en las misma condiciones que se le entrego!'
                                                                    error = 'No hay error!'
                                                                    response = JsonResponse({'mensaje':mensaje,'error':error})
                                                                    response.status_code = 201
                                                                    return response
                                                                
                                                                if entrega_libro[k].estado_libro == "Mala" and nuevo.estado_libro == "Perdido":
                                                                    alumno_sancionado.save()
                                                                    libro[l].cantidad = libro[l].cantidad + 1
                                                                    libro[l].save()
                                                                    entrega_libro[k].estado=False
                                                                    entrega_libro[k].save()
                                                                    form.save()
                                                                    print("entro al malo y perdido")
                                                                    mensaje = f'{self.model.__name__} registrado correctamente y el alumno sara notificado por no devolver el libro que se le entrego!'
                                                                    error = 'No hay error!'
                                                                    response = JsonResponse({'mensaje':mensaje,'error':error})
                                                                    response.status_code = 201
                                                                    return response
                                                            else: 
                                                                libro[l].cantidad = libro[l].cantidad + 1
                                                                libro[l].save()
                                                                entrega_libro[k].estado=False
                                                                entrega_libro[k].save()
                                                                form.save()
                                                                print("entro al malo y perdido")
                                                                mensaje = f'{self.model.__name__} registrado correctamente!'
                                                                error = 'No hay error!'
                                                                response = JsonResponse({'mensaje':mensaje,'error':error})
                                                                response.status_code = 201
                                                                return response

                                                            
                
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else:
            return  redirect ( 'libro: Inicio_devolucion' )

class ListadoDevolucion(ValidarAdministrador,View):    
    model = Devolucion_libro
    permission_required = ('libro.view_devolucion_libro', 'libro.add_devolucion_libro',
                           'libro.delete_devolucion_libro', 'libro.change_devolucion_libro')
 

    def get_queryset(self):
        
        return self.model.objects.filter(estado = True)  

    def get_context_data(self,**kwargs):
        
        
        contexto= {}
        contexto ['devolucion_libro'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('libro:inicio_devolucion')        

class ActualizarDevolucion(ValidarAdministrador,UpdateView):
    
    model = Devolucion_libro
    form_class = Devolucion_libro2Form
    template_name = 'libro/devolucion/devolucion_libro.html'
    permission_required = ('libro.view_devolucion_libro', 'libro.add_devolucion_libro',
                           'libro.delete_devolucion_libro', 'libro.change_devolucion_libro')
    
    def get_context_data(self, **kwargs):
        context = super(ActualizarDevolucion, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else: 
            return redirect('libro:inicio_devolucion')
    
class EliminarDevolucion(ValidarAdministrador,DeleteView):
    
    model = Devolucion_libro
    template_name = 'libro/devolucion/eliminar_devolucion_libro.html'
    permission_required = ('libro.view_devolucion_libro', 'libro.add_devolucion_libro',
                           'libro.delete_devolucion_libro', 'libro.change_devolucion_libro')

    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            devolucion_libro = self.get_object()
            devolucion_libro.estado = False
            devolucion_libro.save()
            mensaje = f'{self.model.__name__} eliminacion correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje':mensaje,'error':error})
            response.status_code = 201
            return response            
        else: 
            return redirect('libro:inicio_devolucion')

class CrearDevolucionProfesor(ValidarAdministrador,CreateView):
    model = Devolucion_libro_Profesor
    form_class = Devolucion_libro_profesorForm
    second_model = Entrega_libro_Profesor
    third_model = Libro
    #fourth_model = Usuario
    #second_form_class = AlumnoForm
    #third_model = Usuario
    #third_form_class = FormularioUsuario
    template_name = 'libro/devolucion_profesor/crear_devolucion_libro_profesor.html'
    permission_required = ('libro.view_devolucion_libro_profesor', 'libro.add_devolucion_libro_profesor',
                           'libro.delete_devolucion_libro_profesor', 'libro.change_devolucion_libro_profesor')
    
    def get_context_data(self, **kwargs):
        context = super(CrearDevolucionProfesor, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        #if 'form2' not in context:
         #   context['form2'] = self.third_form_class(self.request.GET)
        return context
    

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES) 
            #form = self.form_class(data = request.POST,files = request.FILES)
            #form2 = self.third_form_class(data = request.POST,files = request.FILES)           
            if form.is_valid():
                nuevo= Devolucion_libro_Profesor(
                    id_entrega_profesor=form.cleaned_data.get('id_entrega_profesor'),
                    fecha_devolucion=form.cleaned_data.get('fecha_devolucion'),
                    cantidad=form.cleaned_data.get('cantidad')                                     
                )
                devolucion_libro_profesor = self.model.objects.all()
                entrega_libro_profesor = self.second_model.objects.all()
                libro = self.third_model.objects.all()
                #usuario = self.fourth_model.objects.all()
                for k in range(len(entrega_libro_profesor)):
                    if entrega_libro_profesor[k].estado == True:
                        if nuevo.id_entrega_profesor == entrega_libro_profesor[k]:
                            if entrega_libro_profesor[k].cantidad > nuevo.cantidad:
                                mensaje = f' no se ha podido registrar la devolucion porque no se devolvieron todos los libros entregados!'
                                error = form.errors
                                response = JsonResponse({'mensaje':mensaje,'error':error})
                                response.status_code = 400
                                return response
                            
                            if entrega_libro_profesor[k].cantidad < nuevo.cantidad:
                                mensaje = f'no se ha podido registrar la devolucion porque estan devolviendo mas libros de los que se entregaron!'
                                error = form.errors
                                response = JsonResponse({'mensaje':mensaje,'error':error})
                                response.status_code = 400
                                return response

                            if entrega_libro_profesor[k].cantidad == nuevo.cantidad:
                                for j in range(len(libro)):
                                    if libro[j].estado == True:
                                        if libro[j] == entrega_libro_profesor[k].id_libro:
                                            libro[j].cantidad = libro[j].cantidad + nuevo.cantidad
                                            libro[j].save()
                                            entrega_libro_profesor[k].estado=False
                                            entrega_libro_profesor[k].save()
                                            form.save()
                                            mensaje = f'Devolucion de libros registrado correctamente!'
                                            error = 'No hay error!'
                                            response = JsonResponse({'mensaje':mensaje,'error':error})
                                            response.status_code = 201
                                            return response 
                            
                
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else:
            return  redirect ( 'libro: Inicio_devolucion_profesor' )

class ListadoDevolucionProfesor(ValidarAdministrador,View):    
    model = Devolucion_libro_Profesor
    permission_required = ('libro.view_devolucion_libro_profesor', 'libro.add_devolucion_libro_profesor',
                           'libro.delete_devolucion_libro_profesor', 'libro.change_devolucion_libro_profesor')
 

    def get_queryset(self):
        
        return self.model.objects.filter(estado = True)  

    def get_context_data(self,**kwargs):
        
        
        contexto= {}
        contexto ['devolucion_libro_profesor'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('libro:inicio_devolucion_profesor') 

class ActualizarDevolucionProfesor(ValidarAdministrador,UpdateView):
    
    model = Devolucion_libro_Profesor
    form_class = Devolucion_libro_profesor2Form
    template_name = 'libro/devolucion_profesor/devolucion_libro_profesor.html'
    permission_required = ('libro.view_devolucion_libro_profesor', 'libro.add_devolucion_libro_profesor',
                           'libro.delete_devolucion_libro_profesor', 'libro.change_devolucion_libro_profesor')
    
    def get_context_data(self, **kwargs):
        context = super(ActualizarDevolucionProfesor, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else: 
            return redirect('libro:inicio_devolucion_profesor')

class EliminarDevolucionProfesor(ValidarAdministrador,DeleteView):
    
    model = Devolucion_libro_Profesor
    second_model = Entrega_libro_Profesor
    third_model = Libro
    template_name = 'libro/devolucion_profesor/eliminar_devolucion_libro_profesor.html'
    permission_required = ('libro.view_devolucion_libro_profesor', 'libro.add_devolucion_libro_profesor',
                           'libro.delete_devolucion_libro_profesor', 'libro.change_devolucion_libro_profesor')

    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            devolucion_libro_profesor = self.get_object()

            entrega_libro_profesor = self.second_model.objects.all()
            libro = self.third_model.objects.all()

            for k in range(len(entrega_libro_profesor)):
                if entrega_libro_profesor[k] == devolucion_libro_profesor.id_entrega_profesor:   
                    for j in range(len(libro)):
                        if libro[j].estado == True:
                            if libro[j] == entrega_libro_profesor[k].id_libro:
                                #libro[j].cantidad = libro[j].cantidad + nuevo.cantidad
                                #libro[j].save()
                                #entrega_libro_profesor[k].estado=False
                                #entrega_libro_profesor[k].save()
                                #form.save()
                                a

            devolucion_libro_profesor.estado = False
            devolucion_libro_profesor.save()
            mensaje = f'{self.model.__name__} eliminacion correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje':mensaje,'error':error})
            response.status_code = 201
            return response            
        else: 
            return redirect('libro:inicio_devolucion_profesor')

class EstadoAlumno(ValidarAlumno,View):
    model = Alumno
    #second_model = Usuario
    permission_required = ('libro.view_alumno', 'libro.add_alumno',
                           'libro.delete_alumno', 'libro.change_alumno')  
    
    def get_queryset(self):
        return self.model.objects.filter(id_usuario=self.request.user,estado = True)  

    def get_context_data(self):
        pk = self.kwargs.get('pk')
        alumno = self.model.objects.get(pk= pk)
        return alumno
    #def get_context_data(self,**kwargs):
     #   contexto= {}
      #  contexto ['alumnos'] = self.get_queryset()
       # contexto['form'] = self.form_class
        #return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('libro:inicio_alumnos')

class EstadoProfesor(ValidarProfesorP,View):
    model = Profesor
    permission_required = ('libro.view_profesor', 'libro.add_profesor',
                           'libro.delete_profesor', 'libro.change_profesor')  
    
    def get_queryset(self):
        return self.model.objects.filter(id_usuario=self.request.user,estado = True)  

    def get_context_data(self):
        pk = self.kwargs.get('pk')
        profesor = self.model.objects.get(pk= pk)
        return profesor

    
    #def get_context_data(self,**kwargs):
     #   contexto= {}
      #  contexto ['alumnos'] = self.get_queryset()
       # contexto['form'] = self.form_class
        #return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('libro:inicio_profesores')


class LibrosMasPedido(ValidarAdministrador,View):    
    model = Libro
    permission_required = ('libro.view_libro', 'libro.add_libro',
                           'libro.delete_libro', 'libro.change_libro')  

    def get_queryset(self):

        libro = self.model.objects.all() 
        
        contexto =[]
        for i in range(len(libro)):
            if libro[i].estado == True:
                if libro[i].cant_pedido >= 1:
                    
                    #return self.model.objects.filter(estado = True) 
                    #return self.model.objects.filter(estado = True,cant_pedido = libro[i].cant_pedido) 
                    #contexto[''] = libro[i]
                    #contexto.append({self.model.objects.filter(estado = True,cant_pedido = libro[i].cant_pedido)}) 
                    contexto.append(libro[i])  
                 
        return contexto


    def get_context_data(self,**kwargs):
        
        contexto= {}
        contexto ['libros'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('libro:inicio_libros_mas_pedido')


class LibrosMenosPedido(ValidarAdministrador,View):    
    model = Libro
    permission_required = ('libro.view_libro', 'libro.add_libro',
                           'libro.delete_libro', 'libro.change_libro')  

    def get_queryset(self):

        libro = self.model.objects.all() 
        
        contexto =[]
        for i in range(len(libro)):
            if libro[i].estado == True:
                if libro[i].cant_pedido == 0:
                    
                    #return self.model.objects.filter(estado = True) 
                    #return self.model.objects.filter(estado = True,cant_pedido = libro[i].cant_pedido) 
                    #contexto[''] = libro[i]
                    #contexto.append({self.model.objects.filter(estado = True,cant_pedido = libro[i].cant_pedido)}) 
                    contexto.append(libro[i])  
                 
        return contexto


    def get_context_data(self,**kwargs):
        
        contexto= {}
        contexto ['libros'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('libro:inicio_libros_menos_pedido')

class ListadoAlumnosSancionados(ValidarAdministrador,View):
    model = Alumno_Sancionado
    permission_required = ('libro.view_alumno_sancionado', 'libro.add_alumno_sancionado',
                           'libro.delete_alumno_sancionado', 'libro.change_alumno_sancionado') 

    def get_queryset(self):
        return self.model.objects.filter(estado = True)  

    def get_context_data(self,**kwargs):
        contexto= {}
        contexto ['alumno_sancionado'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('libro:inicio_alumno_sancionados')

class EliminarAlumnoSancionado(ValidarAdministrador,DeleteView):    
    model = Alumno_Sancionado
    template_name = 'libro/eliminar_alumno_sancionado.html'
    permission_required = ('libro.view_alumno_sancionado', 'libro.add_alumno_sancionado',
                           'libro.delete_alumno_sancionado', 'libro.change_alumno_sancionado') 

    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            alumno_sancionado = self.get_object()
            alumno_sancionado.estado = False
            alumno_sancionado.save()
            mensaje = f'{self.model.__name__} eliminacion correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje':mensaje,'error':error})
            response.status_code = 201
            return response            
        else: 
            return redirect('libro:inicio_alumno_sancionados')

class ActualizarAlumnoSancionado(ValidarAdministrador,UpdateView):    
    model = Alumno_Sancionado
    form_class = Alumno_SancionadoForm
    template_name = 'libro/editar_alumno_sancionado.html'
    permission_required = ('libro.view_alumno_sancionado', 'libro.add_alumno_sancionado',
                           'libro.delete_alumno_sancionado', 'libro.change_alumno_sancionado') 
    
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else: 
            return redirect('libro:inicio_alumno_sancionados')

class MensajeAlumno(ValidarProfesor,DetailView):
    template_name = 'libro/mensaje/mensaje_alumno.html'
    model = Alumno
    
    def post(self,request,*args,**kwargs):                 
        pk = self.kwargs.get('pk')
        alumno = self.model.objects.filter(id_alumno= pk) 

        if request.method == "POST":
            asunto = request.POST["txtAsunto"]
            mensaje = request.POST["txtMensaje"]
            email_desde = settings.EMAIL_HOST_USER

        for i in range(len(alumno)):
            if alumno[i].estado == True:
                if alumno[i].id_alumno == pk:
                    print ("entro")
                    print(asunto)
                    print(mensaje)
                    print(email_desde)
                    print(alumno[i].email)

                    email_para= "sistema.academico.ipes@gmail.com",alumno[i].email
                    send_mail(asunto,mensaje,email_desde,email_para, fail_silently=False)
                                                        
        return render(request,'libro/alumnos_sancionados.html')

class ListadoNuevosLibros(LoginMixin,ListView):    
    model = Libro
    paginate_by = 6
    #template_name = 'libro/libros_disponibles.html'
    template_name = 'libro/libro/listar_libros_nuevos.html'
    permission_required = ('libro.view_libro', 'libro.add_libro',
                           'libro.delete_libro', 'libro.change_libro')      
    
    def get_queryset(self):
        #
        #print (queryset)
        
        queryset =self.request.GET.get("buscar")

        if queryset is None:
            ahora = datetime.date.today()
            ayer = ahora - datetime.timedelta(days=14) 
            mañana = ahora + datetime.timedelta(days=14)
            
            queryset = self.model.objects.filter(estado = True,cantidad__gte = 1,fecha_publicacion__gte = ayer,fecha_publicacion__lte = mañana)
           
            return queryset
        else:
            ahora = datetime.date.today()
            ayer = ahora - datetime.timedelta(days=14) 
            mañana = ahora + datetime.timedelta(days=14)
            
            libro = self.model.objects.filter(estado = True,cantidad__gte = 1,fecha_publicacion__gte = ayer,fecha_publicacion__lte = mañana)
            
            if queryset:
                libro = Libro.objects.filter(
                    Q(titulo__icontains = queryset), #|
                    #Q(descripcion_icontains = queryset),
                    estado = True,
                    cantidad__gte = 1,
                    fecha_publicacion__gte = ayer,
                    fecha_publicacion__lte = mañana
                ).distinct()  
                return libro
            return libro
        #return render(request,'index.html',{'libro':libro})
        

    #def buscar(self,request):
     #def buscar(request):
    """def get(self,request,*args,**kwargs):
        ahora = datetime.date.today()
        ayer = ahora - datetime.timedelta(days=14) 
        mañana = ahora + datetime.timedelta(days=14)
        print("entro")
        #if request.is_ajax():   
        print("entro2")
        queryset =self.request.GET.get("buscar")
        print (queryset)

        libro = self.model.objects.filter(estado = True,cantidad__gte = 1,fecha_publicacion__gte = ayer,fecha_publicacion__lte = mañana)
        if queryset:
            libro = Libro.objects.filter(
                Q(titulo__icontains = queryset) #|
                #Q(descripcion_icontains = queryset),
            ).distinct()
        return render(request,'libro/libro/listar_libros_nuevos.html',{'libro':libro}) 


        return render(request,'libro/libro/listar_libros_nuevos.html') 
    """

"""
    def get_queryset(self):  
        libro = self.model.objects.all() 
        ahora = datetime.date.today()
        ayer = ahora - datetime.timedelta(days=14) 
        mañana = ahora + datetime.timedelta(days=14)                
        contexto =[]
        for i in range(len(libro)):
            if libro[i].estado == True: 
                if libro[i].fecha_publicacion >= ayer and libro[i].fecha_publicacion <= mañana:  
                    contexto.append(libro[i])  
        return contexto

        #return self.model.objects.filter(estado = True, fecha_publicacion__gte=mañana,fecha_publicacion__lte=20)  

    def get_context_data(self,**kwargs):
        
        contexto= {}
        contexto ['libros'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax(): 

            
            #if ahora < fecha[i].fecha_evento:
             #   dias_dies = fecha[i].fecha_evento - datetime.timedelta(days=10)
              #  dias_dos = fecha[i].fecha_evento - datetime.timedelta(days=2)                                
               # if ahora >= dias_dies and ahora < dias_dos:         
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('libro:inicio_libros_nuevos')

"""
class DetalleLibroDiponibleNuevo(LoginMixin,DetailView):
    model = Libro
    template_name = 'libro/libro/detalle_libro_disponible_nuevo.html'

    def get(self,request,*agrs,**kwargs):
        #libro = self.get_object()
        if self.get_object().cantidad >= 0:            
            return render(request,self.template_name,{'object':self.get_object()})
        else:
            return redirect('libro:listado_libros_nuevos')

        return redirect('libro:listado_libros_nuevos')


class RegistrarReservaNuevo(LoginMixin,CreateView):
    model = Reserva
    second_model = Libro
    success_url = reverse_lazy('libro:listado_libros_nuevos')

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            libro = Libro.objects.filter(id = request.POST.get('libro')).first()
            usuario = Usuario.objects.filter(id = request.POST.get('usuario')).first()
            if libro and usuario:
                if libro.cantidad > 0:
                    nueva_reserva = self.model(
                        libro = libro,
                        usuario = usuario
                    )
                    libro.cant_pedido = libro.cant_pedido + 1
                    libro.cantidad = libro.cantidad - 1
                    libro.save()

                    nueva_reserva.save()
                    mensaje = f'{self.model.__name__} registrada correctamente!'
                    error = 'No hay error!'
                    response = JsonResponse({'mensaje': mensaje, 'error': error,'url':self.success_url})
                    response.status_code = 201
                    return response
        return redirect('libro:listado_libros_nuevos')