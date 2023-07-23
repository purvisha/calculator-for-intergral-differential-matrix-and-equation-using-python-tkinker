from tkinter import *
import tkinter.messagebox as tmsg
import os
import time
from math import *
from sympy import *
import numpy as np
import cmath
def getvals(event):
value = event.widget.cget('text')
if value=='Clr':
sc_variable.set('')
if value=='enter':
sc_variable.set('')
elif value=='=':
try:
sc_variable.set(eval(screen.get()))
screen.update()
except Exception as e:
sc_variable.set('Error - Wait for 3 sec')
screen.update()
status_var.set('Preparing...')
screen.update()
time.sleep(3)
sc_variable.set('')
screen.update()
status_var.set('Ready..')
screen.update()
else:
sc_variable.set(f'{sc_variable.get()}{value}')
def display(self,value):
screen.delete(0, END)
screen.insert(0, value)
def integral():
mm = screen.get()
init_printing(use_unicode=False, wrap_line=False)
x = Symbol('x')
z=integrate(mm, x)
display(0,z)
def differential():
mm = screen.get()
init_printing()
x=Symbol('x')
dx=Derivative(mm)
dx=dx.doit()
display(0,dx)
def add():
mm = screen.get()
digits = mm.split()
l = int(len(digits) / 2)
if l % 2 != 0:
display('Not a Correct Matrix')
else:
n = sqrt(l)
rows,cols=(n,n)
a=[[0]*cols]*rows
b=[[0]*cols]*rows
for x in range(0, l):
a.append(int(digits[x]))
for x in range(l, len(digits)):
b.append(int(digits[x]))
c = np.array(a)
d = np.array(b)
e = c + d
display(0, e)
def mul():
mm=screen.get()
digits=[int(x) for x in str(mm)]
a=[[digits[0],digits[1]],[digits[2],digits[3]]]
b=[[digits[4],digits[5]],[digits[6],digits[7]]]
c=np.array(a)
d=np.array(b)
e=c.dot(d)
display(0,e)
def trans():
mm=screen.get()
digits=[int(x) for x in str(mm)]
a=[[digits[0],digits[1]],[digits[2],digits[3]]]
y=np.array(a)
d=np.transpose(y)
display(0,d)
def inv():
mm=screen.get()
digits=[int(x) for x in str(mm)]
a=[[digits[0],digits[1]],[digits[2],digits[3]]]
b=np.array(a)
c=np.linalg.inv(b)
display(0,c)
def det():
mm = screen.get()
digits = [int(x) for x in str(mm)]
a = [[digits[0], digits[1]], [digits[2], digits[3]]]
b = np.array(a)
c=np.linalg.det(b)
d=round(c)
display(0,d)
def equation():
mm=screen.get()
digits=[int(x) for x in str(mm)]
a1=digits[0]
b1=digits[1]
c1=digits[2]
a=float(a1)
b=float(b1)
c=float(c1)
sol = []
d = int((b ** 2) - (4 * a * c))
e=d*d
sol1 =(-b - e)/ int((2 * a))
sol2 =(-b + e) / int((2 * a))
sol.append(sol1)
sol.append(",")
sol.append(sol2)
display(0, sol)
root=Tk()
canvas_width=555
canvas_height=620
root.geometry(f'{canvas_width}x{canvas_height}')
root.maxsize(canvas_width,canvas_height)
root.minsize(canvas_width,canvas_height)
root.title('Calculator ')
my_menu=Menu(root)
m1=Menu(my_menu,tearoff=0,fg='red')
m1.add_command(label='adding matrix',command=add)
m1.add_command(label='multiply two matrices',command=mul)
m1.add_command(label='transposing of matrix',command=trans)
m1.add_command(label='determinant of matrix',command=det)
m1.add_command(label='inverse of matrix',command=inv)
root.config(menu=my_menu)
my_menu.add_cascade(label=' Matrix ',menu=m1)
my_menu.add_cascade(label=' Integral',command=integral)
my_menu.add_cascade(label=' Differential',command=differential)
my_menu.add_cascade(label=' Equation',command=equation)
my_menu.add_command(label='Exit',command=quit)
sc_variable=StringVar()
screen=Entry(root,textvariable=sc_variable,font='lucida 35 bold',fg='black',bg='white',borderwidth=10)
screen.pack(pady=30)
f=Frame(root)
f.pack()
b1=Button(f,text='7',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b2=Button(f,text='8',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b3=Button(f,text='9',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b4=Button(f,text='*',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b5=Button(f,text='sin',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b6=Button(f,text='(',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5.bind('<Button-1>',getvals)
b6.bind('<Button-1>',getvals)
buttons=[b1,b2,b3,b4,b5,b6]
count=0
for i in range(6):
buttons[count].grid(row=1,column=i)
count += 1
f=Frame(root)
f.pack()
b1=Button(f,text='4',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b2=Button(f,text='5',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b3=Button(f,text='6',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b4=Button(f,text='-',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b5=Button(f,text='cos',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b6=Button(f,text=')',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5.bind('<Button-1>',getvals)
b6.bind('<Button-1>',getvals)
buttons=[b1,b2,b3,b4,b5,b6]
count=0
for i in range(6):
buttons[count].grid(row=2,column=i)
count += 1
f=Frame(root)
f.pack()
b1=Button(f,text='1',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b2=Button(f,text='2',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b3=Button(f,text='3',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b4=Button(f,text='+',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b5=Button(f,text='tan',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b6=Button(f,text='%',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5.bind('<Button-1>',getvals)
b6.bind('<Button-1>',getvals)
buttons=[b1,b2,b3,b4,b5,b6]
count=0
for i in range(6):
buttons[count].grid(row=3,column=i)
count += 1
f=Frame(root)
f.pack()
b1=Button(f,text='.',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b2=Button(f,text='0',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b3=Button(f,text='[',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b4=Button(f,text=']',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b5=Button(f,text='log10',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b6=Button(f,text='pi',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5.bind('<Button-1>',getvals)
b6.bind('<Button-1>',getvals)
buttons=[b1,b2,b3,b4,b5,b6]
count=0
for i in range(6):
buttons[count].grid(row=4,column=i)
count += 1
f=Frame(root)
f.pack()
b1=Button(f,text='enter',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b2=Button(f,text='exp',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b3=Button(f,text='/',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b4=Button(f,text='Clr',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='red',width=3)
b5=Button(f,text='log',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b6=Button(f,text='=',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5.bind('<Button-1>',getvals)
b6.bind('<Button-1>',getvals)
buttons=[b1,b2,b3,b4,b5,b6]
count=0
for i in range(6):
buttons[count].grid(row=5,column=i)
count += 1
f=Frame(root)
f.pack()
b1=Button(f,text='x',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b2=Button(f,text='y',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b3=Button(f,text='𝑥^2',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b4=Button(f,text='y^2',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b5=Button(f,text='n',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b6=Button(f,text=',',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='black',bg='grey',width=3)
b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5.bind('<Button-1>',getvals)
b6.bind('<Button-1>',getvals)
buttons=[b1,b2,b3,b4,b5,b6]
count=0
for i in range(6):
buttons[count].grid(row=5,column=i)
count += 1
root.mainloop()
