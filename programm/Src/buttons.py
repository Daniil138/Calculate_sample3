
from tkinter import * # Import the essential modules for the graphical user interface.
from tkinter import ttk
import tkinter.messagebox # For MessageBox widget.
from  Src.button_function import button_function
from Src.calculate_model import calculate_model


#
#Класс кнопки
#

class buttons:
    __data = {}
    __bt_func: button_function
    __calc_model: calculate_model



    


    def __init__(self):
        self.__bt_func =  button_function()
        self.__calc_model = calculate_model()

        self.__data={
            "7": Button(self.__calc_model.mf, text = "7", command = self.__bt_func.construct7, width = 5, height = 2),
            "8": Button(self.__calc_model.mf, text = "8", command = self.__bt_func.construct8, width = 5, height = 2),
            "9": Button(self.__calc_model.mf, text = "9", command = self.__bt_func.construct9, width = 5, height = 2),
            "+": Button(self.__calc_model.mf, text = "+", command = self.__bt_func.performa, width = 5, height = 2),
            "4": Button(self.__calc_model.mf, text = "4", command = self.__bt_func.construct4, width = 5, height = 2),
            "5": Button(self.__calc_model.mf, text = "5", command = self.__bt_func.construct5, width = 5, height = 2),
            "6": Button(self.__calc_model.mf, text = "6", command = self.__bt_func.construct6, width = 5, height = 2),
            "-": Button(self.__calc_model.mf, text = "-", command = self.__bt_func.performs, width = 5, height = 2),
            "1": Button(self.__calc_model.mf, text = "1", command = self.__bt_func.construct1, width = 5, height = 2),
            "2": Button(self.__calc_model.mf, text = "2", command = self.__bt_func.construct2, width = 5, height = 2),
            "3": Button(self.__calc_model.mf, text = "3", command = self.__bt_func.construct3, width = 5, height = 2),
            "*": Button(self.__calc_model.mf, text = "*", command = self.__bt_func.performm, width = 5, height = 2),
            "0": Button(self.__calc_model.mf, text = "0", command = self.__bt_func.construct0, width = 5, height = 2),
            ".": Button(self.__calc_model.mf, text = ".", command = self.__bt_func.constructd, width = 5, height = 2),
            "!": Button(self.__calc_model.mf, text = "!", command = self.__bt_func.performa, width = 5, height = 2),
            "/": Button(self.__calc_model.mf, text = "/", command = self.__bt_func.performd, width = 5, height = 2),
            "Push!":  Button(self.__calc_model.mf, text = "Push!", command = self.__bt_func.push, width = 5, height = 2),
            "neg": Button(self.__calc_model.mf, text = "neg", command = self.__bt_func.constructm, width = 5, height = 2),
            "<-": Button(self.__calc_model.mf, text = "<-", command = self.__bt_func.goback, width = 5, height = 2),
            "<- (st)": Button(self.__calc_model.mf, text = "<- (st)", command = self.__bt_func.delfromstack, width = 5, height = 2)
        }
        
    def get_button(self, value: str):
        if type(value)!= str:
            print("Не корректно преданы параметры")
            return
        return self.__data[value]

    

        
