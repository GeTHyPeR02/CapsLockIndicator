import threading
import pystray
from PIL import Image
import keyboard

# Set up system tray icons
caps_off = pystray.Icon("off", Image.open("caps_lock_off.png"), "Caps Lock is off")
caps_on = pystray.Icon("on", Image.open("caps_lock_on.png"), "Caps Lock is on")

# Blocking functions for running icons
def check_caps_lock_off():
    caps_off.run()

def check_caps_lock_on():
    caps_on.run()

# Threads for blocking functions
def icon_threads():
    running_functions = [check_caps_lock_on, check_caps_lock_off]
    running_threads = []

    for func in running_functions:
        thread = threading.Thread(target=func)
        thread.daemon = True
        running_threads.append(thread)
                    
    for thread in running_threads:
        thread.start()       

# Shows icon depending on caps lock state
def update_caps_lock_icon():
    caps_lock_on = not keyboard.is_pressed('caps lock')
    
    try:
        icon_threads()

        while True:
            caps_lock_on = not caps_lock_on

            if caps_lock_on:
                caps_off.visible = False
                caps_on.visible = True
            else:
                caps_on.visible = False
                caps_off.visible = True

            keyboard.wait('caps lock')

    except KeyboardInterrupt:
        caps_off.stop()
        caps_on.stop()
        pass

def main():
    update_caps_lock_icon()       

if __name__ == "__main__":
    main()
