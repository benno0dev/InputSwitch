
# InputSwitch

A System Tray Icon for Windows to change your Display Input
Already Supported Inputs: HDMI 1; HDMI 2; Display Port


## Preview

![Preview](https://raw.githubusercontent.com/benno0dev/InputSwitch/refs/heads/main/preview_inputswitch.gif)

## Requirements
- Monitor with DDC/ci enabled (Usally activatable from OSD menu; See your Manufacturers Support page)

## Installation
Download the newest .exe from the releases and execute [WARNING: Monitor is as of right now ONLY changable by executing from Source; The Default Monitor is always taken instead]

## Running from Source (.py)
### Requirements
- Python (obviously)
- Pystray
- Pillow
- Monitorcontrol

```bash
  pip install pystray pillow monitorcontrol
```
### Run
- Download the Sourcecode
- Execute main.py

## Config (only when running by source)
### Change Monitor
Just change the variable "Monitor" to a different number (0 should be your main monitor)
### Add/Change an Input
First add a MenuItem() Line to the "menu = Menu(...)" class, by copying an existing one and changing the names
Second copy an existing function of an input and also here change the names of your desired source:
- HDMI1, HDMI2, DP1, DP2 (For USB Type-C and different inputs, look here: https://github.com/newAM/monitorcontrol/issues/93)
