namespace Observer.WinForms
{
    partial class PanelActualControl
    {
        /// <summary> 
        /// Variable del diseñador necesaria.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary> 
        /// Limpiar los recursos que se estén usando.
        /// </summary>
        /// <param name="disposing">true si los recursos administrados se deben desechar; false en caso contrario.</param>
        protected override void Dispose ( bool disposing )
        {
            if (disposing && (components != null))
            {
                components.Dispose ();
            }
            base.Dispose (disposing);
        }

        #region Código generado por el Diseñador de componentes

        /// <summary> 
        /// Método necesario para admitir el Diseñador. No se puede modificar
        /// el contenido de este método con el editor de código.
        /// </summary>
        private void InitializeComponent ( )
        {
            lblTemperatura = new Label ();
            lblHumedad = new Label ();
            flowLayoutPanel1 = new FlowLayoutPanel ();
            SuspendLayout ();
            // 
            // lblTemperatura
            // 
            lblTemperatura.AutoSize = true;
            lblTemperatura.Location = new Point (70, 226);
            lblTemperatura.Name = "lblTemperatura";
            lblTemperatura.Size = new Size (100, 20);
            lblTemperatura.TabIndex = 0;
            lblTemperatura.Text = "Temperatura: ";
            lblTemperatura.Click += lblTemperatura_Click;
            // 
            // lblHumedad
            // 
            lblHumedad.AutoSize = true;
            lblHumedad.Location = new Point (70, 278);
            lblHumedad.Name = "lblHumedad";
            lblHumedad.Size = new Size (82, 20);
            lblHumedad.TabIndex = 1;
            lblHumedad.Text = "Humedad: ";
            // 
            // flowLayoutPanel1
            // 
            flowLayoutPanel1.Location = new Point (567, 175);
            flowLayoutPanel1.Name = "flowLayoutPanel1";
            flowLayoutPanel1.Size = new Size (8, 8);
            flowLayoutPanel1.TabIndex = 2;
            // 
            // PanelActualControl
            // 
            AutoScaleDimensions = new SizeF (8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            Controls.Add (flowLayoutPanel1);
            Controls.Add (lblHumedad);
            Controls.Add (lblTemperatura);
            Name = "PanelActualControl";
            Size = new Size (890, 560);
            Load += PanelActualControl_Load;
            ResumeLayout (false);
            PerformLayout ();
        }

        #endregion

        private Label lblTemperatura;
        private Label lblHumedad;
        private FlowLayoutPanel flowLayoutPanel1;
    }
}
