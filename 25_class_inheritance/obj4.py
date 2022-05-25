## Device is the parent class and printer is one of the device
## But printer has specific functionality that other device dont have
## so we create another class Printer that uses some characterstics of Device parent class

class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True
    

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"  ## !r calls the __repr__ method of the name 
    
    def disconnect(self):
        self.connected = False
        print("Disconnected.")
    
## new class Printer inherits from Device
class Printer (Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)  ## this super().className(method) calls the methods of parent class
        self.capacity = capacity
        self.remaining_pages = capacity
    
    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"
    
    def print(self, pages):
        if not self.connected:
            print("your printer is not connected!")
            return      ## this exits the function if not connected
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages

## creating object of Printer class
printer = Printer("Printer", "USB", 500)
printer.print(20)

print(printer)

# Output
#Printing 20 pages.
#Device 'Printer' (USB) (480 pages remaining)

printer.disconnect()   ## this method is not defined in Printer() but it calls from Device() class
printer.print(30)

#Output
#Disconnected.
#your printer is not connected!

