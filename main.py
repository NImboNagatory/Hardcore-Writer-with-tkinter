from func import Hard_core_writer
from tkinter import Tk


gui = Tk()

gui.config(bg="#f8f9fa")

gui.grid_rowconfigure(0, weight=1)

gui.grid_columnconfigure(0, weight=1)

gui.geometry("800x600")

gui.resizable(False, False)

gui.title("Hardcore Writer")

screen = Hard_core_writer(gui)

screen.grid(row=0, column=0)

screen.grid_rowconfigure(1, weight=1)

screen.grid_columnconfigure(1, weight=1)

loop_on = True

while loop_on:
    gui.update_idletasks()
    gui.update()
