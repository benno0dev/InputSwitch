from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw
import monitorcontrol as mc

def create_image(): # Draws the Icon
    width = 64
    height = 64
    image = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    draw.ellipse((16, 16, 48, 48), fill='green')

    return image

Monitor = 0 # Change the Int to change the disired monitor (0 is probably always the main monitor)

def on_hdmi1():
    monitors = mc.get_monitors()
    with monitors[Monitor]:
        monitors[Monitor].set_input_source("HDMI1")
        print("Monitor set to HDMI 1")

def on_hdmi2():
    monitors = mc.get_monitors()
    with monitors[Monitor]:
        monitors[Monitor].set_input_source("HDMI2")
        print("Monitor set to HDMI 2")

def on_dp():
    monitors = mc.get_monitors()
    with monitors[Monitor]:
        monitors[Monitor].set_input_source("DP1")
        print("Monitor set to DisplayPort")
        

def on_quit(icon, item):
    icon.stop()

# Define the menu
menu = Menu(
    MenuItem('HDMI 1', lambda: on_hdmi1()),
    MenuItem('HDMI 2', lambda: on_hdmi2()),
    MenuItem('DisplayPort', lambda: on_dp()),
    MenuItem('Quit', on_quit)
)

icon = Icon("InputSwitch", create_image(), "InputSwitch Tray Icon", menu)

icon.run()
