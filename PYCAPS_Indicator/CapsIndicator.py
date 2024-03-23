import pystray
from PIL import Image
import keyboard

# Set up system tray icon
caps_off = pystray.Icon("off", Image.open("caps_lock_off.png"), "Caps Lock is off")
caps_on = pystray.Icon("on", Image.open("caps_lock_on.png"), "Caps Lock is on")

def update_caps_lock_icon():
    caps_lock_on = not keyboard.is_pressed('caps lock')
    try:
        while True:
            caps_lock_on = not caps_lock_on
            print("CapsLock: ", caps_lock_on)

            if caps_lock_on:
                caps_off.visible = False
                caps_on.visible = True
            else:
                caps_on.visible = False
                caps_off.visible = True

            keyboard.wait('caps lock')
    except KeyboardInterrupt:
        pass

def main():
    print("Hello")
    update_caps_lock_icon()        

if __name__ == "__main__":
    main()
