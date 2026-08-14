using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using Observer.Core;

namespace Observer.WinForms
{
    public partial class PanelActualControl : UserControl
    {
        public PanelActualControl ( )
        {
            InitializeComponent ();
        }

        private void PanelActualControl_Load ( object sender, EventArgs e )
        {

        }
        public void Actualizar ( Lectura lectura )
        {
            lblTemperatura.Text =
                $"Temperatura: {lectura.Temperatura} °C";

            lblHumedad.Text =
                $"Humedad: {lectura.Humedad} %";
        }

        private void lblTemperatura_Click ( object sender, EventArgs e )
        {

        }
    }
}
