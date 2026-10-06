using Observer.Core;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace Observer.WinForms
{
    public partial class FrmPrincipal : Form
    {
        private EstacionMeteorologica _estacion;

        public FrmPrincipal ( )
        {
            InitializeComponent ();
            _estacion = new EstacionMeteorologica ();

            _estacion.Suscribir (panelActualControl1);
        }

        private void FrmPrincipal_Load ( object sender, EventArgs e )
        {

        }

        private void button1_Click ( object sender, EventArgs e )
        {

        }

        private void btnPublicar_Click(object sender, EventArgs e)
        {
            double temperatura =
                (double)nudTemperatura.Value;

            double humedad =
                (double)nudHumedad.Value;

            Lectura lectura =
                new Lectura(temperatura, humedad, DateTime.Now);

            _estacion.Publicar(lectura);
        }
    }
}
