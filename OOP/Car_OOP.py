class Window:

    def __init__(self, tint = "", thickness = "", material = "", handle = ""): #all init statements and super init statements that we add must follow this same order in order to work correctly
        self.tint = self.set_tint(tint) # The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
        self.thickness = self.set_thickness(thickness)
        self.material = self.set_material(material)
        self.handle = self.set_handle(handle)

    def set_tint(self, tint):
        tint_lvl = ["none", "medium", "heavy"] #must first list - mk sure list name dif to variable
        if tint.lower() in tint_lvl: #ref list
            self.tint = tint.lower()
            # print(f"Window tint is now {self.tint}") - added to mk sure everything was working but hashed this out bc too much text
            return self.tint
        if tint == '': # Need this other if statement so that it doesn't print everything we asked it to in the else when nothing has been filled in for the variable
            return
        else:
            return print("You have selected a tint level that is not available.\nPlease choose a tint level from the following:\nnone, medium, heavy")

    def set_thickness(self, thickness):
        window_thickness = ["standard", "durable"]
        if thickness.lower() in window_thickness:
            self.thickness = thickness.lower()
            # print(f"Window thickness is now {self.thickness}")
            return self.thickness
        if thickness == '':
            return
        else:
            return print("You have selected a window thickness that is not available.\nPlease choose a window thickness from the following:\nstandard, durable")

    def set_handle(self, handle):
        handle_material = ["plastic", "metal"]
        if handle.lower() in handle_material:
            self.handle = handle.lower()
            # print(f"Window handle material is now {self.handle}")
            return self.handle
        if handle == '':
            return
        else:
            return print("You have selected a handle material that is not available.\nPlease choose a handle material from the following:\nplastic, metal")

    def set_material(self, material):
        window_material = ["plastic", "glass"]
        if material.lower() in window_material:
            self.material = material.lower()
            # print(f"Window material is now {self.material}")
            return self.material
        if material == '':
            return
        else:
            return print("You have selected a window material that is not available.\nPlease choose a window material from the following:\nplastic, glass")


class Door(Window):

    def __init__(self, colour = "",  open_style = "", lock_type = "", tint = "", thickness = "", material = "", handle = ""):
        super().__init__(tint, thickness, material, handle)
        self.colour = self.set_colour(colour)
        self.open_style = self.set_open_style(open_style)
        self.lock_type = self.set_lock_type(lock_type)

    def open(self):
        return print("Door is open")

    def shut(self):
        return print("Door is shut")

    def lock_door(self):
        return print("Door is locked")

    def wind_window_down(self):
        return print("Winding window down")

    def set_colour(self, colour):
        colours = ["red", "silver", "black"]
        if colour.lower() in colours:
            self.colour = colour.lower()
            # print(f"Car colour is now {self.colour}")
            return self.colour
        if colour == '':
            return
        else:
            return print("You have selected a colour that is not available.\nPlease choose a colour from the following:\nred, silver, black")

    def set_open_style(self, style):
        styles = ["standard", "vertical"]
        if style.lower() in styles:
            self.style = style.lower()
            # print(f"Window style is {self.style}")
            return self.style
        if style == '':
            return
        else:
            return print("You have selected a style that is not available.\nPlease choose a style from the following:\nstandard, vertical")

    def set_lock_type(self, lock_type):
        lock_types = ["remote", "manual"]
        if lock_type.lower() in lock_types:
            self.lock_type = lock_type.lower()
            # print(f"Lock type is {self.lock_type}")
            return self.lock_type
        if lock_type == '':
            return
        else:
            return print("You have selected a lock type that is not available.\nPlease choose a lock type from the following:\nremote, manual")

class Car(Door):

    def __init__(self, make = "", style = "", doors = "" , colour = "",  open_style = "", lock_type = "", tint = "", thickness = "", material = "", handle = ""):
        super().__init__(colour, open_style, lock_type, tint, thickness, material, handle)
        self.style = self.set_style(style)
        self.doors = self.set_doors(doors)
        self.make = self.set_make(make)

    def accelerate(self):
        return print("You are accelerating")

    def brake(self):
        return print("You are slowing down or coming to a stop")

    def steer(self):
        return print("You are turning")

    def park(self):
        return print("Car is parking")

    def set_style(self, style):
        styles = ["hatchback", "cruiser", "sport"]
        if style.lower() in styles:
            self.style = style.lower()
            # print(f"Car style is {self.style}")
            return self.style
        if style == '':
            return
        else:
            return print("You have selected a style that is not available.\nPlease choose a style from the following:\nhatchback, cruiser, sport")

    def set_doors(self, doors):
        door_num = ["3 door", "5 door"]
        if doors.lower() in door_num:
            self.doors = doors.lower()
            # print(f"Door number is {self.doors}")
            return self.doors
        if doors == '':
            return
        else:
            return print("You have selected a number of doors that is not available.\nPlease choose a number of doors from the following:\n3 door, 5 door")

    def set_make(self, make):
        car_make = ["Honda", "Toyota", "Porsche"]
        if make.title() in car_make:
            self.make = make.lower()
            # print(f"Car make is {self.make}")
            return self.make
        if make == '':
            return
        else:
            return print("You have selected a make that is not available.\nPlease choose a make from the following:\nHonda, Toyota, Porsche")

    def get_car_details(self):
        print('Car Make: ' + str(self.make)) #str is casting as a string
        print('Style: ' + str(self.style)) # we add these lines so that when we run it, it looks neater and is easier look at/follow
        print('Doors: ' + str(self.doors))
        print('Colour: ' + str(self.colour))
        print('Open style: ' + str(self.open_style))
        print('Lock type: ' + str(self.lock_type))
        print('Handle material: ' + str(self.handle))
        print('Tint level: ' + str(self.tint))
        print('Window thickness: ' + str(self.thickness))
        print('Window material: ' + str(self.material))


car1 = Car("porsche", "hatchback", "3 door", "red")
car1.get_car_details()
car1.open()