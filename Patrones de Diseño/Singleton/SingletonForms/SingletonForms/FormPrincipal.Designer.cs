namespace SingletonForms
{
    partial class FormPrincipal
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            comboIdiomas = new ComboBox();
            lblIdioma = new Label();
            btnForm2 = new Button();
            btnForm3 = new Button();
            SuspendLayout();
            // 
            // comboIdiomas
            // 
            comboIdiomas.DropDownStyle = ComboBoxStyle.DropDownList;
            comboIdiomas.Location = new Point(20, 20);
            comboIdiomas.Name = "comboIdiomas";
            comboIdiomas.Size = new Size(121, 28);
            comboIdiomas.TabIndex = 0;
            // 
            // lblIdioma
            // 
            lblIdioma.AutoSize = true;
            lblIdioma.Location = new Point(20, 60);
            lblIdioma.Name = "lblIdioma";
            lblIdioma.Size = new Size(0, 20);
            lblIdioma.TabIndex = 1;
            // 
            // btnForm2
            // 
            btnForm2.Location = new Point(20, 100);
            btnForm2.Name = "btnForm2";
            btnForm2.Size = new Size(75, 23);
            btnForm2.TabIndex = 2;
            btnForm2.Text = "Abrir Form2";
            // 
            // btnForm3
            // 
            btnForm3.Location = new Point(140, 100);
            btnForm3.Name = "btnForm3";
            btnForm3.Size = new Size(75, 23);
            btnForm3.TabIndex = 3;
            btnForm3.Text = "Abrir Form3";
            // 
            // FormPrincipal
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(comboIdiomas);
            Controls.Add(lblIdioma);
            Controls.Add(btnForm2);
            Controls.Add(btnForm3);
            Name = "FormPrincipal";
            Text = "Form1";
            Load += FormPrincipal_Load;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private ComboBox comboIdiomas;
        private Label lblIdioma;
        private Button btnForm2;
        private Button btnForm3;
    }
}
