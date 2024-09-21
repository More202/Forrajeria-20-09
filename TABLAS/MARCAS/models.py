from django.db import models
from django.utils import timezone

# Create your models here.
class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=100)
    def __str__(self):
        return self.marca
    



class Edad(models.Model):
    id = models.AutoField(primary_key=True)
    edad = models.CharField(max_length=100)
    def __str__(self):
        return self.edad
    



class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    direccion = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    



class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=100)
    def __str__(self):
        return self.categoria
    



class Sucursal(models.Model):
    id = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    def __str__(self):
        return self.direccion

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    consumidor = models.CharField(max_length=100)
    def __str__(self):
        return self.consumidor
    
class Tamaño(models.Model):
    id=models.AutoField(primary_key=True)
    tamaño=models.CharField(max_length=100,verbose_name="Tamaño")
    def __str__(self) -> str:
        return self.tamaño
    
class Consistencia(models.Model):
    id = models.AutoField(primary_key=True)
    consistencia = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.consistencia

class Animal(models.Model):
    id = models.AutoField(primary_key=True)
    animal = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.animal
    
    

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.ForeignKey('Categoria', null=True, blank=False, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=100)
    animal = models.ForeignKey('Animal', null=True, blank=False, on_delete=models.CASCADE)
    tamaño = models.ForeignKey('Tamaño', null=True, blank=True, on_delete=models.CASCADE)
    edad=models.ForeignKey('Edad', null=True, blank=True, on_delete=models.CASCADE)
    marca = models.ForeignKey('Marca', null=True, blank=False, on_delete=models.CASCADE)
    precio = models.DecimalField(verbose_name='Precio',max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True, blank=True)
    stock_a=models.IntegerField(verbose_name='Stock Actual')
    stock_r=models.IntegerField(verbose_name='Stock Reposicion', default=0, null=True, blank=True)
    stock_m=models.IntegerField(verbose_name='Stock Minimo')
    peso = models.CharField(max_length=100, null=True, blank=True)
    consis = models.ForeignKey('Consistencia', null=True, blank=True, on_delete=models.CASCADE)
    obs = models.CharField(max_length=150, verbose_name='Observaciones', default='',null=True, blank=True,)
    des = models.TextField(verbose_name='Descripcion', default='')
    def __str__(self):
        return self.nombre
    
    
class Caja(models.Model):
    id = models.AutoField(primary_key=True)
    empleado = models.ForeignKey('Empleado', null=True, blank=False, on_delete=models.CASCADE)
    sucursal = models.ForeignKey('Sucursal', null=True, blank=False, on_delete=models.CASCADE)
    abierta = models.BooleanField(default=False, verbose_name='Caja Abierta')
    fecha_hs_ap = models.DateTimeField(default=timezone.now, verbose_name='Fecha y hora de apertura')
    fecha_hs_cier = models.DateTimeField(default=timezone.now,null=True, blank=True, verbose_name='Fecha y hora de cierre') 
    monto_ini = models.DecimalField(verbose_name='Monto Inicial',null=True, blank=True, max_digits=10, decimal_places=2)
    total_ing = models.DecimalField(verbose_name='Total Ingresos', max_digits=10, decimal_places=2)
    total_egr = models.DecimalField(verbose_name='Total Egresos',null=True, blank=True, max_digits=10, decimal_places=2)

    def cerrar_caja(self):
        self.fecha_hs_cier = timezone.now()
        self.abierta = False
        self.save()

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey('Cliente', null=True, blank=False, on_delete=models.CASCADE)
    caja = models.ForeignKey('Caja',null=True, blank=False, on_delete=models.CASCADE )
    fecha_venta = models.DateField(default=timezone.now,verbose_name='Fecha de Venta')
    hora_venta = models.TimeField(default=timezone.now,verbose_name='Hora de Venta')
    total_venta = models.DecimalField(verbose_name='Total',null=True, blank=True, max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=False, verbose_name='Estado')
    
class DetalleVenta(models.Model):
    descuentos_opciones = [
        (0, '0%'),
        (5, '5%'),
        (10, '10%'),
        (15, '15%'),
        (20, '20%'),
        (25, '25%'),
        (30, '30%')
    ]
    id = models.AutoField(primary_key=True)
    venta = models.ForeignKey('Venta',null=True, blank=False, on_delete=models.CASCADE )
    producto = models.ForeignKey('Producto', null=True, blank=False, on_delete=models.CASCADE)
    cantidad = models.IntegerField(verbose_name='Total unidades')
    subtotal = models.DecimalField(verbose_name='Subtotal', max_digits=10, decimal_places=2)
    precio_unitario = models.DecimalField(verbose_name='Precio unitario',max_digits=10, decimal_places=2)
    descuento = models.IntegerField(choices=descuentos_opciones,default=0,verbose_name='Descuento')


