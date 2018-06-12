namespace SimpleImageDisplaySample
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
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
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.CameraIDTextBox = new System.Windows.Forms.TextBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.SearchButton = new System.Windows.Forms.Button();
            this.StartButton = new System.Windows.Forms.Button();
            this.StopButton = new System.Windows.Forms.Button();
            this.ImageSizeGroupBox = new System.Windows.Forms.GroupBox();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.HeightNumericUpDown = new System.Windows.Forms.NumericUpDown();
            this.WidthNumericUpDown = new System.Windows.Forms.NumericUpDown();
            this.GainGroupBox = new System.Windows.Forms.GroupBox();
            this.GainLabel = new System.Windows.Forms.Label();
            this.GainTrackBar = new System.Windows.Forms.TrackBar();
            this.asynchImageRecordingGroupBox = new System.Windows.Forms.GroupBox();
            this.recordingModeComboBox = new System.Windows.Forms.ComboBox();
            this.recordingModeLabel = new System.Windows.Forms.Label();
            this.saveRawCheckBox = new System.Windows.Forms.CheckBox();
            this.skipCountNumericUpDown = new System.Windows.Forms.NumericUpDown();
            this.skipCountLabel = new System.Windows.Forms.Label();
            this.saveButton = new System.Windows.Forms.Button();
            this.replayButton = new System.Windows.Forms.Button();
            this.stopCaptureButton = new System.Windows.Forms.Button();
            this.startCaptureButton = new System.Windows.Forms.Button();
            this.recordingCountLabel = new System.Windows.Forms.Label();
            this.captureCountNumericUpDown = new System.Windows.Forms.NumericUpDown();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.toolTip1 = new System.Windows.Forms.ToolTip(this.components);
            this.progressBar1 = new System.Windows.Forms.ProgressBar();
            this.recordingStatusLabel = new System.Windows.Forms.Label();
            this.groupBox1.SuspendLayout();
            this.ImageSizeGroupBox.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.HeightNumericUpDown)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.WidthNumericUpDown)).BeginInit();
            this.GainGroupBox.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.GainTrackBar)).BeginInit();
            this.asynchImageRecordingGroupBox.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.skipCountNumericUpDown)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.captureCountNumericUpDown)).BeginInit();
            this.SuspendLayout();
            // 
            // CameraIDTextBox
            // 
            this.CameraIDTextBox.Enabled = false;
            this.CameraIDTextBox.Location = new System.Drawing.Point(6, 18);
            this.CameraIDTextBox.Multiline = true;
            this.CameraIDTextBox.Name = "CameraIDTextBox";
            this.CameraIDTextBox.Size = new System.Drawing.Size(441, 42);
            this.CameraIDTextBox.TabIndex = 0;
            this.toolTip1.SetToolTip(this.CameraIDTextBox, "ID text string for the first camera detected during Device Discovery");
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.SearchButton);
            this.groupBox1.Controls.Add(this.CameraIDTextBox);
            this.groupBox1.Location = new System.Drawing.Point(12, 11);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(488, 66);
            this.groupBox1.TabIndex = 1;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "ID of the first camera found";
            // 
            // SearchButton
            // 
            this.SearchButton.Location = new System.Drawing.Point(453, 18);
            this.SearchButton.Name = "SearchButton";
            this.SearchButton.Size = new System.Drawing.Size(29, 21);
            this.SearchButton.TabIndex = 6;
            this.SearchButton.Text = "...";
            this.toolTip1.SetToolTip(this.SearchButton, "Search for cameras");
            this.SearchButton.UseVisualStyleBackColor = true;
            this.SearchButton.Click += new System.EventHandler(this.SearchButton_Click);
            // 
            // StartButton
            // 
            this.StartButton.Enabled = false;
            this.StartButton.Location = new System.Drawing.Point(425, 90);
            this.StartButton.Name = "StartButton";
            this.StartButton.Size = new System.Drawing.Size(75, 21);
            this.StartButton.TabIndex = 2;
            this.StartButton.Text = "Start";
            this.toolTip1.SetToolTip(this.StartButton, "Start Image Acquisition");
            this.StartButton.UseVisualStyleBackColor = true;
            this.StartButton.Click += new System.EventHandler(this.StartButton_Click);
            // 
            // StopButton
            // 
            this.StopButton.Enabled = false;
            this.StopButton.Location = new System.Drawing.Point(425, 117);
            this.StopButton.Name = "StopButton";
            this.StopButton.Size = new System.Drawing.Size(75, 21);
            this.StopButton.TabIndex = 3;
            this.StopButton.Text = "Stop";
            this.toolTip1.SetToolTip(this.StopButton, "Stop Image Acquisition");
            this.StopButton.UseVisualStyleBackColor = true;
            this.StopButton.Click += new System.EventHandler(this.StopButton_Click);
            // 
            // ImageSizeGroupBox
            // 
            this.ImageSizeGroupBox.Controls.Add(this.label2);
            this.ImageSizeGroupBox.Controls.Add(this.label1);
            this.ImageSizeGroupBox.Controls.Add(this.HeightNumericUpDown);
            this.ImageSizeGroupBox.Controls.Add(this.WidthNumericUpDown);
            this.ImageSizeGroupBox.Location = new System.Drawing.Point(12, 82);
            this.ImageSizeGroupBox.Name = "ImageSizeGroupBox";
            this.ImageSizeGroupBox.Size = new System.Drawing.Size(200, 84);
            this.ImageSizeGroupBox.TabIndex = 4;
            this.ImageSizeGroupBox.TabStop = false;
            this.ImageSizeGroupBox.Text = "Image Size";
            this.toolTip1.SetToolTip(this.ImageSizeGroupBox, "Image Size control");
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(7, 46);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(41, 12);
            this.label2.TabIndex = 6;
            this.label2.Text = "Height";
            this.toolTip1.SetToolTip(this.label2, "Height");
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(7, 20);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(35, 12);
            this.label1.TabIndex = 2;
            this.label1.Text = "Width";
            this.toolTip1.SetToolTip(this.label1, "Width");
            // 
            // HeightNumericUpDown
            // 
            this.HeightNumericUpDown.Enabled = false;
            this.HeightNumericUpDown.Location = new System.Drawing.Point(74, 44);
            this.HeightNumericUpDown.Name = "HeightNumericUpDown";
            this.HeightNumericUpDown.Size = new System.Drawing.Size(120, 21);
            this.HeightNumericUpDown.TabIndex = 1;
            this.toolTip1.SetToolTip(this.HeightNumericUpDown, "Height");
            this.HeightNumericUpDown.ValueChanged += new System.EventHandler(this.HeightNumericUpDown_ValueChanged);
            // 
            // WidthNumericUpDown
            // 
            this.WidthNumericUpDown.Enabled = false;
            this.WidthNumericUpDown.Location = new System.Drawing.Point(74, 18);
            this.WidthNumericUpDown.Name = "WidthNumericUpDown";
            this.WidthNumericUpDown.Size = new System.Drawing.Size(120, 21);
            this.WidthNumericUpDown.TabIndex = 0;
            this.toolTip1.SetToolTip(this.WidthNumericUpDown, "Width");
            this.WidthNumericUpDown.ValueChanged += new System.EventHandler(this.WidthNumericUpDown_ValueChanged);
            // 
            // GainGroupBox
            // 
            this.GainGroupBox.Controls.Add(this.GainLabel);
            this.GainGroupBox.Controls.Add(this.GainTrackBar);
            this.GainGroupBox.Location = new System.Drawing.Point(218, 82);
            this.GainGroupBox.Name = "GainGroupBox";
            this.GainGroupBox.Size = new System.Drawing.Size(200, 85);
            this.GainGroupBox.TabIndex = 5;
            this.GainGroupBox.TabStop = false;
            this.GainGroupBox.Text = "Gain Control";
            this.toolTip1.SetToolTip(this.GainGroupBox, "Gain Control");
            // 
            // GainLabel
            // 
            this.GainLabel.AutoSize = true;
            this.GainLabel.Enabled = false;
            this.GainLabel.Location = new System.Drawing.Point(12, 19);
            this.GainLabel.Name = "GainLabel";
            this.GainLabel.Size = new System.Drawing.Size(11, 12);
            this.GainLabel.TabIndex = 2;
            this.GainLabel.Text = "0";
            this.toolTip1.SetToolTip(this.GainLabel, "Gain (Raw)");
            // 
            // GainTrackBar
            // 
            this.GainTrackBar.Enabled = false;
            this.GainTrackBar.Location = new System.Drawing.Point(6, 42);
            this.GainTrackBar.Name = "GainTrackBar";
            this.GainTrackBar.Size = new System.Drawing.Size(187, 45);
            this.GainTrackBar.TabIndex = 1;
            this.toolTip1.SetToolTip(this.GainTrackBar, "Gain (Raw)");
            this.GainTrackBar.Scroll += new System.EventHandler(this.GainTrackBar_Scroll);
            // 
            // asynchImageRecordingGroupBox
            // 
            this.asynchImageRecordingGroupBox.Controls.Add(this.recordingModeComboBox);
            this.asynchImageRecordingGroupBox.Controls.Add(this.recordingModeLabel);
            this.asynchImageRecordingGroupBox.Controls.Add(this.progressBar1);
            this.asynchImageRecordingGroupBox.Controls.Add(this.saveRawCheckBox);
            this.asynchImageRecordingGroupBox.Controls.Add(this.skipCountNumericUpDown);
            this.asynchImageRecordingGroupBox.Controls.Add(this.skipCountLabel);
            this.asynchImageRecordingGroupBox.Controls.Add(this.recordingStatusLabel);
            this.asynchImageRecordingGroupBox.Controls.Add(this.saveButton);
            this.asynchImageRecordingGroupBox.Controls.Add(this.replayButton);
            this.asynchImageRecordingGroupBox.Controls.Add(this.stopCaptureButton);
            this.asynchImageRecordingGroupBox.Controls.Add(this.startCaptureButton);
            this.asynchImageRecordingGroupBox.Controls.Add(this.recordingCountLabel);
            this.asynchImageRecordingGroupBox.Controls.Add(this.captureCountNumericUpDown);
            this.asynchImageRecordingGroupBox.Location = new System.Drawing.Point(13, 173);
            this.asynchImageRecordingGroupBox.Name = "asynchImageRecordingGroupBox";
            this.asynchImageRecordingGroupBox.Size = new System.Drawing.Size(487, 117);
            this.asynchImageRecordingGroupBox.TabIndex = 6;
            this.asynchImageRecordingGroupBox.TabStop = false;
            this.asynchImageRecordingGroupBox.Text = "Asynchronous Image Recording Control";
            this.toolTip1.SetToolTip(this.asynchImageRecordingGroupBox, "Asynchronous Image Recording Control");
            // 
            // recordingModeComboBox
            // 
            this.recordingModeComboBox.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.recordingModeComboBox.FormattingEnabled = true;
            this.recordingModeComboBox.Items.AddRange(new object[] {
            "List",
            "Cyclical"});
            this.recordingModeComboBox.Location = new System.Drawing.Point(101, 66);
            this.recordingModeComboBox.Name = "recordingModeComboBox";
            this.recordingModeComboBox.Size = new System.Drawing.Size(92, 20);
            this.recordingModeComboBox.TabIndex = 12;
            // 
            // recordingModeLabel
            // 
            this.recordingModeLabel.AutoSize = true;
            this.recordingModeLabel.Location = new System.Drawing.Point(6, 68);
            this.recordingModeLabel.Name = "recordingModeLabel";
            this.recordingModeLabel.Size = new System.Drawing.Size(95, 12);
            this.recordingModeLabel.TabIndex = 11;
            this.recordingModeLabel.Text = "Recording mode:";
            // 
            // saveRawCheckBox
            // 
            this.saveRawCheckBox.AutoSize = true;
            this.saveRawCheckBox.Location = new System.Drawing.Point(405, 44);
            this.saveRawCheckBox.Name = "saveRawCheckBox";
            this.saveRawCheckBox.Size = new System.Drawing.Size(72, 16);
            this.saveRawCheckBox.TabIndex = 9;
            this.saveRawCheckBox.Text = "Save Raw";
            this.saveRawCheckBox.UseVisualStyleBackColor = true;
            // 
            // skipCountNumericUpDown
            // 
            this.skipCountNumericUpDown.Location = new System.Drawing.Point(101, 42);
            this.skipCountNumericUpDown.Maximum = new decimal(new int[] {
            500,
            0,
            0,
            0});
            this.skipCountNumericUpDown.Name = "skipCountNumericUpDown";
            this.skipCountNumericUpDown.Size = new System.Drawing.Size(92, 21);
            this.skipCountNumericUpDown.TabIndex = 8;
            this.toolTip1.SetToolTip(this.skipCountNumericUpDown, "Number of frames to skip during recording");
            // 
            // skipCountLabel
            // 
            this.skipCountLabel.AutoSize = true;
            this.skipCountLabel.Location = new System.Drawing.Point(6, 43);
            this.skipCountLabel.Name = "skipCountLabel";
            this.skipCountLabel.Size = new System.Drawing.Size(71, 12);
            this.skipCountLabel.TabIndex = 7;
            this.skipCountLabel.Text = "Skip Count:";
            this.toolTip1.SetToolTip(this.skipCountLabel, "Number of frames to skip during recording");
            // 
            // saveButton
            // 
            this.saveButton.Location = new System.Drawing.Point(404, 17);
            this.saveButton.Name = "saveButton";
            this.saveButton.Size = new System.Drawing.Size(77, 21);
            this.saveButton.TabIndex = 5;
            this.saveButton.Text = "Save";
            this.toolTip1.SetToolTip(this.saveButton, "Save recorded images to disk");
            this.saveButton.UseVisualStyleBackColor = true;
            this.saveButton.Click += new System.EventHandler(this.saveButton_Click);
            // 
            // replayButton
            // 
            this.replayButton.Location = new System.Drawing.Point(311, 17);
            this.replayButton.Name = "replayButton";
            this.replayButton.Size = new System.Drawing.Size(87, 21);
            this.replayButton.TabIndex = 4;
            this.replayButton.Text = "Replay";
            this.toolTip1.SetToolTip(this.replayButton, "Replay recorded images in a seperate window");
            this.replayButton.UseVisualStyleBackColor = true;
            this.replayButton.Click += new System.EventHandler(this.replayButton_Click);
            // 
            // stopCaptureButton
            // 
            this.stopCaptureButton.Location = new System.Drawing.Point(205, 41);
            this.stopCaptureButton.Name = "stopCaptureButton";
            this.stopCaptureButton.Size = new System.Drawing.Size(100, 21);
            this.stopCaptureButton.TabIndex = 3;
            this.stopCaptureButton.Text = "Stop recording";
            this.toolTip1.SetToolTip(this.stopCaptureButton, "Stop Image Recording");
            this.stopCaptureButton.UseVisualStyleBackColor = true;
            this.stopCaptureButton.Click += new System.EventHandler(this.stopCaptureButton_Click);
            // 
            // startCaptureButton
            // 
            this.startCaptureButton.Location = new System.Drawing.Point(205, 17);
            this.startCaptureButton.Name = "startCaptureButton";
            this.startCaptureButton.Size = new System.Drawing.Size(100, 21);
            this.startCaptureButton.TabIndex = 2;
            this.startCaptureButton.Text = "Start recording";
            this.toolTip1.SetToolTip(this.startCaptureButton, "Start Image Recording");
            this.startCaptureButton.UseVisualStyleBackColor = true;
            this.startCaptureButton.Click += new System.EventHandler(this.startCaptureButton_Click);
            // 
            // recordingCountLabel
            // 
            this.recordingCountLabel.AutoSize = true;
            this.recordingCountLabel.Location = new System.Drawing.Point(6, 19);
            this.recordingCountLabel.Name = "recordingCountLabel";
            this.recordingCountLabel.Size = new System.Drawing.Size(101, 12);
            this.recordingCountLabel.TabIndex = 1;
            this.recordingCountLabel.Text = "Recording count:";
            this.toolTip1.SetToolTip(this.recordingCountLabel, "Number of frames to record");
            // 
            // captureCountNumericUpDown
            // 
            this.captureCountNumericUpDown.Location = new System.Drawing.Point(101, 18);
            this.captureCountNumericUpDown.Maximum = new decimal(new int[] {
            500,
            0,
            0,
            0});
            this.captureCountNumericUpDown.Name = "captureCountNumericUpDown";
            this.captureCountNumericUpDown.Size = new System.Drawing.Size(92, 21);
            this.captureCountNumericUpDown.TabIndex = 0;
            this.toolTip1.SetToolTip(this.captureCountNumericUpDown, "Number of frames to record");
            this.captureCountNumericUpDown.Value = new decimal(new int[] {
            100,
            0,
            0,
            0});
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // progressBar1
            // 
            this.progressBar1.Location = new System.Drawing.Point(205, 90);
            this.progressBar1.Name = "progressBar1";
            this.progressBar1.Size = new System.Drawing.Size(276, 18);
            this.progressBar1.TabIndex = 10;
            // 
            // recordingStatusLabel
            // 
            this.recordingStatusLabel.AutoSize = true;
            this.recordingStatusLabel.Location = new System.Drawing.Point(6, 92);
            this.recordingStatusLabel.Name = "recordingStatusLabel";
            this.recordingStatusLabel.Size = new System.Drawing.Size(113, 12);
            this.recordingStatusLabel.TabIndex = 6;
            this.recordingStatusLabel.Text = "Recording Stopped.";
            this.toolTip1.SetToolTip(this.recordingStatusLabel, "Status for the recording");
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(512, 303);
            this.Controls.Add(this.asynchImageRecordingGroupBox);
            this.Controls.Add(this.GainGroupBox);
            this.Controls.Add(this.ImageSizeGroupBox);
            this.Controls.Add(this.StopButton);
            this.Controls.Add(this.StartButton);
            this.Controls.Add(this.groupBox1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
            this.Name = "Form1";
            this.Text = "Asynchronous Image Recording Sample";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Form1_FormClosing);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ImageSizeGroupBox.ResumeLayout(false);
            this.ImageSizeGroupBox.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.HeightNumericUpDown)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.WidthNumericUpDown)).EndInit();
            this.GainGroupBox.ResumeLayout(false);
            this.GainGroupBox.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.GainTrackBar)).EndInit();
            this.asynchImageRecordingGroupBox.ResumeLayout(false);
            this.asynchImageRecordingGroupBox.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.skipCountNumericUpDown)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.captureCountNumericUpDown)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.TextBox CameraIDTextBox;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button StartButton;
        private System.Windows.Forms.Button StopButton;
        private System.Windows.Forms.GroupBox ImageSizeGroupBox;
        private System.Windows.Forms.NumericUpDown HeightNumericUpDown;
        private System.Windows.Forms.NumericUpDown WidthNumericUpDown;
        private System.Windows.Forms.GroupBox GainGroupBox;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TrackBar GainTrackBar;
        private System.Windows.Forms.Button SearchButton;
        private System.Windows.Forms.Label GainLabel;
        private System.Windows.Forms.GroupBox asynchImageRecordingGroupBox;
        private System.Windows.Forms.Button saveButton;
        private System.Windows.Forms.Button replayButton;
        private System.Windows.Forms.Button stopCaptureButton;
        private System.Windows.Forms.Button startCaptureButton;
        private System.Windows.Forms.Label recordingCountLabel;
        private System.Windows.Forms.NumericUpDown captureCountNumericUpDown;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.Label skipCountLabel;
        private System.Windows.Forms.NumericUpDown skipCountNumericUpDown;
        private System.Windows.Forms.ToolTip toolTip1;
        private System.Windows.Forms.CheckBox saveRawCheckBox;
        private System.Windows.Forms.ComboBox recordingModeComboBox;
        private System.Windows.Forms.Label recordingModeLabel;
        private System.Windows.Forms.ProgressBar progressBar1;
        private System.Windows.Forms.Label recordingStatusLabel;
    }
}

