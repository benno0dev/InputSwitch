
# InputSwitch

A System Tray Icon for Windows to change your Display Input \
Already Supported Inputs: HDMI 1; HDMI 2; Display Port


## 👀 Preview

![Preview](https://raw.githubusercontent.com/benno0dev/InputSwitch/refs/heads/main/preview_inputswitch.gif)

## 🛠️ Roadmap
- Switch Monitor in the Menu
- Better way to add Inputs

## 📄 Requirements
- Monitor with DDC/ci enabled (Usally activatable from OSD menu; See your Manufacturers Support page)

## 📥 Installation
Download the newest .exe from the releases and execute [WARNING: Monitor is as of right now ONLY changable by executing from Source; The Default (Main) Monitor is always taken instead] \
ANTI-VIRUS WARNING: Some Anti-Viruses may detect the .exe as a virus, because it uses the ports of your monitor and i dont have a software license, which are very expensive (+300€ or something) \
if it is too unsafe/not trustworthy for you, you can always check the sourcecode and run it by source or compile it to an exe with [auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/)

## 👾 Running from Source (.py)
### Extra Information
It is recommended to run all this in a venv (If you dont know how, use the [vscode extension](https://marketplace.visualstudio.com/items/?itemName=ms-python.vscode-python-envs) or look it up [in the docs](https://docs.python.org/3/library/venv.html) for example)
### Requirements
- Python (obviously)
- git (optional)
- Pystray
- Pillow
- Monitorcontrol

```bash
  pip install pystray pillow monitorcontrol
```
### Run
- Download the Sourcecode and icon by using the following command or just download it from github
```bash
  git clone https://github.com/benno0dev/InputSwitch.git
```
- Enter the venv (automatically done by vscode, else look it up in the docs)
- Execute main.py

## ⚙️ Config (only when running by source)
### Change Monitor
Just change the variable "Monitor" to a different number (0 should be your main monitor)
### Automatically use specific venv when executing the script
- Add line like this at the start of the main.py file (when you dont want a console popping up (windows only))
```python
  #![link to your venv]\Scripts\pythonw.exe
```
- with console
```python
  #![link to your venv]\Scripts\python.exe
```
- it should look like this (".venv" is my venv name and the rest is the path to the folder with the files in it)
```python
  #!C:\Users\benni\Projects\Python\InputSwitch\.venv\Scripts\pythonw.exe
```
### Add/Change an Input
First add a MenuItem() Line to the "menu = Menu(...)" class, by copying an existing one and changing the names
Second copy an existing function of an input and also here change the names of your desired source:
- HDMI1, HDMI2, DP1, DP2 (For USB Type-C and different inputs, look here: https://github.com/newAM/monitorcontrol/issues/93)
