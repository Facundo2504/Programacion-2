using System;

namespace Backend.Configuracion
{
    public sealed class ConfigSingleton
    {
        private static readonly ConfigSingleton _instancia = new ConfigSingleton();

        public static ConfigSingleton Instancia => _instancia;

        public Idioma IdiomaSeleccionado { get; private set; }

        private ConfigSingleton()
        {
            IdiomaSeleccionado = new Idioma(1, "Español");
        }

        public void SeleccionarIdioma(Idioma idioma)
        {
            if (idioma == null)
            {
                throw new ArgumentNullException(nameof(idioma));
            }

            IdiomaSeleccionado = idioma;
        }
    }
}
