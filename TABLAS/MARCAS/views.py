from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import *
from .forms import *
from django.http import JsonResponse
from decimal import Decimal
from django.db import transaction
from django.views.decorators.http import require_http_methods, require_GET
from django.urls import reverse



# Create your views here.
#----------------------------------
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})



#---------------------------------
@login_required
def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

##################################----MARCAS----#########################################

def marcas(request):
    marcas= Marca.objects.all()
    return render(request, 'tablas/LISTAR_MARCAS.html', {'marcas': marcas})

def crear(request):
    formulario= Marcaform(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('marcas')
    return render(request, 'tablas/htmlbase/crear_marca.html', {'formulario': formulario})

def editar(request, id):
    marca = Marca.objects.get(id=id)
    formulario = Marcaform(request.POST or None, request.FILES or None, instance=marca)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('marcas')
    return render(request, 'tablas/htmlbase/editar_marca.html', {'formulario': formulario})

def eliminar(request, id):
    marca = Marca.objects.get(id=id)
    marca.delete()
    return redirect('marcas')

##################################----EDADES----#######################################

def edades(request):
    edades= Edad.objects.all()
    return render(request, 'tablas/LISTAR_EDADES.html', {'edades': edades})

def crear_edad(request):
    formulario= Edadform(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('edades')
    return render(request, 'tablas/htmlbase/crear_edad.html', {'formulario': formulario})

def editar_edad(request, id):
    edad = Edad.objects.get(id=id)
    formulario = Edadform(request.POST or None, request.FILES or None, instance=edad)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('edades')
    return render(request, 'tablas/htmlbase/editar_edad.html', {'formulario': formulario})

def eliminar_edad(request, id):
    edad = Edad.objects.get(id=id)
    edad.delete()
    return redirect('edades')

##################################----EMPLEADOS----#######################################

def empleados(request):
    empleados= Empleado.objects.all()
    return render(request, 'tablas/LISTAR_EMPLEADOS.html', {'empleados': empleados})

def crear_emp(request):
    formulario= Empleadoform(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('empleados')
    return render(request, 'tablas/htmlbase/crear_empleado.html', {'formulario': formulario})

def editar_empleado(request, id):
    edad = Empleado.objects.get(id=id)
    formulario = Empleadoform(request.POST or None, request.FILES or None, instance=edad)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('empleados')
    return render(request, 'tablas/htmlbase/editar_empleado.html', {'formulario': formulario})

def eliminar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    return redirect('empleados')


def categorias(request):
    categorias= Categoria.objects.all()
    return render(request, 'tablas/LISTAR_CATEGORIAS.html', {'categorias': categorias})

def crear_categoria(request):
    formulario= Categoriaform(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('categorias')
    return render(request, 'tablas/htmlbase/crear_categoria.html', {'formulario': formulario})

def editar_categoria(request, id):
    edad = Categoria.objects.get(id=id)
    formulario = Categoriaform(request.POST or None, request.FILES or None, instance=edad)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('categorias')
    return render(request, 'tablas/htmlbase/editar_categoria.html', {'formulario': formulario})

def eliminar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return redirect('categorias')



##################################----SUCURSALES----#######################################

def sucursales(request):
    sucursales= Sucursal.objects.all()
    return render(request, 'tablas/LISTAR_SUCURSALES.html', {'sucursales': sucursales})

def crear_sucursal(request):
    formulario= Sucursalform(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('sucursales')
    return render(request, 'tablas/htmlbase/crear_sucursal.html', {'formulario': formulario})

def editar_sucursal(request, id):
    sucursal = Sucursal.objects.get(id=id)
    formulario = Sucursalform(request.POST or None, request.FILES or None, instance=sucursal)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('sucursales')
    return render(request, 'tablas/htmlbase/editar_sucursal.html', {'formulario': formulario})

def eliminar_sucursal(request, id):
    sucursal = Sucursal.objects.get(id=id)
    sucursal.delete()
    return redirect('sucursales')


##################################----CLIENTES----#######################################
def clientes(request):
    clientes= Cliente.objects.all()
    return render(request, 'tablas/LISTAR_CLIENTES.html', {'clientes': clientes})

def crear_cliente(request):
    formulario= Clienteform(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('clientes')
    return render(request, 'tablas/htmlbase/crear_cliente.html', {'formulario': formulario})

def editar_cliente(request, id):
    sucursal = Cliente.objects.get(id=id)
    formulario = Clienteform(request.POST or None, request.FILES or None, instance=sucursal)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('clientes')
    return render(request, 'tablas/htmlbase/editar_cliente.html', {'formulario': formulario})

def eliminar_cliente(request, id):
    clientes = Cliente.objects.get(id=id)
    clientes.delete()
    return redirect('clientes')

##################################----TAMAÑOS----#######################################
def tamaños(request):
    tamaños= Tamaño.objects.all()
    return render(request, 'tablas/LISTAR_TAMAÑOS.html', {'tamaños': tamaños})

def crear_tamaño(request):
    formulario= Tamañoform(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('tamaños')
    return render(request, 'tablas/htmlbase/crear_tamaño.html', {'formulario': formulario})

def editar_tamaño(request, id):
    tamaño = Tamaño.objects.get(id=id)
    formulario = Tamañoform(request.POST or None, request.FILES or None, instance=tamaño)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('tamaños')
    return render(request, 'tablas/htmlbase/editar_tamaño.html', {'formulario': formulario})

def eliminar_tamaño(request, id):
    tamaños = Tamaño.objects.get(id=id)
    tamaños.delete()
    return redirect('tamaños')

##################################----animal----#######################################
def animales(request):
    animales= Animal.objects.all()
    return render(request, 'tablas/LISTAR_ANIMALES.html', {'animales': animales})

def crear_animal(request):
    formulario= Animalform(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('animales')
    return render(request, 'tablas/htmlbase/crear_animal.html', {'formulario': formulario})

def editar_animal(request, id):
    animal = Animal.objects.get(id=id)
    formulario = Animalform(request.POST or None, request.FILES or None, instance=animal)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('animales')
    return render(request, 'tablas/htmlbase/editar_animal.html', {'formulario': formulario})

def eliminar_animal(request, id):
    animales = Animal.objects.get(id=id)
    animales.delete()
    return redirect('animales')

##################################----consistencia----#######################################
def consistencias(request):
    consistencias= Consistencia.objects.all()
    return render(request, 'tablas/LISTAR_CONSISTENCIAS.html', {'consistencias': consistencias})

def crear_consistencia(request):
    formulario= Consistenciaform(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('consistencias')
    return render(request, 'tablas/htmlbase/crear_consistencia.html', {'formulario': formulario})

def editar_consistencia(request, id):
    consistencia = Consistencia.objects.get(id=id)
    formulario = Consistenciaform(request.POST or None, request.FILES or None, instance=consistencia)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('consistencias')
    return render(request, 'tablas/htmlbase/editar_consistencia.html', {'formulario': formulario})

def eliminar_consistencia(request, id):
    consistencias = Consistencia.objects.get(id=id)
    consistencias.delete()
    return redirect('consistencias')
##################################----PRODUCTOS----#######################################
def productos(request):
    productos= Producto.objects.all()
    return render(request, 'tablas/LISTAR_PRODUCTOS.html', {'productos': productos})


def crear_producto(request):
    formulario= Productoform(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('productos')
    return render(request, 'tablas/htmlbase/crear_producto.html', {'formulario': formulario})

def editar_producto(request, id):
    producto = Producto.objects.get(id=id)
    formulario = Productoform(request.POST or None, request.FILES or None, instance=producto)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('productos')
    return render(request, 'tablas/htmlbase/editar_producto.html', {'formulario': formulario})

def eliminar_producto(request, id):
    productos = Producto.objects.get(id=id)
    productos.delete()
    return redirect('productos')

def productos_baja_existencia(request):
    query = """
        SELECT * from marcas_Producto where stock_a <= 7;
    """
    productos_baja_existencia = Producto.objects.raw(query)
    return render(request, 'tablas/bajo_stock.html', {'productos_baja_existencia': productos_baja_existencia})
    

def autocomplete_productos(request):
    if 'term' in request.GET:
        qs = Producto.objects.filter(nombre__icontains=request.GET['term'])
        productos = list(qs.values_list('nombre', flat=True))
        return JsonResponse(productos, safe=False)
    return JsonResponse([], safe=False)


##################################----CAJAS----#######################################
def cajas(request):
    cajas= Caja.objects.all()
    return render(request,'tablas/LISTAR_CAJAS.html', {'cajas': cajas})

def crear_caja(request):
    formulario= Cajaform(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('cajas')
    return render(request, 'tablas/htmlbase/crear_caja.html', {'formulario': formulario})

def editar_caja(request, id):
    caja = Caja.objects.get(id=id)
    formulario = Cajaform(request.POST or None, request.FILES or None, instance=caja)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('cajas')
    return render(request, 'tablas/htmlbase/editar_caja.html', {'formulario': formulario})

def eliminar_caja(request, id):
    cajas = Caja.objects.get(id=id)
    cajas.delete()
    return redirect('cajas')
def cerrar_caja(request):
    caja = Caja.objects.get(id=id)
    if caja.abierta:
        caja.cerrar_caja()
        return render(request,'tablas/LISTAR_CAJAS.html', {'cajas': cajas})
    else:
        pass

##################################----LOGIN----#######################################
@login_required
def inicio(request):
    return render(request, 'paginas/menu_p.html')

def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('menu_p')
    else:
        return redirect('login')
def exit(request):
    logout(request)
    return redirect('inicio')

def menu_p(request):
    return render(request, 'paginas/menu_p.html')
##################################----APERTURA----#######################################
def apertura_caja(request):
    if request.method == 'POST':
        form = AperturaCajaForm(request.POST)
        if form.is_valid():
            monto_inicial = form.cleaned_data['monto_inicial']
            caja = Caja(
                monto_ini=monto_inicial,
                fecha_hs_ap=timezone.now(),
                abierta=True,
                total_ing=0,
                total_egr=0
            )
            caja.save()
            return redirect('nueva_venta')  # Redirigir a nueva_venta en lugar de cajas
    else:
        form = AperturaCajaForm()
    
    return render(request, 'tablas/htmlbase/apertura_caja.html', {'formulario': form})

def stock(request):
    pass


def listado_ventas(request):
    pass

import logging
logger = logging.getLogger(__name__)

def agregarcosas(request):
    if request.method == 'POST':
        logger.debug(f"POST data: {request.POST}")
        logger.debug(f"GET data: {request.GET}")
        
        form_type = request.GET.get('form_type')
        logger.debug(f"Form type: {form_type}")
        
        formulario = None
        redirect_url = None

        if form_type == 'animal':
            formulario = Animalform(request.POST)
            redirect_url = reverse('animales')
        elif form_type == 'marca':
            formulario = Marcaform(request.POST)
            redirect_url = reverse('marcas')
        elif form_type == 'categoria':
            formulario = Categoriaform(request.POST)
            redirect_url = reverse('categorias')
        elif form_type == 'tamaño':
            formulario = Tamañoform(request.POST)
            redirect_url = reverse('tamaños')
        elif form_type == 'edad':
            formulario = Edadform(request.POST)
            redirect_url = reverse('edades')
        elif form_type == 'consistencia':
            formulario = Consistenciaform(request.POST)
            redirect_url = reverse('consistencias')

        if formulario:
            if formulario.is_valid():
                try:
                    formulario.save()
                    return JsonResponse({
                        'success': True,
                        'type': form_type.capitalize(),
                        'redirect_url': redirect_url
                    })
                except Exception as e:
                    logger.error(f"Error saving {form_type}: {str(e)}")
                    return JsonResponse({'success': False, 'errors': str(e)}, status=500)
            else:
                logger.error(f"Form errors: {formulario.errors}")
                return JsonResponse({'success': False, 'errors': formulario.errors}, status=400)
        else:
            logger.error(f"Invalid form type: {form_type}")
            return JsonResponse({'success': False, 'errors': 'Invalid form type'}, status=400)


    # Rest of the view function remains the same
    marca_form = Marcaform()
    categoria_form = Categoriaform()
    tamaño_form = Tamañoform()
    edad_form = Edadform()
    animal_form = Animalform()
    consistencia_form = Consistenciaform()

    form_type = request.GET.get('form_type')
    if form_type == 'marca':
        form_to_display = marca_form
    elif form_type == 'categoria':
        form_to_display = categoria_form
    elif form_type == 'tamaño':
        form_to_display = tamaño_form
    elif form_type == 'edad':
        form_to_display = edad_form
    elif form_type == 'animal':
        form_to_display = animal_form
    elif form_type == 'consistencia':
        form_to_display = consistencia_form
    else:
        form_to_display = None

    return render(request, 'tablas/agregar.html', {
        'form_to_display': form_to_display,
        'marca_form': marca_form,
        'categoria_form': categoria_form,
        'tamaño_form': tamaño_form,
        'edad_form': edad_form,
        'animal_form': animal_form,
        'consistencia_form': consistencia_form,
    })
##################################----VENTAS----#######################################
def ventas(request):
    ventas= Venta.objects.all()
    return render(request, 'tablas/LISTAR_VENTAS.html', {'ventas': ventas})

def crear_ventas(request):
    formulario= Ventaform(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('ventas')
    return render(request, 'tablas/htmlbase/crear_venta.html', {'formulario': formulario})

def editar_venta(request, id):
    venta = Venta.objects.get(id=id)
    formulario = Ventaform(request.POST or None, request.FILES or None, instance=venta)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('ventas')
    return render(request, 'tablas/htmlbase/editar_venta.html', {'formulario': formulario})

def eliminar_venta(request, id):
    ventas = Venta.objects.get(id=id)
    ventas.delete()
    return redirect('ventas')
##################################----DETALLES----#######################################
def detalles(request):
    detalles= DetalleVenta.objects.all()
    return render(request, 'tablas/LISTAR_DETALLES.html', {'detalles': detalles})

def crear_detalles(request):
    formulario= DetalleVentaform(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('detalles')
    return render(request, 'tablas/htmlbase/crear_detalle.html', {'formulario': formulario})

def editar_detalle(request, id):
    detalle = DetalleVenta.objects.get(id=id)
    formulario = DetalleVentaform(request.POST or None, request.FILES or None, instance=detalle)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('detalles')
    return render(request, 'tablas/htmlbase/editar_detalle.html', {'formulario': formulario})

def eliminar_detalle(request, id):
    detalles = DetalleVenta.objects.get(id=id)
    detalles.delete()
    return redirect('detalles')



@require_http_methods(["GET", "POST"])
def nueva_venta(request):
    if request.method == 'POST':
        with transaction.atomic():
            cliente_id = request.POST.get('cliente')
            caja_id = request.POST.get('caja')
            productos = request.POST.getlist('producto_id')
            cantidades = request.POST.getlist('cantidad')
            descuentos = request.POST.getlist('descuento')
            
            venta = Venta.objects.create(
                cliente_id=cliente_id,
                caja_id=caja_id,
                fecha_venta=timezone.now().date(),
                hora_venta=timezone.now().time(),
                estado=True
            )
            
            total_venta = Decimal('0.00')
            
            for producto_id, cantidad, descuento in zip(productos, cantidades, descuentos):
                producto = Producto.objects.get(id=producto_id)
                cantidad = int(cantidad)
                descuento = Decimal(descuento)
                
                precio_unitario = producto.precio
                subtotal = precio_unitario * cantidad
                descuento_decimal = descuento / 100
                subtotal_con_descuento = subtotal * (1 - descuento_decimal)
                
                DetalleVenta.objects.create(
                    venta=venta,
                    producto=producto,
                    cantidad=cantidad,
                    precio_unitario=precio_unitario,
                    subtotal=subtotal_con_descuento,
                    descuento=descuento
                )
                
                total_venta += subtotal_con_descuento
                
                # Actualizar el stock del producto
                producto.stock_a -= cantidad
                producto.save()
            
            venta.total_venta = total_venta
            venta.save()
            
            caja = Caja.objects.get(id=caja_id)
            caja.total_ing += total_venta
            caja.save()
            
            return redirect('detalle_venta', venta_id=venta.id)
    
    productos = Producto.objects.all()
    cajas_abiertas = Caja.objects.filter(abierta=True)
    clientes = Cliente.objects.all()
    
    return render(request, 'paginas/nueva_venta.html', {
        'productos': productos,
        'cajas_abiertas': cajas_abiertas,
        'clientes': clientes
    })

def buscar_producto(request):
    query = request.GET.get('q', '')
    productos = Producto.objects.filter(nombre__icontains=query)[:10]
    data = [{'id': p.id, 'nombre': p.nombre, 'precio': str(p.precio), 'stock': p.stock_a} for p in productos]
    return JsonResponse(data, safe=False)

# VENTASSSSS

@require_GET
def obtener_productos(request):
    animal_nombre = request.GET.get('animal')
    categoria_nombre = request.GET.get('categoria')

    # Si no se proporcionan parámetros, devolver todos los productos
    if not animal_nombre and not categoria_nombre:
        productos = Producto.objects.all()
    elif animal_nombre and categoria_nombre:
        try:
            animal = Animal.objects.get(animal=animal_nombre)
            categoria = Categoria.objects.get(categoria=categoria_nombre)
            productos = Producto.objects.filter(animal=animal, categoria=categoria)
        except (Animal.DoesNotExist, Categoria.DoesNotExist):
            return JsonResponse({'error': 'Animal o categoría no encontrada'}, status=404)
    else:
        return JsonResponse({'error': 'Parámetros incompletos'}, status=400)

    productos_list = [
        {
            'id': producto.id,
            'nombre': producto.nombre,
            'marca': producto.marca.marca if producto.marca else 'Sin marca',
            'peso': f"{producto.peso} Kg" if producto.peso else 'N/A',
            'precio': float(producto.precio),
            'stock': producto.stock_a
        } for producto in productos
    ]
    
    return JsonResponse(productos_list, safe=False)