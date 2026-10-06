namespace Backend.Configuracion
{
    public class Idioma
    {
        public int Id { get; set; }
        public string Nombre { get; set; }

        public Idioma(int id, string nombre)
        {
            Id = id;
            Nombre = nombre;
        }

        public override string ToString() => Nombre;
    }
}
