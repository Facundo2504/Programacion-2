namespace EjemploObserver
{
    partial class Form1
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
            button1 = new Button();
            button2 = new Button();
            textBox1 = new TextBox();
            button3 = new Button();
            button4 = new Button();
            textBox2 = new TextBox();
            label1 = new Label();
            button5 = new Button();
            button6 = new Button();
            SuspendLayout();
            // 
            // button1
            // 
            button1.Location = new Point(203, 52);
            button1.Name = "button1";
            button1.Size = new Size(159, 59);
            button1.TabIndex = 0;
            button1.Text = "Crear 3 Prod";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            // 
            // button2
            // 
            button2.Location = new Point(728, 288);
            button2.Name = "button2";
            button2.Size = new Size(140, 65);
            button2.TabIndex = 1;
            button2.Text = "Cambiar Dolar";
            button2.UseVisualStyleBackColor = true;
            button2.Click += button2_Click;
            // 
            // textBox1
            // 
            textBox1.Location = new Point(728, 230);
            textBox1.Name = "textBox1";
            textBox1.Size = new Size(169, 31);
            textBox1.TabIndex = 2;
            // 
            // button3
            // 
            button3.Location = new Point(203, 189);
            button3.Name = "button3";
            button3.Size = new Size(159, 51);
            button3.TabIndex = 3;
            button3.Text = "Ver Productos";
            button3.UseVisualStyleBackColor = true;
            button3.Click += button3_Click;
            // 
            // button4
            // 
            button4.Location = new Point(452, 405);
            button4.Name = "button4";
            button4.Size = new Size(272, 76);
            button4.TabIndex = 4;
            button4.Text = "Crear Observer";
            button4.UseVisualStyleBackColor = true;
            button4.Click += button4_Click;
            // 
            // textBox2
            // 
            textBox2.Location = new Point(637, 66);
            textBox2.Name = "textBox2";
            textBox2.Size = new Size(353, 31);
            textBox2.TabIndex = 5;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(550, 72);
            label1.Name = "label1";
            label1.Size = new Size(46, 25);
            label1.TabIndex = 6;
            label1.Text = "Noti";
            // 
            // button5
            // 
            button5.Location = new Point(776, 126);
            button5.Name = "button5";
            button5.Size = new Size(112, 34);
            button5.TabIndex = 7;
            button5.Text = "button5";
            button5.UseVisualStyleBackColor = true;
            button5.Click += button5_Click;
            // 
            // button6
            // 
            button6.Location = new Point(575, 148);
            button6.Name = "button6";
            button6.Size = new Size(123, 34);
            button6.TabIndex = 8;
            button6.Text = "Ver MEdios";
            button6.UseVisualStyleBackColor = true;
            button6.Click += button6_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(10F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1142, 591);
            Controls.Add(button6);
            Controls.Add(button5);
            Controls.Add(label1);
            Controls.Add(textBox2);
            Controls.Add(button4);
            Controls.Add(button3);
            Controls.Add(textBox1);
            Controls.Add(button2);
            Controls.Add(button1);
            Name = "Form1";
            Text = "Form1";
            Load += Form1_Load;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button button1;
        private Button button2;
        private TextBox textBox1;
        private Button button3;
        private Button button4;
        private TextBox textBox2;
        private Label label1;
        private Button button5;
        private Button button6;
    }
}
