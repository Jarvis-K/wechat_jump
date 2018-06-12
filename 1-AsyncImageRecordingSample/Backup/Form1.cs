using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using Jai_FactoryDotNET;
using System.Threading;

namespace SimpleImageDisplaySample
{
    public partial class Form1 : Form
    {
        // Main factory object
        CFactory myFactory = new CFactory();

        // Opened camera object
        CCamera myCamera;

        // GenICam nodes
        CNode myWidthNode;
        CNode myHeightNode;
        CNode myGainNode;

        private int _progressCharIndex = 0;

        public Form1()
        {
            InitializeComponent();

            Jai_FactoryWrapper.EFactoryError error = Jai_FactoryWrapper.EFactoryError.Success;

            // Open the factory with the default Registry database
            error = myFactory.Open("");

            // Search for cameras and update all controls
            SearchButton_Click(null, null);

            recordingModeComboBox.SelectedIndex = 0;
        }

        private void WidthNumericUpDown_ValueChanged(object sender, EventArgs e)
        {
            if (myWidthNode != null)
            {
                myWidthNode.Value = int.Parse(WidthNumericUpDown.Value.ToString());
                SetFramegrabberValue("Width", (Int64)myWidthNode.Value);
            }
        }

        private void HeightNumericUpDown_ValueChanged(object sender, EventArgs e)
        {
            if (myHeightNode != null)
            {
                myHeightNode.Value = int.Parse(HeightNumericUpDown.Value.ToString());
                SetFramegrabberValue("Height", (Int64)myHeightNode.Value);
            }
        }

        private void GainTrackBar_Scroll(object sender, EventArgs e)
        {
            if (myGainNode != null)
                myGainNode.Value = int.Parse(GainTrackBar.Value.ToString());

            GainLabel.Text = myGainNode.Value.ToString();
        }

        private void StartButton_Click(object sender, EventArgs e)
        {
            if (myCamera != null)
                myCamera.StartImageAcquisition(true, 5);
        }

        private void StopButton_Click(object sender, EventArgs e)
        {
            if (myCamera != null)
                myCamera.StopImageAcquisition();
        }

        private void SearchButton_Click(object sender, EventArgs e)
        {
            if (null != myCamera)
            {
                if (myCamera.IsOpen)
                {
                    myCamera.Close();
                }

                myCamera = null;
            }

            // Discover GigE and/or generic GenTL devices using myFactory.UpdateCameraList(in this case specifying Filter Driver for GigE cameras).
            myFactory.UpdateCameraList(Jai_FactoryDotNET.CFactory.EDriverType.FilterDriver);

            // Open the camera - first check for GigE devices
            for (int i = 0; i < myFactory.CameraList.Count; i++)
            {
                myCamera = myFactory.CameraList[i];
                if (Jai_FactoryWrapper.EFactoryError.Success == myCamera.Open())
                {
                    break;
                }
            }

            if (null != myCamera && myCamera.IsOpen)
            {
                CameraIDTextBox.Text = myCamera.CameraID;

                // Attach an event that will be called every time the Async Recording finishes
                myCamera.AsyncImageRecordingDoneEvent += new CCamera.AsyncImageRecordingDoneHandler(myCamera_AsyncImageRecordingDoneEvent);

                if (myCamera.NumOfDataStreams > 0)
                {
                    StartButton.Enabled = true;
                    StopButton.Enabled = true;
                }
                else
                {
                    StartButton.Enabled = false;
                    StopButton.Enabled = false;
                    startCaptureButton.Enabled = false;
                }

                int currentValue = 0;

                // Get the Width GenICam Node
                myWidthNode = myCamera.GetNode("Width");
                if (myWidthNode != null)
                {
                    currentValue = int.Parse(myWidthNode.Value.ToString());

                    // Update range for the Numeric Up/Down control
                    // Convert from integer to Decimal type
                    WidthNumericUpDown.Maximum = decimal.Parse(myWidthNode.Max.ToString());
                    WidthNumericUpDown.Minimum = decimal.Parse(myWidthNode.Min.ToString());
                    WidthNumericUpDown.Value = decimal.Parse(currentValue.ToString());

                    WidthNumericUpDown.Enabled = true;
                }
                else
                    WidthNumericUpDown.Enabled = false;

                SetFramegrabberValue("Width", (Int64)myWidthNode.Value);

                // Get the Height GenICam Node
                myHeightNode = myCamera.GetNode("Height");
                if (myHeightNode != null)
                {
                    currentValue = int.Parse(myHeightNode.Value.ToString());

                    // Update range for the Numeric Up/Down control
                    // Convert from integer to Decimal type
                    HeightNumericUpDown.Maximum = decimal.Parse(myHeightNode.Max.ToString());
                    HeightNumericUpDown.Minimum = decimal.Parse(myHeightNode.Min.ToString());
                    HeightNumericUpDown.Value = decimal.Parse(currentValue.ToString());

                    HeightNumericUpDown.Enabled = true;
                }
                else
                    HeightNumericUpDown.Enabled = false;

                SetFramegrabberValue("Height", (Int64)myHeightNode.Value);

                SetFramegrabberPixelFormat();

                // Get the GainRaw GenICam Node
                myGainNode = myCamera.GetNode("GainRaw");
                if (myGainNode != null)
                {
                    currentValue = int.Parse(myGainNode.Value.ToString());

                    // Update range for the TrackBar Controls
                    GainTrackBar.Maximum = int.Parse(myGainNode.Max.ToString());
                    GainTrackBar.Minimum = int.Parse(myGainNode.Min.ToString());
                    GainTrackBar.Value = currentValue;
                    GainLabel.Text = myGainNode.Value.ToString();

                    GainLabel.Enabled = true;
                    GainTrackBar.Enabled = true;
                }
                else
                {
                    GainLabel.Enabled = false;
                    GainTrackBar.Enabled = false;
                }
            }
            else
            {
                StartButton.Enabled = false;
                StopButton.Enabled = false;
                WidthNumericUpDown.Enabled = false;
                HeightNumericUpDown.Enabled = true;
                GainLabel.Enabled = false;
                GainTrackBar.Enabled = false;

                MessageBox.Show("No Cameras Found!");
            }
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (myCamera != null)
            {                
                stopCaptureButton_Click(null, null);
                myCamera.Close();
            }
        }

        private void startCaptureButton_Click(object sender, EventArgs e)
        {
            if (myCamera != null)
            {
                if (myCamera.IsAsyncImageRecordingRunning || (myCamera.TotalAsyncImagesRecordedCount > 0))
                {
                    DialogResult res = MessageBox.Show(this, "The Asychynchronuous Image Recording is already active or the internal buffer is not empty! Do you want to restart the image recording and discard recorded images?", "Asynchronous Image Capture", MessageBoxButtons.YesNo, MessageBoxIcon.Question, MessageBoxDefaultButton.Button2);

                    if (res == DialogResult.Yes)
                    {
                        myCamera.StopAsyncImageRecording();
                        myCamera.FreeAsyncRecordedImages();
                        myCamera.StartAsyncImageRecording(Convert.ToInt32(captureCountNumericUpDown.Value), (CCamera.AsyncImageRecordingMode)recordingModeComboBox.SelectedIndex, Convert.ToInt32(skipCountNumericUpDown.Value));
                    }
                }
                else
                {
                    myCamera.StartAsyncImageRecording(Convert.ToInt32(captureCountNumericUpDown.Value), (CCamera.AsyncImageRecordingMode)recordingModeComboBox.SelectedIndex, Convert.ToInt32(skipCountNumericUpDown.Value));
                }
            }
        }

        void myCamera_AsyncImageRecordingDoneEvent(int Count)
        {
            MessageBox.Show("Done capturing " + Count.ToString() + " images asynchronously!", "Asynch Image Capture");
        }

        private void stopCaptureButton_Click(object sender, EventArgs e)
        {
            if (myCamera != null)
            {
                myCamera.StopAsyncImageRecording();

                progressBar1.Style = ProgressBarStyle.Blocks;
                progressBar1.Minimum = 0;
                progressBar1.Maximum = myCamera.AsyncImageRecordingCount;
                progressBar1.Value = myCamera.TotalAsyncImagesRecordedCount;
                progressBar1.Enabled = false;
            }
        }

        private void replayButton_Click(object sender, EventArgs e)
        {
            // Here we have access to the stored images! Lets show them in an image window!!
            //Create a replay window
            if (myCamera != null && !myCamera.IsAsyncImageRecordingRunning && (myCamera.TotalAsyncImagesRecordedCount > 0))
            {
                IntPtr WindowHandle = IntPtr.Zero;

                // Try to read get the maximum width and height by looking for "SensorWidth" and "SensorHeight"
                Int32 Width = 0;
                Int32 Height = 0;
                CNode WidthNode = myCamera.GetNode("Width");
                CNode HeightNode = myCamera.GetNode("Height");

                Width = Convert.ToInt32(WidthNode.Max);
                Height = Convert.ToInt32(HeightNode.Max);

                IntPtr nodeHandle;

                uint BytesPerPixel = 4;
                if (Jai_FactoryWrapper.J_Camera_GetNodeByName(myCamera.CameraHandle, "PixelFormat", out nodeHandle) == Jai_FactoryWrapper.EFactoryError.Success)
                {
                    Int64 value = 0;
                    if (Jai_FactoryWrapper.J_Node_GetValueInt64(nodeHandle, false, ref value) == Jai_FactoryWrapper.EFactoryError.Success)
                    {
                        Jai_FactoryWrapper.EPixelFormatType pixeltype = (Jai_FactoryWrapper.EPixelFormatType)value;
                        BytesPerPixel = Jai_FactoryWrapper.GetPixelTypeMemorySize(pixeltype);
                    }
                }

                Jai_FactoryWrapper.SIZE maxSize = new Jai_FactoryWrapper.SIZE(Width, Height);

                Jai_FactoryWrapper.EFactoryError error = Jai_FactoryWrapper.EFactoryError.Success;

                // Calculate the size of the window rect to display the images
                int RectWidth = 0;
                int RectHeight = 0;

                Jai_FactoryWrapper.RECT frameRect = new Jai_FactoryWrapper.RECT(0, 0, 100, 100); ;

                // Does the image fit in width?
                if ((Width + 2 * System.Windows.Forms.SystemInformation.Border3DSize.Width) > System.Windows.Forms.Screen.PrimaryScreen.WorkingArea.Width)
                    RectWidth = System.Windows.Forms.Screen.PrimaryScreen.WorkingArea.Width - 2 * System.Windows.Forms.SystemInformation.Border3DSize.Width;
                else
                    RectWidth = Width;

                // Does the image fit in Height?
                if ((Height + System.Windows.Forms.SystemInformation.Border3DSize.Height + System.Windows.Forms.SystemInformation.CaptionHeight) > System.Windows.Forms.Screen.PrimaryScreen.WorkingArea.Height)
                    RectHeight = System.Windows.Forms.Screen.PrimaryScreen.WorkingArea.Height - System.Windows.Forms.SystemInformation.Border3DSize.Height - System.Windows.Forms.SystemInformation.CaptionHeight;
                else
                    RectHeight = Height;

                frameRect = new Jai_FactoryWrapper.RECT(0, 0, RectWidth, RectHeight);

                // Open the replay view
                error = Jai_FactoryWrapper.J_Image_OpenViewWindowEx(Jai_FactoryWrapper.EIVWWindowType.OverlappedStretch, "Replay", ref frameRect, ref maxSize, IntPtr.Zero, out WindowHandle);

                if (WindowHandle != IntPtr.Zero)
                {
                    List<Jai_FactoryWrapper.ImageInfo> imageList = myCamera.GetAsyncRecordedImages();
                    if (imageList != null && (imageList.Count > 0))
                    {
                        for (int index = 0; index < myCamera.TotalAsyncImagesRecordedCount; index++)
                        {
                            Jai_FactoryWrapper.ImageInfo ii = imageList[index];
                            Jai_FactoryWrapper.J_Image_SetViewWindowTitle(WindowHandle, "Replay (" + index.ToString() + "/" + myCamera.TotalAsyncImagesRecordedCount.ToString() + ")");
                            Jai_FactoryWrapper.J_Image_ShowImage(WindowHandle, ref ii, 4096, 4096, 4096);
                            Application.DoEvents();
                            Thread.Sleep(10);
                        }
                    }

                    Jai_FactoryWrapper.J_Image_CloseViewWindow(WindowHandle);
                }
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (myCamera != null)
            {
                startCaptureButton.Enabled = !myCamera.IsAsyncImageRecordingRunning && (myCamera.NumOfDataStreams > 0);
                stopCaptureButton.Enabled = myCamera.IsAsyncImageRecordingRunning && (myCamera.NumOfDataStreams > 0);
                replayButton.Enabled = !myCamera.IsAsyncImageRecordingRunning && (myCamera.TotalAsyncImagesRecordedCount > 0) && (myCamera.NumOfDataStreams > 0);
                saveButton.Enabled = !myCamera.IsAsyncImageRecordingRunning && (myCamera.TotalAsyncImagesRecordedCount > 0) && (myCamera.NumOfDataStreams > 0);

                if (!myCamera.IsAsyncImageRecordingRunning)
                {
                    recordingStatusLabel.Text = "Recording Stopped.";
                    progressBar1.Style = ProgressBarStyle.Blocks;
                    progressBar1.Minimum = 0;
                    progressBar1.Maximum = myCamera.AsyncImageRecordingCount;
                    progressBar1.Value = myCamera.TotalAsyncImagesRecordedCount;
                    progressBar1.Enabled = false;
                }
                else
                {
                    if (myCamera.GetAsyncImageRecordingMode == CCamera.AsyncImageRecordingMode.List)
                    {
                        recordingStatusLabel.Text = "Recorded " + myCamera.TotalAsyncImagesRecordedCount.ToString() + " images out of " + myCamera.AsyncImageRecordingCount.ToString();
                        progressBar1.Style = ProgressBarStyle.Blocks;
                        progressBar1.Minimum = 0;
                        progressBar1.Maximum = myCamera.AsyncImageRecordingCount;
                        progressBar1.Value = myCamera.TotalAsyncImagesRecordedCount;
                    }
                    else
                    {
                        if (myCamera.TotalAsyncImagesRecordedCount < myCamera.AsyncImageRecordingCount)
                        {
                            recordingStatusLabel.Text = "Recorded " + myCamera.TotalAsyncImagesRecordedCount.ToString() + " images out of " + myCamera.AsyncImageRecordingCount.ToString();
                            progressBar1.Style = ProgressBarStyle.Blocks;
                            progressBar1.Minimum = 0;
                            progressBar1.Maximum = myCamera.AsyncImageRecordingCount;
                            progressBar1.Value = myCamera.TotalAsyncImagesRecordedCount;
                        }
                        else
                        {
                            recordingStatusLabel.Text = "Recording frames Cyclically " + GetProgressChar();
                            progressBar1.Style = ProgressBarStyle.Marquee;
                        }
                    }
                }

                StartButton.Enabled = !myCamera.IsAcquisitionRunning && (myCamera.NumOfDataStreams > 0);
                StopButton.Enabled = myCamera.IsAcquisitionRunning && (myCamera.NumOfDataStreams > 0);
                SearchButton.Enabled = !myCamera.IsAcquisitionRunning && (myCamera.NumOfDataStreams > 0);
            }
            else
            {
                startCaptureButton.Enabled = false;
                stopCaptureButton.Enabled = false;
                replayButton.Enabled = false;
                saveButton.Enabled = false;
                SearchButton.Enabled = true;
            }
        }

        private string GetProgressChar()
        {
            _progressCharIndex++;

            if (_progressCharIndex > 3)
                _progressCharIndex = 0;

            switch (_progressCharIndex)
            {
                case 0:
                    return "/";
                case 1:
                    return "--";
                case 2:
                    return "\\";
                case 3:
                    return "|";
            }

            return "";
        }

        private void saveButton_Click(object sender, EventArgs e)
        {
            // Have we got any images to save to disk?
            if (myCamera != null && !myCamera.IsAsyncImageRecordingRunning && (myCamera.TotalAsyncImagesRecordedCount > 0))
            {
                // Prompt the user if he wants to continue or not with the image save
                if (MessageBox.Show(this, "Image save might take long time!\nAre you sure you want to continue?", "Image Save", MessageBoxButtons.OKCancel, MessageBoxIcon.Question, MessageBoxDefaultButton.Button1) == DialogResult.OK)
                {
                    // Disable the Image Recording buttons as long as we are saving the images
                    asynchImageRecordingGroupBox.Enabled = false;

                    // Get the recorded images as a list
                    List<Jai_FactoryWrapper.ImageInfo> imageList = myCamera.GetAsyncRecordedImages();

                    // Any images recorded?
                    if (imageList != null && (imageList.Count > 0))
                    {
                        // Run through the list of recorded images
                        for (int index = 0; index < myCamera.TotalAsyncImagesRecordedCount; index++)
                        {
                            Jai_FactoryWrapper.EFactoryError error = Jai_FactoryWrapper.EFactoryError.Success;

                            // Get the recorded image at this index
                            Jai_FactoryWrapper.ImageInfo ii = imageList[index];

                            // Are we saving the images in "raw" format or in Tiff?
                            if (saveRawCheckBox.Checked)
                            {
                                // Save the image to disk
                                error = Jai_FactoryWrapper.J_Image_SaveFileRaw(ref ii, ".\\RecordedImage" + index.ToString("000") + ".raw");
                            }
                            else
                            {
                                // Create local image that will contain the converted image
                                Jai_FactoryWrapper.ImageInfo localImageInfo = new Jai_FactoryWrapper.ImageInfo();

                                // Allocate buffer that will contain the converted image
                                // In this sample we re-allocate the buffer over-and-over because we assume that the recorded images could be
                                // of different size (If we have been using the Sequence functionality in the cameras)
                                error = Jai_FactoryWrapper.J_Image_Malloc(ref ii, ref localImageInfo);

                                // Convert the raw image to image format
                                error = Jai_FactoryWrapper.J_Image_FromRawToImage(ref ii, ref localImageInfo, 4096, 4096, 4096);

                                // Save the image to disk
                                error = Jai_FactoryWrapper.J_Image_SaveFile(ref localImageInfo, ".\\RecordedImage" + index.ToString("000") + ".tif");

                                //Free the conversion buffer
                                error = Jai_FactoryWrapper.J_Image_Free(ref localImageInfo);
                            }
                            Application.DoEvents();
                        }

                        MessageBox.Show(this, "The recorded images has been saved!", "Image save", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    }

                    // Re-enable the Image Recording buttons
                    asynchImageRecordingGroupBox.Enabled = true;
                }
            }
        }

        private void SetFramegrabberValue(String nodeName, Int64 int64Val)
        {
            if (null == myCamera)
            {
                return;
            }

            IntPtr hDevice = IntPtr.Zero;
            Jai_FactoryWrapper.EFactoryError error = Jai_FactoryWrapper.J_Camera_GetLocalDeviceHandle(myCamera.CameraHandle, ref hDevice);
            if (Jai_FactoryWrapper.EFactoryError.Success != error)
            {
                return;
            }

            if (IntPtr.Zero == hDevice)
            {
                return;
            }

            IntPtr hNode;
            error = Jai_FactoryWrapper.J_Camera_GetNodeByName(hDevice, nodeName, out hNode);
            if (Jai_FactoryWrapper.EFactoryError.Success != error)
            {
                return;
            }

            if (IntPtr.Zero == hNode)
            {
                return;
            }

            error = Jai_FactoryWrapper.J_Node_SetValueInt64(hNode, false, int64Val);
            if (Jai_FactoryWrapper.EFactoryError.Success != error)
            {
                return;
            }

            //Special handling for Active Silicon CXP boards, which also has nodes prefixed
            //with "Incoming":
            if ("Width" == nodeName || "Height" == nodeName)
            {
                string strIncoming = "Incoming" + nodeName;
                IntPtr hNodeIncoming;
                error = Jai_FactoryWrapper.J_Camera_GetNodeByName(hDevice, strIncoming, out hNodeIncoming);
                if (Jai_FactoryWrapper.EFactoryError.Success != error)
                {
                    return;
                }

                if (IntPtr.Zero == hNodeIncoming)
                {
                    return;
                }

                error = Jai_FactoryWrapper.J_Node_SetValueInt64(hNodeIncoming, false, int64Val);
            }
        }

        private void SetFramegrabberPixelFormat()
        {
            String nodeName = "PixelFormat";

            if (null == myCamera)
            {
                return;
            }

            IntPtr hDevice = IntPtr.Zero;
            Jai_FactoryWrapper.EFactoryError error = Jai_FactoryWrapper.J_Camera_GetLocalDeviceHandle(myCamera.CameraHandle, ref hDevice);
            if (Jai_FactoryWrapper.EFactoryError.Success != error)
            {
                return;
            }

            if (IntPtr.Zero == hDevice)
            {
                return;
            }

            long pf = 0;
            error = Jai_FactoryWrapper.J_Camera_GetValueInt64(myCamera.CameraHandle, nodeName, ref pf);
            if (Jai_FactoryWrapper.EFactoryError.Success != error)
            {
                return;
            }
            UInt64 pixelFormat = (UInt64)pf;

            UInt64 jaiPixelFormat = 0;
            error = Jai_FactoryWrapper.J_Image_Get_PixelFormat(myCamera.CameraHandle, pixelFormat, ref jaiPixelFormat);
            if (Jai_FactoryWrapper.EFactoryError.Success != error)
            {
                return;
            }

            StringBuilder sbJaiPixelFormatName = new StringBuilder(512);
            uint iSize = (uint)sbJaiPixelFormatName.Capacity;
            error = Jai_FactoryWrapper.J_Image_Get_PixelFormatName(myCamera.CameraHandle, jaiPixelFormat, sbJaiPixelFormatName, iSize);
            if (Jai_FactoryWrapper.EFactoryError.Success != error)
            {
                return;
            }

            IntPtr hNode;
            error = Jai_FactoryWrapper.J_Camera_GetNodeByName(hDevice, nodeName, out hNode);
            if (Jai_FactoryWrapper.EFactoryError.Success != error)
            {
                return;
            }

            if (IntPtr.Zero == hNode)
            {
                return;
            }

            error = Jai_FactoryWrapper.J_Node_SetValueString(hNode, false, sbJaiPixelFormatName.ToString());
            if (Jai_FactoryWrapper.EFactoryError.Success != error)
            {
                return;
            }

            //Special handling for Active Silicon CXP boards, which also has nodes prefixed
            //with "Incoming":
            string strIncoming = "Incoming" + nodeName;
            IntPtr hNodeIncoming;
            error = Jai_FactoryWrapper.J_Camera_GetNodeByName(hDevice, strIncoming, out hNodeIncoming);
            if (Jai_FactoryWrapper.EFactoryError.Success != error)
            {
                return;
            }

            if (IntPtr.Zero == hNodeIncoming)
            {
                return;
            }

            error = Jai_FactoryWrapper.J_Node_SetValueString(hNodeIncoming, false, sbJaiPixelFormatName.ToString());
        }
    }
}