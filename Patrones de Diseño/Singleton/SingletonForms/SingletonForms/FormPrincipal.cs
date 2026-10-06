using System;
using System.Windows.Forms;
using System.Drawing;
using Backend.Configuracion;

namespace SingletonForms
{
    public partial class FormPrincipal : Form
    {
        public FormPrincipal()
        {
            InitializeComponent();

            // Poblar combo con idiomas disponibles usando la clase Idioma
            comboIdiomas.Items.AddRange(new object[] {
                new Idioma(1, "Español"),
                new Idioma(2, "English"),
                new Idioma(3, "Português"),
                new Idioma(4, "Français"),
                new Idioma(5, "Deutsch")
            });
            comboIdiomas.SelectedIndexChanged += ComboIdiomas_SelectedIndexChanged;

            // Botones
            btnForm2.Click += BtnForm2_Click;
            btnForm3.Click += BtnForm3_Click;

            // Mostrar el idioma actual desde el singleton
            lblIdioma.Text = "Idioma: " + ConfigSingleton.Instancia.IdiomaSeleccionado.Nombre;
        }

        private void ComboIdiomas_SelectedIndexChanged(object? sender, EventArgs e)
        {
            var idiomaSeleccionado = comboIdiomas.SelectedItem as Idioma;
            if (idiomaSeleccionado == null)
                return;

            ConfigSingleton.Instancia.SeleccionarIdioma(idiomaSeleccionado);
            lblIdioma.Text = "Idioma: " + ConfigSingleton.Instancia.IdiomaSeleccionado.Nombre;
        }

        private void BtnForm2_Click(object? sender, EventArgs e)
        {
            var f2 = new Form2();
            f2.Show();
        }

        private void BtnForm3_Click(object? sender, EventArgs e)
        {
            var f3 = new Form3();
            f3.Show();
        }

        private void FormPrincipal_Load(object sender, EventArgs e)
        {
            // Establecer el idioma inicial en el combo según el singleton
            var actual = ConfigSingleton.Instancia.IdiomaSeleccionado?.Nombre;
            for (int i = 0; i < comboIdiomas.Items.Count; i++)
            {
                if (comboIdiomas.Items[i]?.ToString() == actual)
                {
                    comboIdiomas.SelectedIndex = i;
                    break;
                }
            }
        }
    }
}
