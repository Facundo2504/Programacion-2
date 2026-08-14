using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Transactions;

namespace ClassLibrary1
{
    public class Producto : IObservador
    {
        public int Id { get; set; } 
        public string? descripcion { get; set; }
        public double precioDolares {  get; set; }
        public double precioEnPesos { get; set; }

        public Producto(int id, string? descripcion, double precioDolares)
        {
            Id = id;
            this.descripcion = descripcion;
            this.precioDolares = precioDolares;
            this.precioEnPesos = precioDolares * CotizaciónDolar.Instancia.obtenerCotizacion();
        }

        public void actualizarCotizacionDolar()
        {
            precioEnPesos = precioDolares * CotizaciónDolar.Instancia.obtenerCotizacion();

        }
    }
}
