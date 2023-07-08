import tkinter as tk
from tkinter import *

def convert(x):
    # If the user has selected to convert from Imperial to Metric, execute this
    if conversionSelection.get() == 1:
        # If the conversion is any of these, you can divide by whatever the conversion rate is
        if selection.get() == "ft -> m" or selection.get() == "lb -> kg" or selection.get() == "yd -> m":
            # Divide by the conversion rate listed in 'measurements' to convert it
            x /= measurements[selection.get()]
            return round(x, 2)
        # If it isn't, you can divide by the conversion rate for the rest
        else:
            # Multiply by the conversion rate listed in 'measurements' to convert it
            x *= measurements[selection.get()]
            return round(x, 2)
    # If the user has selected to convert from Metric to Imperial, executre this
    else:
        # If the conversion is any of these, you can multiply by whatever the conversion rate is
        if selection.get() == "m -> ft" or selection.get() == "kg -> lb" or selection.get() == "m -> yd":
            x *= measurements[selection.get()]
            return round(x, 2)
        # If it isn't, you can divide by the conversion rate for the rest
        else:
            x /= measurements[selection.get()]
            return round(x, 2)


def updateResult():
    # Displays the result of the conversion, as well as adds the appropriate unit

    # Imperial -> Metric
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
    # Metric -> Imperial
    elif selection.get() == "m -> ft":
        result.config(text=f"{convert(float(entry.get()))}ft")
    elif selection.get() == "kg -> lb":
        result.config(text=f"{convert(float(entry.get()))}lb")
    elif selection.get() == "m -> yd":
        result.config(text=f"{convert(float(entry.get()))}yd")
    elif selection.get() == "g -> oz":
        result.config(text=f"{convert(float(entry.get()))}oz")
    elif selection.get() == "cm -> in":
        result.config(text=f"{convert(float(entry.get()))}in")
    elif selection.get() == "km -> mi":
        result.config(text=f"{convert(float(entry.get()))}mi")

def conversionTypeUpdate():
    # Reset 'selection' and delete all old options
    selection.set("")
    dropdownMenu['menu'].delete(0, 'end')

    # Insert list of new options (tk._setit hooks them up to 'selection')
    if conversionSelection.get() == 1:
        new_choices = ("ft -> m", "in -> cm", "lb -> kg", "oz -> g", "yd -> m", "mi -> km")
    else:
        new_choices = ("m -> ft", "cm -> in", "kg -> lb", "g -> oz", "m -> yd", "km -> mi")
    for choice in new_choices:
        dropdownMenu['menu'].add_command(label=choice, command=tk._setit(selection, choice))

measurements = {
    # Imperial -> Metric
    "ft -> m": 3.281, # divide by to get meters
    "lb -> kg": 2.205, # divide by to get kilograms
    "yd -> m": 1.094, # divide by to get meters
    "oz -> g": 28.35, # multiply by to get grams
    "in -> cm": 2.54, # multiply by to get centimetres
    "mi -> km": 1.609, # multiply by to get kilometres
    # Metric -> Imperial
    "m -> ft": 3.281, # multiply by to get feet
    "kg -> lb": 2.205, # multiply by to get pounds
    "m -> yd": 1.094, # mulitply by to get yards
    "g -> oz": 28.35, # divide by to get ounces
    "cm -> in": 2.54, # divide by to get inches
    "km -> mi": 1.609, # multiply by to get miles
}

choices = ("", "")

# Initialises the window
master = tk.Tk(className="Imperial and Metric Unit Converter")

# Initialises the entry field to input the measurement value
entry = Entry(master)

# Initialises the radio buttons to choose whether to convert from imperial to metric, or from metric to imperial
conversionSelection = IntVar(master)
rButton1 = Radiobutton(master, text="Imperial -> Metric", variable=conversionSelection, value=1, command=conversionTypeUpdate)
rButton2 = Radiobutton(master, text="Metric -> Imperial", variable=conversionSelection, value=2, command=conversionTypeUpdate)

# Initialises the drop-down menu to select the measurements
selection = StringVar(master)
selection.set("Please select an option above")
dropdownMenu = OptionMenu(master, selection, *choices)

# Initialises the 'Convert' button
button = Button(master, text="Convert", command=updateResult)

# Initalises the text that will display the conversion result
result = Label(master, text="")

# Displays the GUI elements
entry.pack()
rButton1.pack()
rButton2.pack()
dropdownMenu.pack()
button.pack()
result.pack()

master.mainloop()