document.addEventListener('DOMContentLoaded', function() {
    var modal = document.getElementById('modal');
    var openModalBtn = document.getElementById('openModalBtn');
    var closeModalBtn = document.getElementById('closeModalBtn');
    var aperturaCajaForm = document.getElementById('aperturaCajaForm');

    if (openModalBtn) {
        openModalBtn.onclick = function() {
            modal.style.display = "block";
        }
    }

    if (closeModalBtn) {
        closeModalBtn.onclick = function() {
            modal.style.display = "none";
        }
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    if (aperturaCajaForm) {
        aperturaCajaForm.onsubmit = function(e) {
            e.preventDefault();
            var montoInicial = document.getElementById('montoInicial').value;
            if (montoInicial) {
                this.submit();
            } else {
                alert('Por favor, ingrese un monto inicial.');
            }
        }
    }
});

//-------------------------VENTAS------------------------------///
// Otras funciones y código que puedas tener en main.js

/// Inicialización cuando el DOM está listo
document.addEventListener('DOMContentLoaded', function() {
    // Inicializar Lucide
    lucide.createIcons();

    // Inicializar botones de animales
    const animalButtons = document.querySelectorAll('.animal-buttons button');
    animalButtons.forEach(button => {
        button.addEventListener('click', function() {
            console.log('Botón de animal clickeado:', this.innerText);
            mostrarCategorias(this.innerText);
        });
    });

    // Inicializar búsqueda de productos
    const buscarProductoInput = document.getElementById('buscar-producto');
    if (buscarProductoInput) {
        buscarProductoInput.addEventListener('input', function() {
            const query = this.value.toLowerCase();
            buscarProductos(query);
        });
    }
});

    // No cargar todos los productos al inicio
    // cargarTodosLosProductos();


function mostrarSugerencias(query) {
    const sugerenciasContainer = document.getElementById('sugerencias-productos');
    const listaProductos = document.getElementById('lista-productos');
    const productos = listaProductos.getElementsByTagName('li');
    
    sugerenciasContainer.innerHTML = '';
    sugerenciasContainer.style.display = 'none';

    if (query.length < 2) return; // No mostrar sugerencias para consultas muy cortas

    let sugerencias = [];
    for (let producto of productos) {
        const texto = producto.textContent.toLowerCase();
        if (texto.includes(query)) {
            sugerencias.push(producto.textContent);
        }
    }

    if (sugerencias.length > 0) {
        sugerenciasContainer.style.display = 'block';
        sugerencias.forEach(sugerencia => {
            const div = document.createElement('div');
            div.textContent = sugerencia;
            div.addEventListener('click', function() {
                document.getElementById('buscar-producto').value = sugerencia;
                buscarProductos(sugerencia);
                sugerenciasContainer.style.display = 'none';
            });
            sugerenciasContainer.appendChild(div);
        });
    }
}

function cargarTodosLosProductos() {
    console.log('Cargando todos los productos...');
    fetch('/obtener_productos/')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(productos => {
            console.log('Productos cargados:', productos);
            const listaProductos = document.getElementById('lista-productos');
            if (!listaProductos) {
                console.error('Elemento lista-productos no encontrado');
                return;
            }
            listaProductos.innerHTML = '';
            productos.forEach(producto => {
                const li = document.createElement('li');
                li.innerText = `${producto.nombre} - ${producto.marca} - ${producto.peso} - $${producto.precio.toFixed(2)} - Stock: ${producto.stock}`;
                li.onclick = function() {
                    agregarProductoAVenta(producto);
                };
                listaProductos.appendChild(li);
            });
            document.getElementById('productos-mostrar').style.display = 'block';
        })
        .catch(error => {
            console.error('Error al cargar productos:', error);
            const listaProductos = document.getElementById('lista-productos');
            if (listaProductos) {
                listaProductos.innerHTML = '<li>Error al cargar productos. Por favor, intenta de nuevo.</li>';
            }
        });
}
function mostrarCategorias(animal) {
    console.log('Mostrando categorías para:', animal);
    const categoriasProductos = document.getElementById('categorias-productos');
    if (!categoriasProductos) {
        console.error('Elemento categorias-productos no encontrado');
        return;
    }
    
    categoriasProductos.innerHTML = '';
    
    const categorias = ['ALIMENTO', 'INDUMENTARIA', 'MEDICAMENTO'];
    
    categorias.forEach(categoria => {
        const button = document.createElement('button');
        button.type = 'button';
        button.className = 'btn-category';
        button.innerText = categoria;
        button.onclick = function() {
            console.log('Categoría seleccionada:', categoria);
            mostrarProductos(animal, categoria);
        };
        categoriasProductos.appendChild(button);
    });
    
    categoriasProductos.style.display = 'flex';
}
function mostrarProductos(animal, categoria) {
    console.log('mostrarProductos llamado con:', animal, categoria);
    const listaProductos = document.getElementById('lista-productos');
    if (!listaProductos) {
        console.error('Elemento lista-productos no encontrado');
        return;
    }
    
    listaProductos.innerHTML = '<li>Cargando productos...</li>';

    const url = `/obtener_productos/?animal=${encodeURIComponent(animal)}&categoria=${encodeURIComponent(categoria)}`;

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(productos => {
            listaProductos.innerHTML = '';
            if (productos.length === 0) {
                listaProductos.innerHTML = '<li>No se encontraron productos para esta selección.</li>';
            } else {
                productos.forEach(producto => {
                    const li = document.createElement('li');
                    li.className = 'producto-item';
                    li.style.cursor = 'pointer';
                    li.style.padding = '10px';
                    li.style.backgroundColor = '#333333';
                    li.style.marginBottom = '5px';
                    li.style.borderRadius = '5px';
                    li.style.transition = 'background-color 0.3s ease';
                    li.innerText = `${producto.nombre} - ${producto.marca} - ${producto.peso} - $${producto.precio.toFixed(2)} - Stock: ${producto.stock}`;
                    li.onclick = function() {
                        agregarProductoAVenta(producto);
                    };
                    listaProductos.appendChild(li);
                });
            }
            document.getElementById('productos-mostrar').style.display = 'block';
        })
        .catch(error => {
            console.error('Error al cargar productos:', error);
            listaProductos.innerHTML = '<li>Error al cargar productos. Por favor, intenta de nuevo.</li>';
        });
}
function agregarProductoAVenta(producto) {
    const tablaVenta = document.getElementById('productos-venta');
    if (!tablaVenta) return;
    
    const fila = tablaVenta.insertRow();
    fila.innerHTML = `
        <td>${producto.nombre} - ${producto.marca} ${producto.peso}</td>
        <td><input type="number" value="1" min="1" max="${producto.stock}" onchange="actualizarTotal()"></td>
        <td>$${producto.precio.toFixed(2)}</td>
        <td>$<span class="subtotal">${producto.precio.toFixed(2)}</span></td>
        <input type="hidden" name="producto_id" value="${producto.id}">
    `;
    actualizarTotal();
}

function calcularDescuento(precio, cantidad, descuentoPorcentaje) {
    const subtotalSinDescuento = precio * cantidad;
    const descuento = subtotalSinDescuento * (descuentoPorcentaje / 100);
    return subtotalSinDescuento - descuento;
}

function actualizarTotal() {
    const filas = document.getElementById('productos-venta').rows;
    let subtotal = 0;
    for (let i = 0; i < filas.length; i++) {
        const cantidad = parseInt(filas[i].cells[1].getElementsByTagName('input')[0].value);
        const precio = parseFloat(filas[i].cells[2].innerText.replace('$', ''));
        const subtotalProducto = precio * cantidad;
        
        filas[i].cells[3].getElementsByClassName('subtotal')[0].innerText = subtotalProducto.toFixed(2);
        subtotal += subtotalProducto;
    }

    const descuentoTotalSelect = document.getElementById('descuento-total');
    const descuentoTotalPorcentaje = parseInt(descuentoTotalSelect.value);
    const descuentoTotal = subtotal * (descuentoTotalPorcentaje / 100);
    const totalConDescuento = subtotal - descuentoTotal;

    document.getElementById('subtotal-amount').innerText = subtotal.toFixed(2);
    document.getElementById('descuento-amount').innerText = descuentoTotal.toFixed(2);
    document.getElementById('total-amount').innerText = totalConDescuento.toFixed(2);
}

function aplicarDescuentoTotal() {
    actualizarTotal();
}

function buscarProductos(query) {
    const listaProductos = document.getElementById('lista-productos');
    const productos = listaProductos.getElementsByTagName('li');
    
    for (let producto of productos) {
        const texto = producto.textContent.toLowerCase();
        if (texto.includes(query.toLowerCase())) {
            producto.style.display = '';
        } else {
            producto.style.display = 'none';
        }
    }
}


function cancelarVenta() {
    if (confirm('¿Está seguro de que desea cancelar la venta?')) {
        document.getElementById('productos-venta').innerHTML = '';
        actualizarTotal();
    }
}

function imprimirVenta() {
    window.print();
}

function guardarVenta() {
    alert('Funcionalidad de guardar venta no implementada');
}






document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('addElementForm');
    const modal = document.getElementById('elementSuccessModal');
    const closeBtn = document.getElementById('closeElementModalBtn');
    const redirectBtn = document.getElementById('redirectElementBtn');
    const successMessage = document.getElementById('elementSuccessMessage');

    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(form);

            fetch(form.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                    'X-Requested-With': 'XMLHttpRequest'
                },
            })
            .then(response => response.json())
            .then(data => {
                console.log('Respuesta del servidor:', data);
                if (data.success) {
                    if (successMessage) {
                        successMessage.textContent = `${data.type} ha sido agregado con éxito.`;
                    }
                    if (redirectBtn) {
                        redirectBtn.onclick = function() {
                            window.location.href = data.redirect_url;
                        };
                    }
                    if (modal) {
                        modal.style.display = 'block';
                    }
                } else {
                    throw new Error(data.errors || 'Error desconocido');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Hubo un error al enviar el formulario: ' + error.message);
            });
        });
    }

    if (closeBtn) {
        closeBtn.onclick = function() {
            modal.style.display = 'none';
        };
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    };
});