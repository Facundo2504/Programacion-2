using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassLibrary1
{
    public class ObservaNoti
    {
        private CotizaciónDolar observado { get; set; } = CotizaciónDolar.Instancia;

        private List<IObservadorNoti> observadores = new List<IObservadorNoti>();

        public void PonerObservado(CotizaciónDolar aObservar)
        {
            observado = aObservar;
        }

        public void agregarUnObservador(IObservadorNoti itemQueVaAObservar)
        {
            observadores.Add(itemQueVaAObservar);
        }
        private void notificarObservadores()
        {
            foreach (IObservadorNoti item in observadores)
            {
                item.actualizarUltimomento();
            }
        }

        public void modificarUltimaNoti(string noticiaUltima)
        {
            observado.ponerUltimaNoti(noticiaUltima);
            notificarObservadores();
        }
    }
}
