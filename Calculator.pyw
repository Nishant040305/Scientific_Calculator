from tkinter import *
import math
import tkinter.messagebox
import prim
import seq
from random import choice
from traceback import format_exc
from sys import stderr
from time import strftime
from copy import deepcopy
root = Tk()
photo = PhotoImage(file = 'cal.png' )
root.iconphoto(False,photo)
 
# sets the name on the top of the gui
root.title("Scientific Calculator")
 
# sets the background color of the calculator
# as white
root.configure(background = 'white')
 
# fixed the width and height of the gui,
# hence can't be expanded/stretched

 
# sets the geometry
root.geometry("480x568+450+90")
 
# holds the buttons in the calculator,
# act as a container for numbers and operators
calc = Frame(root)
 
# create a grid like pattern of the frame
# i.e buttons
calc.grid()
#this is called class which consist of func inshort
class Calc():
    #init special kind of func in class
    def __init__(self):
        self.total = 0
        self.current = ''
        self.input_value = True
        self.check_sum = False
        self.op = ''
        self.result = False
 
    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum+secondnum
        self.display(self.current)
 
    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())
 
    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)
 
    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        if self.op == 'pow':
            self.total = self.total**self.current
        if self.op == 'ncr':
            try:
                if self.total == int(self.total):
                    self.total = int(self.total)
                    self.current = int(self.current)
                    self.total = math.comb(self.total,self.current)
                else:
                    self.total='syntax error'
            except:
                self.total = 'syntax error'
        if self.op =='gcd':
            try:
                if self.total == int(self.total):
                    self.total = int(self.total)
                    self.current = int(self.current)
                    self.total = math.gcd(self.total,self.current)
                else:
                    self.total='syntax error'
            except:
                self.total = 'syntax error'
        if self.op=='prange':
            self.total=prim.prange(self.current,self.total)
        self.input_value = True
        self.check_sum = False
        self.display(self.total)
 
    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False
 
    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True
 
    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0
 
    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)
 
    def tau(self):
        self.result = False
        self.current = math.atan(float(txtDisplay.get()))
        self.display(self.current)
 
    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)
 
    def mathPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)
 
    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)
 
    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)
 
    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
 
    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)
 
    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
 
    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)
 
    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    def factoril(self):
        self.result = False
        try:
            self.current = int(self.current)
            self.current = math.factorial(int(txtDisplay.get()))
            self.display(self.current)
        except:
            self.display('syntax error')
 
    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)
 
    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)
 
    def acos(self):
        self.result = False
        self.current = math.acos(float(txtDisplay.get()))
        self.display(self.current)
 
    def asin(self):
        self.result = False
        self.current = math.asin(float(txtDisplay.get()))
        self.display(self.current)
 
    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(txtDisplay.get()))
        self.display(self.current)
 
    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)
 
    def log2(self):
        self.result = False
        self.current = math.log2(float(txtDisplay.get()))
        self.display(self.current)
 
    def log10(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)
    def primx(self):
        self.result = False
        self.current = prim.prime(float(txtDisplay.get()))
        self.display(self.current)
    def rad(self):
        self.result = False
        self.current = math.radians(float(txtDisplay.get()))
        self.display(self.current)
    def col(self):
        self.result = False
        self.current = seq.c(float(txtDisplay.get()))
        self.display(self.current)
            
added_value = Calc()
txtDisplay = Entry(calc,
                   font=('Helvetica', 20,
                         'bold'),
                   bg='black',
                   fg='white',
                   bd=30,
                   width=28,
                   justify=RIGHT)
 
txtDisplay.grid(row=0,
                column=0,
                columnspan=4,
                pady=1)
 
txtDisplay.insert(0, "0")
# store all the numbers in a variable
numberpad = "789456123"
 
# here i will count the rows for placing buttons
# in grid
i = 0
 
# create an empty list to store
# each button with its particular specifications
btn = []
 
# j is in that range to place
# the button in that particular row
for j in range(2, 5):
 
        # k is in this range to place the
    # button in that particular column
    for k in range(3):
        btn.append(Button(calc,
                          width=6,
                          height=2,
                          bg='black',
                          fg='white',
                          font=('Helvetica', 20, 'bold'),
                          bd=4, text=numberpad[i]))
 
        # set buttons in row & column and
        # separate them with a padding of 1 unit
        btn[i].grid(row=j, column=k, pady=1)
 
        # put that number as a symbol on that button
        btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
        i += 1
btnClear = Button(calc, text=chr(67),
                  width=6, height=2,
                  bg='powder blue',
                  font=('Helvetica', 20, 'bold'),
                  bd=4,
                  command=added_value.Clear_Entry).grid(
    row=1, column=0, pady=1)
 
btnAllClear = Button(calc, text=chr(67)+chr(69),
                     width=6, height=2,
                     bg='powder blue',
                     font=('Helvetica',
                           20, 'bold'), bd=4,
                     command=added_value.All_Clear_Entry).grid(
    row=1, column=1, pady=1)
 
btnsq = Button(calc, text="\u221A", width=6,
               height=2, bg='powder blue',
               font=('Helvetica', 20, 'bold'),
               bd=4, command=added_value.squared).grid(
    row=1, column=2, pady=1)
 
btnAdd = Button(calc, text="+", width=6,
                height=2, bg='powder blue',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=lambda: added_value.operation("add")
                ).grid(row=1, column=3, pady=1)
 
btnSub = Button(calc, text="-", width=6,
                height=2, bg='powder blue',
                font=('Helvetica', 20, 'bold'),
                bd=4,
                command=lambda: added_value.operation("sub")
                ).grid(row=2, column=3, pady=1)
 
btnMul = Button(calc, text="x", width=6, height=2,
                bg='powder blue',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=lambda: added_value.operation("multi")
                ).grid(row=3, column=3, pady=1)
 
btnDiv = Button(calc, text="/", width=6,
                height=2, bg='powder blue',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=lambda: added_value.operation("divide")
                ).grid(row=4, column=3, pady=1)
 
btnZero = Button(calc, text="0", width=6,
                 height=2, bg='black', fg='white',
                 font=('Helvetica', 20, 'bold'),
                 bd=4, command=lambda: added_value.numberEnter(0)
                 ).grid(row=5, column=0, pady=1)
 
btnDot = Button(calc, text=".", width=6,
                height=2, bg='powder blue',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=lambda: added_value.numberEnter(".")
                ).grid(row=5, column=1, pady=1)
btnPM = Button(calc, text=chr(177), width=6,
               height=2, bg='powder blue',
               font=('Helvetica', 20, 'bold'),
               bd=4, command=added_value.mathPM
               ).grid(row=5, column=2, pady=1)
 
btnEquals = Button(calc, text="=", width=6,
                   height=2, bg='powder blue',
                   font=('Helvetica', 20, 'bold'),
                   bd=4, command=added_value.sum_of_total
                   ).grid(row=5, column=3, pady=1)
# ROW 1 :
 
btnPi = Button(calc, text="\u03C0", width=6,
               height=2, bg='black', fg='white',
               font=('Helvetica', 20, 'bold'),
               bd=4, command=added_value.pi
               ).grid(row=1, column=7, pady=1)
 
btnCos = Button(calc, text="Cos", width=6,
                height=2, bg='black', fg='white',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=added_value.cos
                ).grid(row=1, column=5, pady=1)
 
btntan = Button(calc, text="tan", width=6,
                height=2, bg='black', fg='white',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=added_value.tan
                ).grid(row=1, column=6, pady=1)
 
btnsin = Button(calc, text="sin", width=6,
                height=2, bg='black', fg='white',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=added_value.sin
                ).grid(row=1, column=4, pady=1)
 
# ROW 2 :
 
btn2Pi = Button(calc, text="atan", width=6,
                height=2, bg='black', fg='white',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=added_value.tau
                ).grid(row=2, column=6, pady=1)
 
btnCosh = Button(calc, text="Cosh", width=6,
                 height=2, bg='black', fg='white',
                 font=('Helvetica', 20, 'bold'),
                 bd=4, command=added_value.cosh
                 ).grid(row=3, column=5, pady=1)
 
btntanh = Button(calc, text="tanh", width=6,
                 height=2, bg='black', fg='white',
                 font=('Helvetica', 20, 'bold'),
                 bd=4, command=added_value.tanh
                 ).grid(row=3, column=6, pady=1)
 
btnsinh = Button(calc, text="sinh", width=6,
                 height=2, bg='black', fg='white',
                 font=('Helvetica', 20, 'bold'),
                 bd=4, command=added_value.sinh
                 ).grid(row=3, column=4, pady=1)
 
# ROW 3 :
 
btnlog = Button(calc, text="ln", width=6,
                height=2, bg='black', fg='white',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=added_value.log
                ).grid(row=4, column=5, pady=1)
 
btnExp = Button(calc, text="exp", width=6,
                height=2, bg='black', fg='white',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=added_value.exp
                ).grid(row=4, column=7, pady=1)
 
btnMod = Button(calc, text="Mod", width=6,
                height=2, bg='black', fg='white',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=lambda: added_value.operation("mod")
                ).grid(row=5, column=7, pady=1)
 
btnE = Button(calc, text="e", width=6,
              height=2, bg='black', fg='white',
              font=('Helvetica', 20, 'bold'),
              bd=4, command=added_value.e
              ).grid(row=2, column=7, pady=1)
 
# ROW 4 :
 
btnlog10 = Button(calc, text="log10", width=6,
                  height=2, bg='black', fg='white',
                  font=('Helvetica', 20, 'bold'),
                  bd=4, command=added_value.log10
                  ).grid(row=4, column=4, pady=1)

 
btncomb = Button(calc, text="nCr", width=6,
                height=2, bg='black', fg='white',
                font=('Helvetica', 20, 'bold'),
                bd=4, command= lambda : added_value.operation('ncr')
                ).grid(row=5, column=5, pady=1)
 
btnpow = Button(calc, text="pow", width=6,
                  height=2, bg='black', fg='white',
                  font=('Helvetica', 20, 'bold'),
                  bd=4, command= lambda : added_value.operation('pow')
                  ).grid(row=4, column=6, pady=1)
 
btngamma = Button(calc, text="gamma", width=6,
                  height=2, bg='black', fg='white',
                  font=('Helvetica', 20, 'bold'),
                  bd=4, command=added_value.lgamma
                  ).grid(row=5, column=6, pady=1)
# ROW 5 :
 
btnfact = Button(calc, text="!", width=6,
                 height=2, bg='black', fg='white',
                 font=('Helvetica', 20, 'bold'),
                 bd=4, command=added_value.factoril
                 ).grid(row=5, column=4, pady=1)
 
btndeg = Button(calc, text="deg", width=6,
                height=2, bg='black', fg='white',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=added_value.degrees
                ).grid(row=3, column=7, pady=1)
 
btnacos = Button(calc, text="acos", width=6,
                  height=2, bg='black', fg='white',
                  font=('Helvetica', 20, 'bold'),
                  bd=4, command=added_value.acos
                  ).grid(row=2, column=5, pady=1)
 
btnasin = Button(calc, text="asin", width=6,
                  height=2, bg='black', fg='white',
                  font=('Helvetica', 20, 'bold'),
                  bd=4, command=added_value.asin
                  ).grid(row=2, column=4, pady=1)
#column 8
btnprime = Button(calc,text = 'prime',width = 7, 
                height = 2,bg = 'black',fg = 'white',
                font = ('Helvetica', 20, 'bold'),
                bd = 4, command= added_value.primx
                ).grid(row=1, column=8, pady=1)
btngcd = Button(calc,text = 'Gcd',width = 7,
                height = 2,bg = 'black',fg = 'white',
                font = ('Helvetica', 20, 'bold'),
                bd = 4, command= lambda: added_value.operation('gcd')
                ).grid(row=2, column=8, pady=1)
btnrad = Button(calc,text = 'radian',width = 7,
                height = 2,bg = 'black',fg = 'white',
                font = ('Helvetica', 20, 'bold'),
                bd = 4, command= added_value.rad
                ).grid(row=3, column=8, pady=1)
btnprange = Button(calc,text = 'prime list',width = 7, 
                height = 2,bg = 'black',fg = 'white',
                font = ('Helvetica', 20, 'bold'),
                bd = 4,command= lambda: added_value.operation('prange')
                ).grid(row=4, column=8, pady=1)
btncol = Button(calc,text = 'collatz',width = 7, 
                height = 2,bg = 'black',fg = 'white',
                font = ('Helvetica', 20, 'bold'),
                bd = 4,command= added_value.col,
                ).grid(row=5, column=8, pady=1)
 
lblDisplay = Label(calc, text="Scientific Calculator",
                   font=('Helvetica', 30, 'bold'),
                   bg='black', fg='white', justify=CENTER)
lblDisplay.grid(row=0, column=4, columnspan=4)
# use askyesno function to
# stop/continue the program execution
def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator",
                                        "Do you want to exit ?")
    if iExit>0:
        root.destroy()
        return
 
def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("1080x568+0+0")
 
 
def Standard():
    root.resizable(width=False, height=False)
    root.geometry("480x568+0+0")
 
menubar = Menu(calc)
 
# ManuBar 1 :
 
filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'File', menu = filemenu)
filemenu.add_command(label = "Standard", command = Standard)
filemenu.add_command(label = "Scientific", command = Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = iExit)

# ManuBar 2 :
 
editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Edit', menu = editmenu)
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Copy")
editmenu.add_separator()
editmenu.add_command(label = "Paste")

root.config(menu=menubar)
 
root.mainloop()
'''     def sysetem(self):
        system = int(input('system'))
        k = 0
        while(True):
            if system**k>self.num:
                break
            k=k+1
        for n in range(k-1,-1,-1):
            a=str(int(self.num//system**n))
            self.num = self.num-int(a)*system**n
            self.transform = self.transform+a
        return self.transform

'''