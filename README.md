--------------Contributers---------------
Name Natnael wondimieneh
Github Captn-levi
Email Natnaelwon@gmail.com
Based on yolo object detection

-----------Install Prerequisites----------

1.Install Python 3.11+

    Download: https://www.python.org/downloads/

    During installation: check “Add Python to PATH”

2.Install Visual Studio Code (optional, for editing)

    Download: https://code.visualstudio.com/

--------------Demonstration-------------
1. Clone or Download the Project or unzip the project folder
 git clone https://github.com/captn-levi/Adaptive-Traffic-Signal-System.git


2. Create & Activate Virtual Environment

open vs terminal/powershell:
while in the folder (Adaptive-Traffic-signal-system)

python -m venv venv
# Activate venv
.\venv\Scripts\Activate.ps1   # or
.\venv\Scripts\activate.bat


If PowerShell blocks script execution, run as admin and execute:

Set-ExecutionPolicy RemoteSigned

3. Install Dependencies
    pip install --upgrade pip
    pip install -r requirements.txt

4.Run the Flask Server

Make sure your virtual environment is activated, then:

     cd backend
    python app.py


You should see something like:

 * Running on http://127.0.0.1:5000
 * Debugger is active!


5. Open in Browser

Open a browser and go to:

    http://127.0.0.1:5000


You should see the UI with map, sidebar, and controls.


6. Using the System

    Click any junction on the map.
    Latitude & Longitude auto-populate.

    Press “Detect Incoming Roads”

    Incoming roads appear in sidebar.

    Upload images for each road.

    Make sure each road has one image.

    Press “Analyze Traffic”

    Vehicle counts and green times appear in the sidebar.

7, Stopping the Server

    Press CTRL + C in the terminal.



--------------Contributers---------------
Name Natnael wondimieneh
Github Captn-levi
Email Natnaelwon@gmail.com
Based on yolo object detection