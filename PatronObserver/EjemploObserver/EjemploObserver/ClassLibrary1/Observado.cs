using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassLibrary1
{
    public class Observado
    {
        private CotizaciónDolar observado { get; set; } = CotizaciónDolar.Instancia;

        private List<IObservador> observadores = new List<IObservador>();

        public void PonerObservado(CotizaciónDolar aObservar)
        {
            observado = aObservar;
        }

        public void agregarUnObservador(IObservador itemQueVaAObservar)
        {
            observadores.Add(itemQueVaAObservar);
        }
        private void notificarObservadores()
        {
            foreach (IObservador item in observadores)
            {
                item.actualizarCotizacionDolar();
            }
        }

        public void modificarCotización(double nuevaCotiz)
        {
            observado.ponerCotizacion(nuevaCotiz);
            notificarObservadores();
        }
    }
}
