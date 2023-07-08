import tkinter as tk
from tkinter import *

def convert(x):
    if selection.get() != "Please select a measurement":
        if selection.get() == "ft -> m" or selection.get() == "lb -> kg" or selection.get() == "yd -> m":
            x /= measurements[selection.get()]
            return round(x, 2)
        else:
            x *= measurements[selection.get()]
            return round(x, 2)

def updateResult():
    if selection.get() == "ft -> m":
        result.config(text=f"{convert(float(entry.get()))}m")
    elif selection.get() == "lb -> kg":
        result.config(text=f"{convert(float(entry.get()))}kg")
    elif selection.get() == "yd -> m":
        result.config(text=f"{convert(float(entry.get()))}m")
    elif selection.get() == "oz -> g":
        result.config(text=f"{convert(float(entry.get()))}g")
    elif selection.get() == "in -> cm":
        result.config(text=f"{convert(float(entry.get()))}cm")
    elif selection.get() == "mi -> km":
        result.config(text=f"{convert(float(entry.get()))}km")

measurements = {
    "ft -> m": 3.281, # divide by to get meters
    "lb -> kg": 2.205, # divide by to get kilograms
    "yd -> m": 1.094, # divide by to get meters
    "oz -> g": 28.35, # multiply by to get grams
    "in -> cm": 2.54, # multiply by to get centimetres
    "mi -> km": 1.609 # multiply by to get kilometres
}

# Initialises the window
master = tk.Tk(className="Converter")

# Initialises the entry field to input the measurement value
entry = Entry(master)
#entry.insert(END, 0)

# Sets up the drop-down menu to select the measurements
selection = StringVar(master)
selection.set("Imperial -> Metric")
dropdownMenu = OptionMenu(master, selection, "ft -> m", "in -> cm", "lb -> kg", "oz -> g", "yd -> m", "mi -> km")

# Initialises the 'Convert' button
button = Button(master, text="Convert", command=updateResult)

# Initalises the text that will display the conversion result
result = Label(master, text="")

# Displays the GUI elements
entry.pack()
dropdownMenu.pack()
button.pack()
result.pack()

master.mainloop()