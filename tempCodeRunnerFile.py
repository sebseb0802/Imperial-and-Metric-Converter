    if variable.get() == "Feet" or variable.get() == "Pounds" or variable.get() == "Yards":
                result = entry * measurements[variable.get()][v]
            else:
                result = entry / measurements[variable.get()][v]
            return result