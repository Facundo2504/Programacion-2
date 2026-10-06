using System;
using System.Collections.Generic;
using System.Text;

namespace Observer.Core
{
    public interface IPanel
    {
        void Actualizar(Lectura lectura);
    }
}
