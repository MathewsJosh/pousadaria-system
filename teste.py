from tkinter import *


Window = Tk()

class Test:
    def __init__(self):

        self.array = ['a', 'b', 'c', 'd']
        self.vars = []

        self.doCheckbutton()

    def doCheckbutton(self):
        for i in range(len(self.array)):
            self.vars.append(StringVar())
            self.vars[-1].set(0)
            c = Checkbutton(Window, text=self.array[i], variable=self.vars[i], command=lambda i=i: self.printSelection(i), onvalue=self.array[i], offvalue=0)
            c.pack()
        print(self.vars, type(self.vars))


    def printSelection(self, i):
        print(self.vars[i].get())
        #print(self.vars)
        #print(type(self.vars))

Test()

Window.mainloop()