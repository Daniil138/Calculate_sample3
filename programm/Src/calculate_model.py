
from tkinter import * # Import the essential modules for the graphical user interface.
from tkinter import ttk
import tkinter.messagebox # For MessageBox widget.



#
#Клас для инициализации и хранения основных переменных калькулятора 
#
class calculate_model:
    rt = Tk() # The root.
    # rt.title("RPN Calc 1.1 by Shino") # The title of the application.
    # rt.resizable(0, 0) # The window should not be resizable.
    mf = ttk.Frame(rt)
    argument, stacklist = StringVar(), StringVar() # For changing the content of the certain elements of the application.
    # mf.grid(column = 0, row = 0, sticky = (N, W, E, S)) # Everything is displayed in a grid.
    label0 = Label(mf, textvariable = stacklist)
    # label0.grid(row = 0, columnspan = 3)
    label1 = Label(mf, textvariable = argument, background = "white")
    # label1.grid(row = 0, column = 3)
    stack, command, num = [], '', ''




    def __init__(self) -> None:
        self.rt.title("RPN Calc 1.1 by Shino") # The title of the application.
        self.rt.resizable(0, 0) # The window should not be resizable.
        self.mf.grid(column = 0, row = 0, sticky = (N, W, E, S))
        self.label0.grid(row = 0, columnspan = 3)
        self.label1.grid(row = 0, column = 3)
        

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(calculate_model, cls).__new__(cls)

        return cls.instance  
    
    
    
    



