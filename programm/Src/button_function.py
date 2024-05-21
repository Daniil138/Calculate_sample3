
from tkinter import * # Import the essential modules for the graphical user interface.
from tkinter import ttk
import tkinter.messagebox # For MessageBox widget.
from Src.calculate_model import calculate_model

#
#Класс функций для кнопок
#
class button_function:

    __calculate: calculate_model
    

    def __init__(self):
        self.__calculate = calculate_model


    def construct0(self):
        if self.__calculate.num == '0':
            tkinter.messagebox.showinfo("The error", "Can't begin with a zero.")
        else:
            self.__calculate.num += '0'
            self.__calculate.argument.set(self.__calculate.num)

    def construct1(self):
        self.__calculate.num += '1'
        self.__calculate.argument.set(self.__calculate.num)

    def construct2(self):
        self.__calculate.num += '2'
        self.__calculate.argument.set(self.__calculate.num)

    def construct3(self):
        self.__calculate.num += '3'
        self.__calculate.argument.set(self.__calculate.num)

    def construct4(self):
        self.__calculate.num += '4'
        self.__calculate.argument.set(self.__calculate.num)

    def construct5(self):
        self.__calculate.num += '5'
        self.__calculate.argument.set(self.__calculate.num)

    def construct6(self):
        self.__calculate.num += '6'
        self.__calculate.argument.set(self.__calculate.num)

    def construct7(self):
        self.__calculate.num += '7'
        self.__calculate.argument.set(self.__calculate.num)

    def construct8(self):
        self.__calculate.num += '8'
        self.__calculate.argument.set(self.__calculate.num)

    def construct9(self):
        self.__calculate.num += '9'
        self.__calculate.argument.set(self.__calculate.num)

    def constructd(self): # The dot.
        if '.' in self.__calculate.num:
            tkinter.messagebox.showinfo("The error", "A dot is used already.")
        elif self.__calculate.num == '':
            self.__calculate.num += "0."
            self.__calculate.argument.set(self.__calculate.num)
        else:
            self.__calculate.num += '.'
            self.__calculate.argument.set(self.__calculate.num)

    def constructm(self): # The minus.
        if self.__calculate.num == '':
            self.__calculate.num += '-'
            self.__calculate.argument.set(self.__calculate.num)
        else:
            tkinter.messagebox.showinfo("The error", "A minus can be put only in the beginning.")

    def goback(self): # The "backspace".
        if self.__calculate.num == '':
            tkinter.messagebox.showinfo("The error", "It's empty already.")
        else:
            self.__calculate.num = self.__calculate.num[:-1]
            self.__calculate.argument.set(self.__calculate.num)

    def delfromstack(self): # Deleting elements from the self.__calculate.stack.
        if len(self.__calculate.stack) == 0:
            tkinter.messagebox.showinfo("The error", "There is nothing on the self.__calculate.stack.")
        else:
            self.__calculate.stack = self.__calculate.stack[:-1]
            if len(self.__calculate.stack) == 0:
                self.__calculate.stacklist.set('')
            else:
                self.__calculate.stacklist.set(', '.join([str(x) for x in self.__calculate.stack]))

    def push(self): # Pushing on the self.__calculate.stack.
        if float(self.__calculate.num) % 1 == 0.0:
            self.__calculate.stack.append(int(self.__calculate.num))
        else:
            self.__calculate.stack.append(float(self.__calculate.num))
        self.__calculate.stacklist.set(', '.join([str(x) for x in self.__calculate.stack]))
        self.__calculate.argument.set('')
        self.__calculate.num = ''

    def factorial(self,number):
        if number == 0:
            return 1
        else:
            return number * self.factorial(number - 1)
        
    def performa(self): # Addition.
        if len(self.__calculate.stack) < 2:
            tkinter.messagebox.showinfo("The error", "At least 2 elements in the self.__calculate.stack are required.")
        else:
            self.__calculate.stack[-2] = self.__calculate.stack[-2] + self.__calculate.stack[-1]
            del self.__calculate.stack[-1]
            if self.__calculate.stack[-1] % 1 == 0.0:
                self.__calculate.stack[-1] = int(self.__calculate.stack[-1])
            self.__calculate.stacklist.set(', '.join([str(x) for x in self.__calculate.stack]))

    def performs(self): # Substraction.
        if len(self.__calculate.stack) < 2:
            tkinter.messagebox.showinfo("The error", "At least 2 elements in the self.__calculate.stack are required.")
        else:
            self.__calculate.stack[-2] = self.__calculate.stack[-2] - self.__calculate.stack[-1]
            del self.__calculate.stack[-1]
            if self.__calculate.stack[-1] % 1 == 0.0:
                self.__calculate.stack[-1] = int(self.__calculate.stack[-1])
            self.__calculate.stacklist.set(', '.join([str(x) for x in self.__calculate.stack]))

    def performm(self): # Multiplication.
        if len(self.__calculate.stack) < 2:
            tkinter.messagebox.showinfo("The error", "At least 2 elements in the self.__calculate.stack are required.")
        else:
            self.__calculate.stack[-2] = self.__calculate.stack[-2] * self.__calculate.stack[-1]
            del self.__calculate.stack[-1]
            if self.__calculate.stack[-1] % 1 == 0.0:
                self.__calculate.stack[-1] = int(self.__calculate.stack[-1])
            self.__calculate.stacklist.set(', '.join([str(x) for x in self.__calculate.stack]))

    def performd(self): # Division.
        if len(self.__calculate.stack) < 2:
            tkinter.messagebox.showinfo("The error", "At least 2 elements in the self.__calculate.stack ais required.")
        else:
            if self.__calculate.stack[-1] == 0:
                tkinter.messagebox.showinfo("The error", "The divisior is 0, can't perform the division.")
            else:
                self.__calculate.stack[-2] = int((self.__calculate.stack[-2] / self.__calculate.stack[-1]) * 1000000 + 0.5) / 1000000.0
                del self.__calculate.stack[-1]
                if self.__calculate.stack[-1] % 1 == 0.0:
                    self.__calculate.stack[-1] = int(self.__calculate.stack[-1])
                self.__calculate.stacklist.set(', '.join([str(x) for x in self.__calculate.stack]))

    def performf(self): # Factorial.
        if len(self.__calculate.stack) < 1:
            tkinter.messagebox.showinfo("The error", "At least 1 element in the self.__calculate.stack is required.")
        elif type(self.__calculate.stack[-1]) != int:
            tkinter.messagebox.showinfo("The error", "The type of the self.__calculate.argument is not an integer.")
        elif self.__calculate.stack[-1] < 0:
            tkinter.messagebox.showinfo("The error", "Unable to factor a negative self.__calculate.number.")
        elif self.__calculate.stack[-1] > 25:
            tkinter.messagebox.showinfo("The error", "The self.__calculate.number is too large.")
        else:
            self.__calculate.stack[-1] = self.factorial(self.__calculate.stack[-1])
            self.__calculate.stacklist.set(', '.join([str(x) for x in self.__calculate.stack]))

    def performp(self): # The power.
        if len(self.__calculate.stack) < 2:
            tkinter.messagebox.showinfo("The error", "At least 2 elements in the self.__calculate.stack are required.")
        else:
            self.__calculate.stack[-2] = self.__calculate.stack[-2] ** self.__calculate.stack[-1]
            del self.__calculate.stack[-1]
            self.__calculate.stacklist.set(', '.join([str(x) for x in self.__calculate.stack]))

    def performr(self): # The root.
        if len(self.__calculate.stack) < 2:
            tkinter.messagebox.showinfo("The error", "At least 2 elements in the self.__calculate.stack are required.")
        else:
            self.__calculate.stack[-2] = self.__calculate.stack[-2] ** self.__calculate.stack[-1]
            del self.__calculate.stack[-1]
            self.__calculate.stacklist.set(', '.join([str(x) for x in self.__calculate.stack]))

    def performmd(self): # The modulo.
        if len(self.__calculate.stack) < 2:
            tkinter.messagebox.showinfo("The error", "At least 2 elements in the self.__calculate.stack are required.")
        elif self.__calculate.stack[-1] >= 0:
            self.__calculate.stack[-2] = self.__calculate.stack[-2] % self.__calculate.stack[-1]
            del self.__calculate.stack[-1]
            self.__calculate.stacklist.set(', '.join([str(x) for x in self.__calculate.stack]))
        else:
            self.__calculate.stack[-1] = -self.__calculate.stack[-1]
            self.__calculate.stack[-2] = self.__calculate.stack[-2] % self.__calculate.stack[-1]
            del self.__calculate.stack[-1]
            self.__calculate.stacklist.set(', '.join([str(x) for x in self.__calculate.stack]))