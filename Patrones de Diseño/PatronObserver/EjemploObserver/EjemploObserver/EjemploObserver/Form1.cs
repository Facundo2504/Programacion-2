using ClassLibrary1;

namespace EjemploObserver
{
    public partial class Form1 : Form
    {
        private ObservaNoti miObservaNoti = new ObservaNoti();

        public Form1()
        {
            InitializeComponent();
            miObservaNoti.agregarUnObservador(new Medio());

            miObservaNoti.agregarUnObservador(new Medio());

            miObservaNoti.agregarUnObservador(new Medio());


        }
        private Observado observado;
        private List<Producto> listaProductos = new List<Producto>();

        private void button1_Click(object sender, EventArgs e)
        {
            listaProductos.Add(new Producto(234, "tornillos", 1));
            listaProductos.Add(new Producto(246, "Pinzas", 10));
            listaProductos.Add(new Producto(334, "MArtillos", 5));

        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (observado == null)
            {
                CotizaciónDolar.Instancia.ponerCotizacion(double.Parse(textBox1.Text));
            }
            else
            {
                observado.modificarCotización(double.Parse(textBox1.Text));
            }

            MessageBox.Show("El dolar vale ahora: " + CotizaciónDolar.Instancia.obtenerCotizacion().ToString());

        }

        private void button3_Click(object sender, EventArgs e)
        {
            string mensaje = string.Empty;
            foreach (Producto item in listaProductos)
            {
                mensaje += item.descripcion + " - Valor Pesos: " + item.precioEnPesos.ToString();
                mensaje += Environment.NewLine;

            }
            MessageBox.Show(mensaje);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            observado = new Observado();

            foreach (Producto item in listaProductos)
            {
                observado.agregarUnObservador(item);
            }


        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {
            miObservaNoti.modificarUltimaNoti(textBox2.Text);

        }

        private void button6_Click(object sender, EventArgs e)
        {
            MessageBox.Show("AVER");

        }
    }
}
