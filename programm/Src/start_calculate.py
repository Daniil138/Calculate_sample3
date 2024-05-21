

from tkinter import * # Import the essential modules for the graphical user interface.
from tkinter import ttk
import tkinter.messagebox # For MessageBox widget.
from Src.calculate_model import calculate_model
from  Src.button_function import button_function
from Src.buttons import buttons


#
#Класс сдля 
#
class start_calculate:
    __bt_func: button_function
    __calc_model: calculate_model
    __buttons: buttons




    def __init__(self) -> None:
        self.__calc_model = calculate_model()
        self.__buttons = buttons()

    def start(self):
        bt0 = self.__buttons.get_button("7")
        bt1 = self.__buttons.get_button("8")
        bt2 = self.__buttons.get_button("9")
        bt3 = self.__buttons.get_button("+")
        bt4 = self.__buttons.get_button("4")
        bt5 = self.__buttons.get_button("5")
        bt6 = self.__buttons.get_button("6")
        bt7 = self.__buttons.get_button("-")
        bt8 = self.__buttons.get_button("1")
        bt9 = self.__buttons.get_button("2")
        bt10 = self.__buttons.get_button("3")
        bt11 = self.__buttons.get_button("*")
        bt12 = self.__buttons.get_button("0")
        bt13 = self.__buttons.get_button(".")
        bt14 = self.__buttons.get_button("!")
        bt15 = self.__buttons.get_button("/")
        bt16 = self.__buttons.get_button("Push!")
        bt17 = self.__buttons.get_button("neg")
        bt18 = self.__buttons.get_button("<-")
        bt19 = self.__buttons.get_button("<- (st)")
        bt0.grid(column = 0, row = 2) 
        bt1.grid(column = 1, row = 2)
        bt2.grid(column = 2, row = 2)
        bt3.grid(column = 3, row = 2)
        bt4.grid(column = 0, row = 3)
        bt5.grid(column = 1, row = 3)
        bt6.grid(column = 2, row = 3)
        bt7.grid(column = 3, row = 3)
        bt8.grid(column = 0, row = 4)
        bt9.grid(column = 1, row = 4)
        bt10.grid(column = 2, row = 4)
        bt11.grid(column = 3, row = 4)
        bt12.grid(column = 0, row = 5)
        bt13.grid(column = 1, row = 5)
        bt14.grid(column = 2, row = 5)
        bt15.grid(column = 3, row = 5)
        bt16.grid(column = 3, row = 1)
        bt17.grid(column = 2, row = 1)
        bt18.grid(column = 1, row = 1)
        bt19.grid(column = 0, row = 1)
        self.__calc_model.rt.mainloop()








