from django.urls import path, include
from . import views
from .views import inicio, home_redirect
from django.contrib.auth import views as auth_views

#Imagen
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    ######LOGIN######
    path('', home_redirect, name='home_redirect'),  
    path('inicio/', inicio, name='inicio'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    ######MENU######
    path('menu/', views.menu_p, name='menu_p'),
    path('apertura-caja/', views.apertura_caja, name='apertura_caja'),
    path('stock/', views.stock, name= 'stock'),
    path('listado_ventas', views.listado_ventas, name='listado_ventas'),



    #######MARCAS######
    path('marcas', views.marcas, name='marcas'),
    path('marcas/crear', views.crear, name='crear'),
    path('eliminar-marca/<int:id>', views.eliminar, name='eliminar_marca'),
    path('tablas/editar-marca', views.editar, name='editar_marca'),
    path('tablas/editar-marca/<int:id>', views.editar, name='editar_marca'),


    ######EDADES######
    path('edades', views.edades, name='edades'),
    path('edades/crear', views.crear_edad, name='crear_edad'),
    path('tablas/editar-edad', views.editar_edad, name='editar_edad'),
    path('tablas/editar-edad/<int:id>', views.editar_edad, name='editar_edad'),
    path('eliminar-edad/<int:id>', views.eliminar_edad, name='eliminar_edad'),


    ######EMPLEADOS######
    path('empleados', views.empleados, name='empleados'),
    path('empleados/crear', views.crear_emp, name='crear_emp'),
    path('tablas/editar-empleado', views.editar_empleado, name='editar_edad'),
    path('tablas/editar-empleado/<int:id>', views.editar_empleado, name='editar_empleado'),
    path('eliminar-empleado/<int:id>', views.eliminar_empleado, name='eliminar_empleado'),


    ######CATEGORIAS######
    path('categorias', views.categorias, name='categorias'),
    path('categorias/crear', views.crear_categoria, name='crear_categoria'),
    path('tablas/editar-categoria', views.editar_categoria, name='editar_categoria'),
    path('tablas/editar-categoria/<int:id>', views.editar_categoria, name='editar_categoria'),
    path('eliminar-categoria/<int:id>', views.eliminar_categoria, name='eliminar_categoria'),


    ######EMPLEADOS######
    path('sucursales', views.sucursales, name='sucursales'),
    path('sucursales/crear', views.crear_sucursal, name='crear_sucursal'),
    path('tablas/editar-sucursal', views.editar_sucursal, name='editar_sucursal'),
    path('tablas/editar-sucursal/<int:id>', views.editar_sucursal, name='editar_sucursal'),
    path('eliminar-sucursal/<int:id>', views.eliminar_sucursal, name='eliminar_sucursal'),


    ######CLIENTE######
    path('clientes', views.clientes, name='clientes'),
    path('clientes/crear', views.crear_cliente, name='crear_cliente'),
    path('tablas/editar-cliente', views.editar_cliente, name='editar_cliente'),
    path('tablas/editar-cliente/<int:id>', views.editar_cliente, name='editar_cliente'),
    path('eliminar-cliente/<int:id>', views.eliminar_cliente, name='eliminar_cliente'),

        ######tamaño######
    path('tamaños', views.tamaños, name='tamaños'),
    path('tamaños/crear', views.crear_tamaño, name='crear_tamaño'),
    path('tablas/editar-tamaño', views.editar_tamaño, name='editar_tamaño'),
    path('tablas/editar-tamaño/<int:id>', views.editar_tamaño, name='editar_tamaño'),
    path('eliminar-tamaño/<int:id>', views.eliminar_tamaño, name='eliminar_tamaño'),

    ######animal######
    path('animales', views.animales, name='animales'),
    path('animales/crear', views.crear_animal, name='crear_animal'),
    path('tablas/editar-animal', views.editar_animal, name='editar_animal'),
    path('tablas/editar-animal/<int:id>', views.editar_animal, name='editar_animal'),
    path('eliminar-animal/<int:id>', views.eliminar_animal, name='eliminar_animal'),

    ######consistencia######
    path('consistencias', views.consistencias, name='consistencias'),
    path('consistencias/crear', views.crear_consistencia, name='crear_consistencia'),
    path('tablas/editar-consistencia', views.editar_consistencia, name='editar_consistencia'),
    path('tablas/editar-consistencia/<int:id>', views.editar_consistencia, name='editar_consistencia'),
    path('eliminar-consistencia/<int:id>', views.eliminar_consistencia, name='eliminar_consistencia'),

    ######PRODUCTOS######
    path('productos', views.productos, name='productos'),
    path('productos/crear', views.crear_producto, name='crear_producto'),
    path('tablas/editar-producto', views.editar_producto, name='editar_producto'),
    path('tablas/editar-producto/<int:id>', views.editar_producto, name='editar_producto'),
    path('eliminar-producto/<int:id>', views.eliminar_producto, name='eliminar_producto'),
    path('productos/bajo_stock/', views.productos_baja_existencia, name='productos_baja_existencia'),
    path('productos/autocomplete/', views.autocomplete_productos, name='autocomplete_productos'),
    path('agregar/', views.agregarcosas, name='agregar'),

    ######CAJAS######
    path('cajas/', views.cajas, name='cajas'),
    path('crear_caja/', views.crear_caja, name='crear_caja'),
    path('editar_caja/<int:id>/', views.editar_caja, name='editar_caja'),
    path('eliminar_caja/<int:id>/', views.eliminar_caja, name='eliminar_caja'),
    path('cerrar_caja/<int:id>/', views.cerrar_caja, name='cerrar_caja'),


    ######VENTAS######
    path('ventas', views.ventas, name='ventas'),
    path('ventas/crear', views.crear_ventas, name='crear_venta'),
    path('tablas/editar-venta', views.editar_venta, name='editar_venta'),
    path('tablas/editar-venta/<int:id>', views.editar_venta, name='editar_venta'),
    path('eliminar-venta/<int:id>', views.eliminar_venta, name='eliminar_venta'),

    ######DETALLE DE VENTA######
    path('detalles', views.detalles, name='detalles'),
    path('detalles/crear', views.crear_detalles, name='crear_detalle'),
    path('tablas/editar-detalle', views.editar_detalle, name='editar_detalle'),
    path('tablas/editar-detalle/<int:id>', views.editar_detalle, name='editar_detalle'),
    path('eliminar-detalle/<int:id>', views.eliminar_detalle, name='eliminar_detalle'),

    path('apertura-caja/', views.apertura_caja, name='apertura_caja'),
    path('nueva-venta/', views.nueva_venta, name='nueva_venta'),
    path('buscar-producto/', views.buscar_producto, name='buscar_producto'),
    path('obtener_productos/', views.obtener_productos, name='obtener_productos'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
