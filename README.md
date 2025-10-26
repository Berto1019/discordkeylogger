Install dependencies

Ensure python is installed and keyboard module:
winget install Python.Python.3
pip install Keyboard

Edit webhook URL to webhook

Run in background:
pythonw.exe your_script_name.py

In order to kill:
taskkill /IM pythonw.exe /F
taskkill /PID [PID_NUMBER] /F
