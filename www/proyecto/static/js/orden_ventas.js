// static/js/ventas.js - Ordenación de tabla de ventas

function ordenarTabla(columna) {
    const tabla = document.querySelector('table');
    const tbody = tabla.querySelector('tbody');
    const filas = Array.from(tbody.querySelectorAll('tr'));
    
    // Índices de columnas: 0:Código, 1:Cliente, 2:Producto, 3:Cantidad, 4:Precio, 5:Total, 6:Fecha
    const indice = columna;
    
    // Determinar dirección
    const ordenActual = tabla.dataset.orden;
    const direccion = (ordenActual === `col-${indice}-asc`) ? 'desc' : 'asc';
    
    filas.sort((a, b) => {
        const aTexto = a.children[indice].textContent.trim();
        const bTexto = b.children[indice].textContent.trim();
        
        // Para números (Cantidad, Precio, Total)
        if ([3, 4, 5].includes(indice)) {
            const aNum = parseFloat(aTexto.replace('$', '')) || 0;
            const bNum = parseFloat(bTexto.replace('$', '')) || 0;
            return direccion === 'asc' ? aNum - bNum : bNum - aNum;
        }
        // Para fechas
        else if (indice === 6) {
            const aFecha = new Date(aTexto.split(' ')[0].split('/').reverse().join('-'));
            const bFecha = new Date(bTexto.split(' ')[0].split('/').reverse().join('-'));
            return direccion === 'asc' ? aFecha - bFecha : bFecha - aFecha;
        }
        // Para texto
        else {
            return direccion === 'asc' 
                ? aTexto.localeCompare(bTexto)
                : bTexto.localeCompare(aTexto);
        }
    });
    
    // Reordenar
    filas.forEach(fila => tbody.appendChild(fila));
    
    // Guardar estado
    tabla.dataset.orden = `col-${indice}-${direccion}`;
}

// Inicializar dataset si no existe
document.addEventListener('DOMContentLoaded', function() {
    const tabla = document.querySelector('table');
    if (tabla && !tabla.dataset.orden) {
        tabla.dataset.orden = '';
    }
});
