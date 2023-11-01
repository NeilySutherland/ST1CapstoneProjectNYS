#Week 11 Challenge problem pt. 1

class Phone:
    def __init__(self, manufacturer, model, retail_price):
        self.__manufact = manufacturer
        self.__model = model
        self.__retail_price = retail_price

    #Mutators
    def set_manufact(self, manufacturer):
        self.__manufact = manufacturer

    def set_model(self, model):
        self.__model = model

    def set_retail_price(self, retail_price):
        self.__retail_price = retail_price

    #Accessors
    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price

#GUI
import tkinter

class PhoneGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Phone Inventory")
        self.main_window.geometry("400x300")
        self.main_window.configure(bg = 'light blue')

        self.frame1 = tkinter.Frame()
        self.frame2 = tkinter.Frame()
        self.frame3 = tkinter.Frame()
        self.frame4 = tkinter.Frame()
        self.frame5 = tkinter.Frame()

        self.label1 = tkinter.Label(self.frame1, text="Manufacturer:")
        self.entry1 = tkinter.Entry(self.frame1)
        self.label1.pack(side="left")
        self.entry1.pack(side="left")

        self.label2 = tkinter.Label(self.frame2, text="Model Number:")
        self.entry2 = tkinter.Entry(self.frame2)
        self.label2.pack(side="left")
        self.entry2.pack(side="left")

        self.label3 = tkinter.Label(self.frame3, text="Retail Price:")
        self.entry3 = tkinter.Entry(self.frame3)
        self.label3.pack(side="left")
        self.entry3.pack(side="left")

        self.submit_button = tkinter.Button(self.frame4, text="Submit", command=self.submit)
        self.submit_button.pack()

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()

        self.main_window.mainloop()

    def submit(self):
        manufacturer = self.entry1.get()
        model = self.entry2.get()
        price = self.entry3.get()

        information = f"Here is the data that you entered:\n\nManufacturer: {manufacturer}\nModel Number: {model}\nRetail Price: ${price}"

        output_label = tkinter.Label(self.frame5, text=information, bg = "light blue")
        output_label.pack(side="left")


my_gui = PhoneGUI()