// static/js/ordenacion.js

class OrdenadorTabla {
    constructor(containerSelector, options = {}) {
        this.container = document.querySelector(containerSelector);
        if (!this.container) {
            console.error("ERROR: No se encontro el contenedor:", containerSelector);
            return;
        }

        this.items = Array.from(this.container.children);
        this.campoActual = options.campoInicial || 'nombre';
        this.direccionActual = options.direccionInicial || 'asc';
        this.selectores = options.selectores || {
            nombre: 'h3',
            precio: '.precio',
            stock: '.stock',
            proveedor: '.proveedor',
            seccion: '.seccion',
            descripcion: '.descripcion',
            cif: '.cif',
            contacto: '.contacto',
            fecha: '.fecha'
        };

        console.log("OK: Ordenador inicializado para:", containerSelector);
        console.log("Items encontrados:", this.items.length);

        this.actualizarIndicadores();
    }

    ordenar(campo) {
        console.log("Ordenando por:", campo);

        if (campo === this.campoActual) {
            this.direccionActual = this.direccionActual === 'asc' ? 'desc' : 'asc';
        } else {
            this.campoActual = campo;
            this.direccionActual = 'asc';
        }

        console.log("Direccion:", this.direccionActual);

        this.items.sort((a, b) => {
            let aValor, bValor;

            switch(campo) {
                case 'nombre':
                    aValor = a.querySelector(this.selectores.nombre)?.textContent || '';
                    bValor = b.querySelector(this.selectores.nombre)?.textContent || '';
                    break;

                case 'precio':
                    aValor = this.parsePrecio(a.querySelector(this.selectores.precio)?.textContent);
                    bValor = this.parsePrecio(b.querySelector(this.selectores.precio)?.textContent);
                    break;

                case 'stock':
                    aValor = this.parseStock(a.querySelector(this.selectores.stock)?.textContent);
                    bValor = this.parseStock(b.querySelector(this.selectores.stock)?.textContent);
                    break;

                case 'proveedor':
                    aValor = a.querySelector(this.selectores.proveedor)?.textContent || '';
                    bValor = b.querySelector(this.selectores.proveedor)?.textContent || '';
                    aValor = aValor.replace('Proveedor:', '').trim();
                    bValor = bValor.replace('Proveedor:', '').trim();
                    break;

                case 'seccion':
                    aValor = a.querySelector(this.selectores.seccion)?.textContent || '';
                    bValor = b.querySelector(this.selectores.seccion)?.textContent || '';
                    aValor = aValor.replace('Sección:', '').replace('Seccion:', '').trim();
                    bValor = bValor.replace('Sección:', '').replace('Seccion:', '').trim();
                    break;

                case 'descripcion':
                    aValor = a.querySelector(this.selectores.descripcion)?.textContent || '';
                    bValor = b.querySelector(this.selectores.descripcion)?.textContent || '';
                    break;

                case 'cif':
                    aValor = a.querySelector(this.selectores.cif)?.textContent || '';
                    bValor = b.querySelector(this.selectores.cif)?.textContent || '';
                    break;

                case 'contacto':
                    aValor = a.querySelector(this.selectores.contacto)?.textContent || '';
                    bValor = b.querySelector(this.selectores.contacto)?.textContent || '';
                    aValor = aValor.replace('Contacto:', '').trim();
                    bValor = bValor.replace('Contacto:', '').trim();
                    break;

                case 'fecha':
                    aValor = this.parseFecha(a.querySelector(this.selectores.fecha)?.textContent);
                    bValor = this.parseFecha(b.querySelector(this.selectores.fecha)?.textContent);
                    break;

                default:
                    return 0;
            }

            if (this.direccionActual === 'asc') {
                return aValor > bValor ? 1 : -1;
            } else {
                return aValor < bValor ? 1 : -1;
            }
        });

        this.items.forEach(item => this.container.appendChild(item));
        this.actualizarIndicadores();
        console.log("Ordenacion completada");
    }

    parsePrecio(texto) {
        if (!texto) return 0;
        return parseFloat(texto.replace(/[$]/g, '').replace(',', '')) || 0;
    }

    parseStock(texto) {
        if (!texto) return 0;
        return parseInt(texto.replace(/[^0-9]/g, '')) || 0;
    }

    parseFecha(texto) {
        if (!texto) return new Date(0);
        const partes = texto.split('/');
        if (partes.length === 3) {
            return new Date(partes[2], partes[1] - 1, partes[0]);
        }
        return new Date(0);
    }

    actualizarIndicadores() {
        document.querySelectorAll('.orden-btn').forEach(btn => {
            btn.classList.remove('activo');
        });

        const btnActual = document.querySelector(`.orden-btn[data-campo="${this.campoActual}"]`);
        if (btnActual) {
            btnActual.classList.add('activo');
            const textoBase = btnActual.textContent.replace(' ↑', '').replace(' ↓', '');
            btnActual.textContent = `${textoBase} ${this.direccionActual === 'asc' ? '↑' : '↓'}`;
        }
    }
}

document.addEventListener('DOMContentLoaded', function() {
    console.log("Inicializando ordenadores...");

    // ============================================
    // PRODUCTOS
    // ============================================
    if (document.querySelector('#productos-container')) {
        console.log("Contenedor de productos encontrado");
        window.ordenadorProductos = new OrdenadorTabla('#productos-container', {
            campoInicial: 'nombre',
            selectores: {
                nombre: 'h3',
                precio: '.precio',
                stock: '.stock',
                proveedor: '.proveedor',
                seccion: '.seccion'
            }
        });
    }

    // ============================================
    // SECCIONES
    // ============================================
    if (document.querySelector('#secciones-container')) {
        console.log("Contenedor de secciones encontrado");
        window.ordenadorSecciones = new OrdenadorTabla('#secciones-container', {
            campoInicial: 'nombre',
            selectores: {
                nombre: '.nombre-seccion',
                descripcion: '.descripcion-seccion'
            }
        });
    }

    // ============================================
    // PROVEEDORES
    // ============================================
    if (document.querySelector('#proveedores-container')) {
        console.log("Contenedor de proveedores encontrado");
        window.ordenadorProveedores = new OrdenadorTabla('#proveedores-container', {
            campoInicial: 'nombre',
            selectores: {
                nombre: '.nombre-proveedor',
                cif: '.cif-proveedor',
                contacto: '.contacto-proveedor'
            }
        });
    }

    // ============================================
    // VENTAS (pendiente de implementar con tabla)
    // ============================================
    if (document.querySelector('table')) {
        console.log("Tabla de ventas encontrada (pendiente de implementar)");
        // Aquí iría la inicialización para ventas cuando adaptemos el script a tablas
    }
});
