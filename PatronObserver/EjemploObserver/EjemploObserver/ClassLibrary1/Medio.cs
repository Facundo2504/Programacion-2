using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassLibrary1
{
    public class Medio : IObservadorNoti
    {
        private string NoticiaQueVoyAEnviarAlDiarioeImprimirPorAhi;

        public void actualizarUltimomento()
        {
            NoticiaQueVoyAEnviarAlDiarioeImprimirPorAhi = CotizaciónDolar.Instancia.obtenerUltimaNot();
            // FLASHHSS!!!!  AAAASSSHHHH!!!

        }
    }
}
