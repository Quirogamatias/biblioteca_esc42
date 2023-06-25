from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *
#from .formsets import FormsetAutor

urlpatterns = [  
    path('inicio_alumno/',InicioAlumno.as_view(), name = 'inicio_alumno'),
    path('inicio_alumnos/',InicioAlumnos.as_view(), name = 'inicio_alumnos'),
    path('crear_alumno/',login_required(CrearAlumno.as_view()), name = 'crear_alumno'),
    path('listar_alumnos/',login_required(ListadoAlumnos.as_view()),name = 'listado_alumnos'),
    path('editar_alumno/<int:pk>/',login_required(ActualizarAlumno.as_view()),name = 'editar_alumno'),
    path('editar_alumnoA/<int:pk>/',login_required(ActualizarAlumnoA.as_view()),name = 'editar_alumnoA'),
    path('eliminar_alumno/<int:pk>/',login_required(EliminarAlumno.as_view()),name = 'eliminar_alumno'),
    path('estado_alumno/',login_required(EstadoAlumno.as_view()),name = 'estado_alumno'),

    path('inicio_administrador/',InicioAdministrador.as_view(), name = 'inicio_administrador'),
    path('crear_administrador/',login_required(CrearAdministrador.as_view()), name = 'crear_administrador'),
    path('listar_administradores/',login_required(ListadoAdministradores.as_view()),name = 'listado_administradores'),
    path('editar_administrador/<int:pk>/',login_required(ActualizarAdministrador.as_view()),name = 'editar_administrador'),
    path('eliminar_administrador/<int:pk>/',login_required(EliminarAdministrador.as_view()),name = 'eliminar_administrador'),

    path('inicio_profesor/',InicioProfesor.as_view(), name = 'inicio_profesor'),
    path('inicio_profesorP/',InicioProfesorP.as_view(), name = 'inicio_profesorP'),
    path('crear_profesor/',login_required(CrearProfesor.as_view()), name = 'crear_profesor'),
    path('listar_profesores/',login_required(ListadoProfesores.as_view()),name = 'listado_profesores'),
    path('estado_profesor/',login_required(EstadoProfesor.as_view()),name = 'estado_profesor'),
    path('editar_profesor/<int:pk>/',login_required(ActualizarProfesor.as_view()),name = 'editar_profesor'),
    path('editar_profesorP/<int:pk>/',login_required(ActualizarProfesorP.as_view()),name = 'editar_profesorP'),
    path('eliminar_profesor/<int:pk>/',login_required(EliminarProfesor.as_view()),name = 'eliminar_profesor'),

    path('inicio_entrega/',InicioEntrega.as_view(), name = 'inicio_entrega'),
    path('crear_entrega_libro/',login_required(CrearEntrega.as_view()), name = 'crear_entrega_libro'),    
    path('listar_entrega_libro/',login_required(ListadoEntrega.as_view()),name = 'listado_entrega'),
    path('editar_entrega_libro/<int:pk>/',login_required(ActualizarEntrega.as_view()),name = 'editar_entrega_libro'),
    path('eliminar_entrega_libro/<int:pk>/',login_required(EliminarEntrega.as_view()),name = 'eliminar_entrega_libro'),

    path('inicio_entrega_administrador/',InicioEntregaAdministrador.as_view(), name = 'inicio_entrega_administrador'),
    path('crear_entrega_libro_administrador/',login_required(CrearEntregaAdministrador.as_view()), name = 'crear_entrega_libro_administrador'), 
    path('listar_entrega_libro_administrador/',login_required(ListadoEntregaAdministrador.as_view()),name = 'listado_entrega_administrador'),
    path('editar_entrega_libro_administrador/<int:pk>/',login_required(ActualizarEntregaAdministrador.as_view()),name = 'editar_entrega_libro_administrador'),
    path('eliminar_entrega_libro_administrador/<int:pk>/',login_required(EliminarEntregaAdministrador.as_view()),name = 'eliminar_entrega_libro_administrador'),

    path('inicio_entrega_profesor/',InicioEntregaProfesor.as_view(), name = 'inicio_entrega_profesor'),
    path('crear_entrega_libro_profesor/',login_required(CrearEntregaProfesor.as_view()), name = 'crear_entrega_libro_profesor'),    
    path('listar_entrega_libro_profesor/',login_required(ListadoEntregaProfesor.as_view()),name = 'listado_entrega_profesor'),
    path('editar_entrega_libro_profesor/<int:pk>/',login_required(ActualizarEntregaProfesor.as_view()),name = 'editar_entrega_libro_profesor'),
    path('eliminar_entrega_libro_profesor/<int:pk>/',login_required(EliminarEntregaProfesor.as_view()),name = 'eliminar_entrega_libro_profesor'),


    path('inicio_devolucion/',InicioDevolucion.as_view(), name = 'inicio_devolucion'),
    path('crear_devolucion_libro/',login_required(CrearDevolucion.as_view()), name = 'crear_devolucion_libro'),
    path('listar_devolucion_libro/',login_required(ListadoDevolucion.as_view()),name = 'listado_devolucion'),
    path('editar_devolucion_libro/<int:pk>/',login_required(ActualizarDevolucion.as_view()),name = 'editar_devolucion_libro'),
    path('eliminar_devolucion_libro/<int:pk>/',login_required(EliminarDevolucion.as_view()),name = 'eliminar_devolucion_libro'),

    path('inicio_devolucion_profesor/',InicioDevolucionProfesor.as_view(), name = 'inicio_devolucion_profesor'),
    path('crear_devolucion_libro_profesor/',login_required(CrearDevolucionProfesor.as_view()), name = 'crear_devolucion_libro_profesor'),
    path('listar_devolucion_libro_profesor/',login_required(ListadoDevolucionProfesor.as_view()),name = 'listado_devolucion_profesor'),
    path('editar_devolucion_libro_profesor/<int:pk>/',login_required(ActualizarDevolucionProfesor.as_view()),name = 'editar_devolucion_libro_profesor'),
    path('eliminar_devolucion_libro_profesor/<int:pk>/',login_required(EliminarDevolucionProfesor.as_view()),name = 'eliminar_devolucion_libro_profesor'),

    #path('inicio_autor/',InicioAutor.as_view(), name = 'inicio_autor'),
    #path('listar_autor/',login_required(ListadoAutor.as_view()),name = 'listar_autor'),  
    #path('crear_autor/',login_required(CrearAutor.as_view()),name='crear_autor'),    
    #path('editar_autor/<int:pk>/',login_required(ActualizarAutor.as_view()),name='editar_autor'),
    #path('eliminar_autor/<int:pk>/',login_required(EliminarAutor.as_view()),name='eliminar_autor'),
    path('inicio_libro/',InicioLibro.as_view(), name = 'inicio_libro'),
    path('listas_libros/', login_required(ListadoLibros.as_view()), name= 'listado_libros'),
    path('crear_libro/', login_required(CrearLibro.as_view()), name= 'crear_libro'),
    path('editar_libro/<int:pk>/', login_required(ActualizarLibro.as_view()), name= 'editar_libro'),
    path('eliminar_libro/<int:pk>/', login_required(EliminarLibro.as_view()), name= 'eliminar_libro'),

    path('inicio_libros_nuevos/',InicioLibrosNuevos.as_view(), name = 'inicio_libros_nuevos'),
    path('listar_libros_nuevos/', login_required(ListadoNuevosLibros.as_view()), name= 'listado_libros_nuevos'),
    path('detalle-libro-nuevo/<int:pk>/',DetalleLibroDiponibleNuevo.as_view(), name = 'detalle_libro_nuevo'),
    path('reservar-libro-nuevo/',RegistrarReservaNuevo.as_view(), name = 'reservar_libro_nuevo'),

    path('inicio_libros_mas_pedido/',InicioLibroMasPedido.as_view(), name = 'inicio_libros_mas_pedido'),
    path('libro_mas_pedido/', login_required(LibrosMasPedido.as_view()), name= 'libro_mas_pedido'),
    path('inicio_libros_menos_pedido/',InicioLibroMenosPedido.as_view(), name = 'inicio_libros_menos_pedido'),
    path('libro_menos_pedido/', login_required(LibrosMenosPedido.as_view()), name= 'libro_menos_pedido'),

    path('inicio_alumno_sancionados/',InicioAlumnosSancionados.as_view(), name = 'inicio_alumno_sancionados'),
    path('alumnos_sancionados/',login_required(ListadoAlumnosSancionados.as_view()),name = 'alumnos_sancionados'),
    path('eliminar_alumno_sancionado/<int:pk>/', login_required(EliminarAlumnoSancionado.as_view()), name= 'eliminar_alumno_sancionado'),
    path('editar_alumno_sancionado/<int:pk>/', login_required(ActualizarAlumnoSancionado.as_view()), name= 'editar_alumno_sancionado'),
    path('mensaje_alumno/<int:pk>/',login_required(MensajeAlumno.as_view()),name = 'mensaje_alumno'),
    
    # URLS GENERALES
    path('inicio_reservas/',InicioReserva.as_view(), name = 'inicio_reservas'),
    path('inicio_reservas_vencidas/',InicioReservaVencida.as_view(), name = 'inicio_reservas_vencidas'),
    path('reservas/',Reservas.as_view(), name = 'reservas'),
    path('eliminar_reserva/<int:pk>/', login_required(EliminarReserva.as_view()), name= 'eliminar_reserva'),
    path('reservas-vencidas/',ReservasVencidas.as_view(), name = 'reservas_vencidas'),
    path('eliminar_reserva_vencida/<int:pk>/', login_required(EliminarReservaVencida.as_view()), name= 'eliminar_reserva_vencida'),
    path('listado-libros-disponibles/',ListadoLibrosDisponibles.as_view(), name = 'listado_libros_disponibles'),
    path('listado-reservas-vencidas/',ListadoReservasVencias.as_view(), name = 'listado_reservas_vencidas'),
    path('listado-libros-reservados/',ListadoLibrosReservados.as_view(), name = 'listado_libros_reservados'),
    path('detalle-libro/<int:pk>/',DetalleLibroDiponible.as_view(), name = 'detalle_libro'),
    path('reservar-libro/',RegistrarReserva.as_view(), name = 'reservar_libro'),
    # FORMSETS
    #path('crear_autor_formset', FormsetAutor.as_view(), name = 'crear_autor_formset')
]
