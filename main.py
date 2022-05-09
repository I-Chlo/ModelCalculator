import datetime
import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox
from tkinter import ttk
from tkinter import Message
from datetime import date
import sv_ttk
import os

# Loop up tables
tbl1 = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]
tbl2 = [[1, 2, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7, 8, 9]]
tbl3 = [[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]



class Window(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.eset = {'ipady':6}
        self.entrywidth = 20
        self.lset = {'padx': 8}
        self.modelResult = ""


        self.heading = ttk.Label(self, font = "Roboto 20 bold", text="Model Portfolio Calculator").grid(self.lset, row=0, column=0, columnspan=3, pady=10)


        # create client name input

        self.clientINL = ttk.Label(self, font = "roboto 14 bold", text="Client\nName").grid(self.lset, row=1, column=0, padx=5)
        self.clientINE = ttk.Entry(self, font = "roboto 15",width=self.entrywidth+2)
        self.clientINE.grid(self.eset,row=1, column=1)


        self.ATLabel = ttk.Label(self,font = "roboto 14 bold", text="ATRQ").grid(self.lset,row=2,column=0,padx=5)

        self.ATEntry = ttk.Combobox(
            self,
            values=["1","2","3","4","5"],
            width = self.entrywidth,
            state="readonly",
            font=("Roboto", 15)
        )
        self.ATEntry.grid(self.eset,row=2, column=1)



        self.KELabel = ttk.Label(self,font = "roboto 14 bold", text="K&E").grid(self.lset,row=3,column=0,padx=5)
        self.KEEntry = ttk.Combobox(
            self,
            values=["0-9","10-15","15+"],
            width = self.entrywidth,
            state="readonly",
            font=("Roboto", 15)
        )
        self.KEEntry.grid(self.eset,row=3, column=1)



        self.TIMELabel = ttk.Label(self,font = "roboto 14 bold", text="TIME").grid(self.lset,row=4,column=0,padx=5)
        self.TIMEEntry = ttk.Combobox(
            self,
            values=["3-7", "8-15", "15+"],
            width = self.entrywidth,
            state = "readonly",
            font=("Roboto", 15)
        )
        self.TIMEEntry.grid(self.eset,row=4, column=1)



        self.CFLLabel = ttk.Label(self,font = "roboto 14 bold",text="CFL").grid(self.lset,row=5,column=0,padx=5)
        self.CFLDrop = ttk.Combobox(
            self,
            values=['None','Low','Medium','High'],
            width = self.entrywidth,
            state = "readonly",
            font=("Roboto", 15)
        )
        self.CFLDrop.grid(self.eset,row=5, column=1)
        self.s = ttk.Style(self)
        self.s.configure('Accent.TButton',font=("Roboto", 13))
        self.Submit = ttk.Button(self,text="Submit", style="Accent.TButton",command=lambda: self.onSubmit()).grid(row=6,column=0,columnspan=2,sticky ="nswe",pady=5)

        self.grid()


    def validateATRQ(self,value):

        try:
            value = int(value)
            if 1 <= value <= 5:
                return True
            else:
                return False
        except:
            return False




    def validateKE(self,value):

        try:
            if value == "0-9" or value == "10-15" or value == "15+":
                return True
            else:
                return False
        except:
            return False



    def validateTIME(self,value):

        try:
            if value == "3-7" or value == "8-15" or value == "15+":
                return True
            else:
                return False
        except:
            return False


    def validateCFL(self,value):

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


    def normaliseKE(self,v):

            try:

                if v == "0-9":
                    return 0
                elif v == "10-15":
                    return 1
                elif v == "15+":
                    return 2
                else:

                    return -1
            except:

                return -1


    def normaliseTIME(self,v):
            try:
                if v == "3-7":
                    return 0
                elif v == "8-15":
                    return 1
                elif v == "15+":
                    return 2
                else:
                    return -1

            except:
                return -1



    def normaliseATRQ(self,v):
            try:
                v = int(v)
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
                        ATRQ_raw = self.ATEntry.get()
                        KE_raw = self.KEEntry.get()
                        TIME_raw = self.TIMEEntry.get()
                        CFL_raw = self.CFLDrop.get()



                        # Now that I know they are valid they can be cast to int
                        ATRQ = self.normaliseATRQ(self.ATEntry.get())
                        KE = self.normaliseKE(self.KEEntry.get())
                        TIME = self.normaliseTIME(self.TIMEEntry.get())
                        CFL = self.validateCFL(self.CFLDrop.get())
                        ClientName = self.clientINE.get()
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

                            tk.messagebox.showinfo(self,"Recommended Model: CASH")
                            self.modelResult = "CASH"
                        elif  0<=out<=2:

                            tk.messagebox.showinfo(self,"Recommended Model: Model 1")
                            self.modelResult = "Model 1"
                        elif  3<=out<=4:

                            tk.messagebox.showinfo(self,"Recommended Model: Model 2")
                            self.modelResult = "Model 2"
                        elif  5<=out<=6:

                            tk.messagebox.showinfo(self,"Recommended Model: Model 3")
                            self.modelResult = "Model 3"
                        elif  7<=out<=8:

                            tk.messagebox.showinfo(self,"Recommended Model: Model 4")
                            self.modelResult = "Model 4"
                        elif  9<=out<=11:

                            tk.messagebox.showinfo(self,"Recommended Model: Model 5")
                            self.modelResult = "Model 5"

                        desktop = os.path.expanduser(r"~\Desktop")



                        path = str(desktop) + r'//' + ClientName + " - Model Calculator - " + str(date.today()) + ".txt"
                        with open(path, 'w') as t:
                            t.write("Client Name: " + ClientName + "\n")
                            t.write("RECOMMENDED MODEL: " + self.modelResult + "\n")
                            t.write("ATRQ: " + ATRQ_raw + "\n")
                            t.write("K&E: " + KE_raw + "\n")
                            t.write("TIME: " + TIME_raw + "\n")
                            t.write("CFL: " + CFL_raw + "\n")
                            t.write("\n\n")
                            t.write("Results from table calculations:" + "\n")
                            t.write("TBL1: " + "ATRQ(" + ATRQ_raw + ") : " + "KE (" + KE_raw + ") = " + str(tbl1res) + "\n")
                            t.write("TBL2: " + "TBL1 (" + str(tbl1res-1) + ") : " + "TIME (" + TIME_raw + ") = " + str(tbl2res) + "\n")
                            t.write("TBL3: " + "TBL2 (" + str(tbl3res) + ") : " + "CFL (" + CFL_raw + ") = " + str(tbl3res) + "\n")

                    else:
                        tk.messagebox.showerror(self, "CFL Error: Please select either: None, Low, Medium or High")
                else:
                    tk.messagebox.showerror(self, "TIME Error: Please enter a number greater than 3")
            else:
                tk.messagebox.showerror(self, "K&E Error: Please enter a number greater than 1")
        else:
            tk.messagebox.showerror(self, "ATRQ Error: Please enter a number between 1 and 5.")



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        sv_ttk.set_theme("dark")
        self.title("")
        #self.geometry("300x350")
        self.resizable(False, False)


if __name__ == "__main__":
    run = App()
    Window(run)
    run.mainloop()



