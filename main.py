import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from tkinter import Message
import sv_ttk
# Loop up tables
tbl1 = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]
tbl2 = [[1, 2, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7, 8, 9]]
tbl3 = [[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]

class Window(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.eset = {'ipady':3}
        self.lset = {}


        # Validate ATRQ Input
        ATRQval = (self.register(self.validateATRQ), '%P')
        ATRQinval = (self.register(self.invalidATRQ),)

        self.ATLabel = ttk.Label(self,font = "Roboto 12 bold", text="ATRQ").grid(self.lset,row=1,column=0,padx=5)

        self.ATEntry = ttk.Entry(self,validate="focusout", validatecommand=ATRQval, invalidcommand=ATRQinval)
        self.ATEntry.grid(self.eset,row=1, column=1)

        # Validate KE Input
        KEval = (self.register(self.validateKE), '%P')
        KEinval = (self.register(self.invalidKE),)

        self.KELabel = ttk.Label(self,font = "Roboto 12 bold", text="K&E").grid(self.lset,row=2,column=0,padx=5)
        self.KEEntry = ttk.Entry(self,validate="focusout", validatecommand=KEval, invalidcommand=KEinval)
        self.KEEntry.grid(self.eset,row=2, column=1)

        # Validate TIME Input
        TIMEval = (self.register(self.validateTIME), '%P')
        TIMEinval = (self.register(self.invalidTIME),)

        self.TIMELabel = ttk.Label(self,font = "Roboto 12 bold", text="TIME").grid(self.lset,row=3,column=0,padx=5)
        self.TIMEEntry = ttk.Entry(self,validate="focusout", validatecommand=TIMEval, invalidcommand=TIMEinval)
        self.TIMEEntry.grid(self.eset,row=3, column=1)



        self.CFLLabel = ttk.Label(self,font = "Roboto 12 bold",text="CFL").grid(self.lset,row=4,column=0,padx=5)
        self.CFLDrop = ttk.Combobox(self, values=['None','Low','Medium','High'], width=17, state = "readonly")
        self.CFLDrop.grid(self.eset,row=4, column=1)

        self.Submit = ttk.Button(self,text="Submit", style="Accent.TButton", command=lambda: self.onSubmit()).grid(row=5,column=0,columnspan=2,sticky = tk.W+tk.E,pady=5)

        self.grid()


    def validateATRQ(self,value):

        try:
            value = int(value)
            if value >=1 and value <=5:
                return True
            else:
                return False
        except:
            return False

    def invalidATRQ(self):

        tk.messagebox.showerror(self, "Please enter a number between 1 and 5.")


    def validateKE(self,value):

        try:
            value = int(value)
            if value >=1:
                return True
            else:
                return False
        except:
            return False

    def invalidKE(self):

        tk.messagebox.showerror(self, "Please enter a number greater than 1")


    def validateTIME(self,value):

        try:
            value = int(value)
            if value >=3:
                return True
            else:
                return False
        except:
            return False

    def invalidTIME(self):

        tk.messagebox.showerror(self, "Please enter a number greater than 3")

    def validateCFL(self,value):
        print("no")
        try:
            value = value.upper()
            if value == "NONE":
                return 0
            elif value == "LOW":
                return 1
            elif value == "MEDIUM":
                return 2
            elif value == "HIGH":
                return 3
            else:
                return False
        except:
            return False

    def invalidCFL(self):

        tk.messagebox.showerror(self, "Please select either: None, Low, Medium or High")

    def normaliseKE(self,v):
            try:

                if 0 <= v <= 9:
                    return 0
                elif 10 <= v <= 15:
                    return 1
                elif v > 15:
                    return 2
                else:
                    return -1
            except:
                return -1


    def normaliseTIME(self,v):
            try:
                if 3 <= v <= 7:
                    return 0
                elif 8 <= v <= 15:
                    return 1
                elif v > 15:
                    return 2
                else:
                    return -1

            except:
                return -1



    def normaliseATRQ(self,v):
            try:
                if 1 <= v <= 5:
                    return v-1
                else:
                    return -1
            except:
                return -1

    def onSubmit(self):
        #       We are going to validate one more time incase the user ignores the invalid warnigns
        #       and just spams the submit button like a champ
        if self.validateATRQ(self.ATEntry.get()):
            # Its valid
            if self.validateKE(self.KEEntry.get()):
                # Its valid
                if self.validateTIME(self.TIMEEntry.get()):
                    #Its valid
                    if self.CFLDrop.get().upper() in ["NONE","LOW","MEDIUM","HIGH"]:
                        # Now that I know they are valid they can be cast to int
                        ATRQ = int(self.normaliseATRQ(self.ATEntry.get()))
                        KE = int(self.normaliseKE(self.KEEntry.get()))
                        TIME = int(self.normaliseTIME(self.TIMEEntry.get()))
                        CFL = int(self.validateCFL(self.CFLDrop.get()))
                        #Its valid
                        # Do Maths
                        # Define Storage Variables For Lookup Table Results

                        tbl1res = 0
                        tbl2res = 0
                        tbl3res = 0
                        tbl1res = tbl1[KE][ATRQ]
                        tbl2res = tbl2[TIME][tbl1res-1]
                        tbl3res = tbl3[CFL][tbl2res]
                        out = tbl3res


                        if out < 0:
                            print("Recommended Model: CASH ")
                        elif  0<=out<=2:
                            print("Recommended Model: Model 1")
                        elif  3<=out<=4:
                            print("Recommended Model: Model 2")
                        elif  5<=out<=6:
                            print("Recommended Model: Model 3")
                        elif  7<=out<=8:
                            print("Recommended Model: Model 4")
                        elif  9<=out<=11:
                            print("Recommended Model: Model 5")





class App(tk.Tk):
    def __init__(self):
        super().__init__()
        sv_ttk.set_theme("light")
        self.title("Model Calculator")
        self.geometry("210x200")
        self.resizable(False, False)


if __name__ == "__main__":
    run = App()
    Window(run)
    run.mainloop()


"""

import tkinter as tk
from time import sleep

def normaliseKE(v):
    while True:
        try:

            if 0 <= v <= 9:
                return 0
            elif 10 <= v <= 15:
                return 1
            elif v > 15:
                return 2
            else:
                print("Please enter a number greater than 0")
        except ValueError:
            print("Sorry! You need to enter a number!")


def normaliseTIME(v):
    while True:
        try:
            if 3 <= v <= 7:
                return 0
            elif 8 <= v <= 15:
                return 1
            elif v > 15:
                return 2
            else:
                print("Please enter a number greater than 3")
        except ValueError:
            print("Sorry! You need to enter a number!")


def normaliseATRQ(v):
    while True:
        try:
            if 1 <= v <= 5:
                return v-1
            else:
                print("Please enter a number between 1 and 5")
        except TypeError:
            return "nonum"


def normaliseCFL(v):
    v = v.upper()
    while True:
        try:
            if v == "NONE":
                return 0
            elif v == "LOW":
                return 1
            elif v == "MED":
                return 2
            elif v == "HIGH":
                return 3
            else:
                raise TypeError
        except TypeError:
            print("Please Enter: None, Low, Med or High")


# Define Lookup Tables

tbl1 = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]
tbl2 = [[1, 2, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7, 8, 9]]
tbl3 = [[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]






def processData():
        # Get input from user

        ATRQ = normaliseATRQ()

        KE = normaliseKE()
        TIME = normaliseTIME()
        CFL = normaliseCFL()

        # Define Storage Variables For Lookup Table Results

        tbl1res = 0
        tbl2res = 0
        tbl3res = 0
        tbl1res = tbl1[KE][ATRQ]
        tbl2res = tbl2[TIME][tbl1res-1]
        tbl3res = tbl3[CFL][tbl2res]
        out = tbl3res


        if out < 0:
            print("Recommended Model: CASH ")
        elif  0<=out<=2:
            print("Recommended Model: Model 1")
        elif  3<=out<=4:
            print("Recommended Model: Model 2")
        elif  5<=out<=6:
            print("Recommended Model: Model 3")
        elif  7<=out<=8:
            print("Recommended Model: Model 4")
        elif  9<=out<=11:
            print("Recommended Model: Model 5")



















"""