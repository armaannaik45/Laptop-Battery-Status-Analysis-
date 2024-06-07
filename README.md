# LaptopBatteryStatusAnalyzerPython
This project is a Python-based application that provides real-time monitoring of your laptop's battery status. It displays detailed information such as the current charge percentage, charging status, estimated time to full charge, and time left to discharge. The application also features a visual representation of the battery level.

**Features**
⦿ Real-time Battery Monitoring: Continuously updates the battery status and displays the charge percentage.
⦿ Charging Status: Indicates whether the laptop is charging or discharging.
⦿ Estimated Time Calculation: Provides estimated time to full charge when charging and time left to discharge when not charging.
⦿ Visual Representation: Displays a graphical representation of the battery level.
⦿ User-Friendly Interface: Built with Tkinter for a clean and simple GUI.

**Technologies Used**
**Python:** Core programming language.
**Tkinter:** For building the graphical user interface.
**psutil:** For accessing battery status and other system-related information.
**Pillow:** For image processing in the GUI.

**Getting Started**
To get a local copy up and running, follow these steps.

**Prerequisites**
⦿ Python 3.x
⦿ psutil library
⦿ Pillow library

**Installation**
1. Clone the repository:
**git clone https://github.com/your-username/laptop-battery-status-analyzer.git**

2. Install the required libraries:
**pip install psutil pillow**

3. Run the application:
**python battery_status_analyzer.py**

**Usage**
• Open the application.
• The main window will display the current battery status, charge percentage, and estimated time.
• Click the "Refresh" button to manually update the battery information.
• The battery visualization will update in real-time based on the current charge percentage.

**Code Overview**
The main Python script is structured as follows:
• Import Libraries: Import necessary libraries including tkinter, psutil, and PIL.
• Define Functions: Key functions to update battery information and refresh the GUI.
• Setup GUI: Create the main window, labels, canvas for battery visualization, and refresh button.
• Main Loop: Start the Tkinter main loop to run the application.

**Contributing**
Contributions are welcome! Please fork the repository and create a pull request with your changes.

**License**
Distributed under the MIT License. See LICENSE for more information.
