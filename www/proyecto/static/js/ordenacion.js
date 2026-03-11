// static/js/ordenacion.js - Version DEBUG para stock

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
            fecha: '.fecha'
        };

        console.log("OK: Ordenador inicializado para:", containerSelector);
        console.log("Items encontrados:", this.items.length);
        
        if (this.items.length > 0) {
            console.log("Primer item - HTML:", this.items[0].innerHTML);
            console.log("Primer item - Stock:", this.items[0].querySelector(this.selectores.stock)?.textContent);
        }

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
                    console.log("Nombre A:", aValor, "B:", bValor);
                    break;
                    
                case 'precio':
                    aValor = this.parsePrecio(a.querySelector(this.selectores.precio)?.textContent);
                    bValor = this.parsePrecio(b.querySelector(this.selectores.precio)?.textContent);
                    console.log("Precio A:", aValor, "B:", bValor);
                    break;
                    
                case 'stock':
                    const stockElemA = a.querySelector(this.selectores.stock);
                    const stockElemB = b.querySelector(this.selectores.stock);
                    
                    console.log("Stock A - Elemento:", stockElemA);
                    console.log("Stock B - Elemento:", stockElemB);
                    
                    if (!stockElemA || !stockElemB) {
                        console.warn("ADVERTENCIA: No se encontro elemento stock en algun item");
                    }
                    
                    const stockTextA = stockElemA?.textContent || '0';
                    const stockTextB = stockElemB?.textContent || '0';
                    
                    console.log("Texto bruto A:", stockTextA);
                    console.log("Texto bruto B:", stockTextB);
                    
                    aValor = this.parseStock(stockTextA);
                    bValor = this.parseStock(stockTextB);
                    
                    console.log("Valor parseado A:", aValor);
                    console.log("Valor parseado B:", bValor);
                    break;

		case 'proveedor':
		    aValor = a.querySelector(this.selectores.proveedor)?.textContent || '';
		    bValor = b.querySelector(this.selectores.proveedor)?.textContent || '';
		    // Limpiar el texto "Proveedor: " para ordenar solo por el nombre
		    aValor = aValor.replace('Proveedor:', '').trim();
		    bValor = bValor.replace('Proveedor:', '').trim();
		    console.log("Proveedor A:", aValor, "B:", bValor);
		    break;

		case 'seccion':
		    aValor = a.querySelector(this.selectores.seccion)?.textContent || '';
		    bValor = b.querySelector(this.selectores.seccion)?.textContent || '';
		    // Limpiar el texto "Sección: " para ordenar solo por el nombre
		    aValor = aValor.replace('Sección:', '').trim();
		    bValor = bValor.replace('Sección:', '').trim();
		    console.log("Sección A:", aValor, "B:", bValor);
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
        const valor = parseFloat(texto.replace(/[$]/g, '').replace(',', '')) || 0;
        console.log("parsePrecio:", texto, "->", valor);
        return valor;
    }

    parseStock(texto) {
        if (!texto) return 0;
        const soloNumeros = texto.replace(/[^0-9]/g, '');
        console.log("soloNumeros:", soloNumeros);
        
        const valor = parseInt(soloNumeros) || 0;
        console.log("parseStock resultado:", valor);
        return valor;
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
    
    if (document.querySelector('#productos-container')) {
        console.log("Contenedor de productos encontrado");
        window.ordenadorProductos = new OrdenadorTabla('#productos-container', {
            campoInicial: 'nombre',
            selectores: {
                nombre: 'h3',
                precio: '.precio',
                stock: '.stock',
		seccion: '.seccion',
		proveedor: '.proveedor'
            }
        });
    } else {
        console.warn("ADVERTENCIA: No se encontro #productos-container");
    }
});
