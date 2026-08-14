using System;
using System.Collections.Generic;
using System.Text;

namespace Observer.Core
{
    public class EstacionMeteorologica
    {
        private readonly List<IPanel> _paneles = new();

        public void Suscribir(IPanel panel)
        {
            _paneles.Add(panel);
        }

        public void Desuscribir(IPanel panel)
        {
            _paneles.Remove(panel);
        }

        public void Publicar(Lectura lectura)
        {
            foreach (IPanel panel in _paneles)
            {
                panel.Actualizar(lectura);
            }
        }
    }
}
