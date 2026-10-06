using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassLibrary1
{
    public class CotizaciónDolar
    {
        private static CotizaciónDolar? instance;

        private double Cotizacion { get; set; } = 1100;

        private string ultimaNoticia { get; set; } = "Nuevo Seguro de Incendio para casas!!"; 

        public static CotizaciónDolar Instancia
        {
            get
            {
                if (instance == null)
                {
                    instance = new CotizaciónDolar();
                }
                return instance;
            }
        }
        public string obtenerUltimaNot()
        {
            return ultimaNoticia;
        }

        public void ponerUltimaNoti(string laNoticia)
        {
            ultimaNoticia = laNoticia; 
        }

        public double obtenerCotizacion()
        {
            return Cotizacion;
        }

        public void ponerCotizacion(double Valor)
        {
            Cotizacion = Valor;
        }
    }
}
