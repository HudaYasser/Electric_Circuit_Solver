from __future__ import print_function
from __future__ import division

import SchemDraw as schem
import SchemDraw.elements as e
from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
import sympy
import numpy as np
from tkinter import messagebox

class element:
    def __init__(self, kind, position, value = 0):
        self.kind = kind
        self.position = position
        self.value = value
class MyWindow:
    def __init__(self, win):
        self.mylabel1=Label(win, text="Hello^_^!\n\n      welcome to our simple program for solving electric circuit ,here a simple tips you should know")
        self.mylabel1.place(x=0, y=0)
        self.bb=Button(win, text="click here", command=self.our_tips)
        self.bb.place(x=420, y=60)
        self.lbl1=Label(win, text='Enter the Start Point')
        self.lbl2=Label(win, text='Enter the End Point')
        self.lbl4=Label(win, text='Enter the Value')
        self.lbl5=Label(win, text='Select the component')
        self.Start_Point=Entry()
        self.End_Point=Entry()
        self.Value=Entry()
        self.b1=Button(win, text='Set Value', command=self.set)
        self.b2=Button(win, text='Add the element', command=self.add)
        self.b3=Button(win, text='Draw the circuit', command=self.drawCircuit)
        self.b3.place(x=400, y=450)
        self.b4=Button(win, text='Analyze the circuit', command=self.analyze)
        self.b4.place(x=400, y=500)
        self.menubar = Menu(win)
        self.menubar.add_command(label="New", command=self.newCircuit)
        win.config(menu=self.menubar)
        self.b1.place(x=30, y=450)
        self.lbl5.place(x=20, y=100)
        data=("Resistor","Voltage Independent Source", "Current Independent Source", "Wire")
        self.cb=Combobox(win, values=data)
        self.cb.place(x=150, y=130,width=200)
        self.txt = scrolledtext.ScrolledText(win)
        self.elements = []
        self.results = []

    def our_tips(self):
        messagebox.showinfo("tips", "you should know some information about how to draw the circuit\n ->First:\nthe points are represented as 3x3 grid \n ->Second:\ngrid[0][0] represent point 1\ngrid[0][1] represent point 4\ngrid[0][2] represent point 7\ngrid[1][0] represent point 2\ngrid[1][1] represent point 5\ngrid[1][2] represent point 8\ngrid[2][0] represent point 3\ngrid[2][1] represent point 6\ngrid[2][2] represent point 9")
    def solvecircuit(self):
        mycircuit = circuit()
        #gnd
        mycircuit.addR('R0', 0, 6, 0)
        for elem in self.elements:
            if elem.kind == "Wire":
                mycircuit.addR('R'+ elem.position, int(elem.position[0]), int(elem.position[1]), 0)

            elif elem.kind == "Resistor":
                mycircuit.addR('R'+ elem.position, int(elem.position[0]), int(elem.position[1]), elem.value)

            elif elem.kind == "Voltage Independent Source":
                mycircuit.addV('V'+ elem.position, int(elem.position[0]), int(elem.position[1]), elem.value)

            elif elem.kind == "Current Independent Source":
                mycircuit.addI('I'+ elem.position, int(elem.position[0]), int(elem.position[1]), elem.value)

            self.results = mycircuit.solve()

    def analyze(self):
        self.mylabel1.place(x=-100, y=-100)
        self.bb.place(x=-100, y=-100)
        self.b2.place(x=-100, y=-500)
        self.lbl1.place(x=-100, y=-350)
        self.lbl2.place(x=-100, y=-400)
        self.Start_Point.place(x=-200, y=-350)
        self.End_Point.place(x=-200, y=-400)
        self.Value.place(x=-200, y=-200)
        self.lbl4.place(x=-100, y=-200)
        self.lbl5.place(x=-100, y=-200)
        self.cb.place(x=-100, y=-200)
        self.b1.place(x=-300, y=-500)
        self.b2.place(x=-300, y=-500)
        self.b3.place(x=-300, y=-500)
        self.b4.place(x=-300, y=-500)
        self.solvecircuit()
        for result in self.results:
            self.txt.insert(INSERT,result)
            self.txt.insert(INSERT, " = ")
            self.txt.insert(INSERT,self.results[result])
            self.txt.insert(INSERT,'\n')
        self.txt.place(x=20, y=20)

    def newCircuit(self):
        self.bb.place(x=420, y=60)
        self.mylabel1.place(x=0, y=0)
        self.cb.place(x=150, y=130,width=200)
        self.lbl5.place(x=20, y=100)
        self.b3.place(x=400, y=450)
        self.b4.place(x=400, y=500)
        self.b1.place(x=30, y=450)
        self.txt.place(x=-1000, y=-1000)
        for elem in self.elements:
            self.elements.remove(elem)
        self.b2.place(x=-100, y=-500)
        self.lbl1.place(x=-100, y=-350)
        self.lbl2.place(x=-100, y=-400)
        self.Start_Point.place(x=-200, y=-350)
        self.End_Point.place(x=-200, y=-400)
        self.Value.place(x=-200, y=-200)
        self.lbl4.place(x=-100, y=-200)

    def set(self):
        self.cb.place(x=150, y=130,width=200)
        self.lbl5.place(x=20, y=100)
        self.b3.place(x=400, y=450)
        self.b4.place(x=400, y=500)
        self.b1.place(x=30, y=450)
        self.txt.place(x=-1000, y=-1000)
        self.b2.place(x=-100, y=-500)
        self.lbl1.place(x=-100, y=-350)
        self.lbl2.place(x=-100, y=-400)
        self.Start_Point.place(x=-200, y=-350)
        self.End_Point.place(x=-200, y=-400)
        self.Value.place(x=-200, y=-200)
        self.lbl4.place(x=-100, y=-200)

        self.Start_Point.delete(0, 'end')
        self.End_Point.delete(0, 'end')
        self.Value.delete(0, 'end')

        kind = self.cb.get()
        self.lbl1.place(x=20, y=200)
        self.Start_Point.place(x=70, y=220)
        self.lbl2.place(x=120, y=270)
        self.End_Point.place(x=170, y=290)
        self.b2.place(x=30, y=500)

        if (kind == "Resistor" or kind == "Voltage Independent Source" or kind == "Current Independent Source" ):
            self.Value.place(x=270, y=360)
            self.lbl4.place(x=220, y=340)

    def add(self):
        self.b2.place(x=-100, y=-500)
        self.lbl1.place(x=-100, y=-350)
        self.lbl2.place(x=-100, y=-400)
        self.Start_Point.place(x=-200, y=-350)
        self.End_Point.place(x=-200, y=-400)
        self.Value.place(x=-200, y=-200)
        self.lbl4.place(x=-100, y=-200)

        sp = self.Start_Point.get()
        ep = self.End_Point.get()
        position = sp + ep
        kind = self.cb.get()
        if (kind == "Resistor" or kind == "Voltage Independent Source" or kind == "Current Independent Source" ):
            value = int(self.Value.get())
            elem = element(kind, position, value)
        else:
            elem = element(kind, position)
        self.elements.append(elem)

    def drawCircuit(self):
        d = schem.Drawing(unit=2, fontsize=12, font='monospace')
        d1 = d.add(e.DOT)
        l12 = d.add(e.LINE, d='down', xy = d1.end, color='white')
        d2 = d.add(e.DOT, xy = l12.end)
        l23 = d.add(e.LINE, d='down', xy = d2.end, color='white')
        d3 = d.add(e.DOT, xy = l23.end)
        l14 = d.add(e.LINE, d='right', xy = d1.end, color='white')
        d4 = d.add(e.DOT, xy = l14.end)
        l45 = d.add(e.LINE, d='down', xy = d4.end, color='white')
        d5 = d.add(e.DOT, xy = l45.end)
        l56 = d.add(e.LINE, d='down', xy = d5.end, color='white')
        d6 = d.add(e.DOT, xy = l56.end)
        l47 = d.add(e.LINE, d='right', xy = d4.end, color='white')
        d7 = d.add(e.DOT, xy = l47.end)
        l78 = d.add(e.LINE, d='down', xy = d7.end, color='white')
        d8 = d.add(e.DOT, xy = l78.end)
        l89 = d.add(e.LINE, d='down', xy = d8.end, color='white')
        d9 = d.add(e.DOT, xy = l89.end)
        l25 = d.add(e.LINE, d='right', xy = d2.end, color='white')
        l58 = d.add(e.LINE, d='right', xy = d5.end, color='white')
        l36 = d.add(e.LINE, d='right', xy = d3.end, color='white')
        l69 = d.add(e.LINE, d='right', xy = d6.end, color='white')
        gnd = d.add(e.GND, d='right', xy = l56.end, color='black')

        for elem in self.elements:
            if elem.position == '12':
                if (elem.kind == 'Resistor'):
                    R1 = d.add(e.RES, d='down', label=str(elem.value)+'$\Omega$', xy = l12.start)
                elif (elem.kind == 'Voltage Independent Source'):
                    S1 = d.add(e.SOURCE_V, d='down', label=str(elem.value)+'V', xy = l12.start)
                elif (elem.kind == 'Current Independent Source'):
                    S1 = d.add(e.SOURCE_I, d='down', label=str(elem.value)+'A', xy = l12.start)
                l12.color = 'none'
                if (elem.kind == 'Wire'):
                    l12.color = 'black'
            elif elem.position == '21':
                if (elem.kind == 'Resistor'):
                    R1 = d.add(e.RES, d='up', label=str(elem.value)+'$\Omega$', xy = l12.end)
                elif (elem.kind == 'Voltage Independent Source'):
                    S1 = d.add(e.SOURCE_V, d='up', label=str(elem.value)+'V', xy = l12.end)
                elif (elem.kind == 'Current Independent Source'):
                    S1 = d.add(e.SOURCE_I, d='up', label=str(elem.value)+'A', xy = l12.end)
                l12.color = 'none'
                if (elem.kind == 'Wire'):
                    l12.color = 'black'
            elif elem.position == '23':
                if (elem.kind == 'Resistor'):
                    R2 = d.add(e.RES, d='down', label=str(elem.value)+'$\0mega$', xy = l23.start)
                elif (elem.kind == 'Voltage Independent Source'):
                    S2 = d.add(e.SOURCE_V, d='down', label=str(elem.value)+'V', xy = l23.start)
                elif (elem.kind == 'Current Independent Source'):
                    S2 = d.add(e.SOURCE_I, d='down', label=str(elem.value)+'A', xy = l23.start)
                l23.color = 'none'
                if (elem.kind == 'Wire'):
                    l23.color = 'black'
            elif elem.position == '32':
                if (elem.kind == 'Resistor'):
                    R2 = d.add(e.RES, d='up', label=str(elem.value)+'$\0mega$', xy = l23.end)
                elif (elem.kind == 'Voltage Independent Source'):
                    S2 = d.add(e.SOURCE_V, d='up', label=str(elem.value)+'V', xy = l23.end)
                elif (elem.kind == 'Current Independent Source'):
                    S2 = d.add(e.SOURCE_I, d='up', label=str(elem.value)+'A', xy = l23.end)
                l23.color = 'none'
                if (elem.kind == 'Wire'):
                    l23.color = 'black'
            elif elem.position == '58':
                if (elem.kind == 'Resistor'):
                    R3 = d.add(e.RES, d='right', label=str(elem.value)+'$\0mega$', xy = l58.start)
                elif (elem.kind == 'Voltage Independent Source'):
                    S3 = d.add(e.SOURCE_V, d='right', label=str(elem.value)+'V', xy = l58.start)
                elif (elem.kind == 'Current Independent Source'):
                    S3 = d.add(e.SOURCE_I, d='right', label=str(elem.value)+'A', xy = l58.start)
                l58.color = 'none'
                if (elem.kind == 'Wire'):
                    l58.color = 'black'
            elif elem.position == '85':
                if (elem.kind == 'Resistor'):
                    R3 = d.add(e.RES, d='left', label=str(elem.value)+'$\Omega$', xy = l58.end)
                elif (elem.kind == 'Voltage Independent Source'):
                    S3 = d.add(e.SOURCE_V, d='left', label=str(elem.value)+'V', xy = l58.end)
                elif (elem.kind == 'Current Independent Source'):
                    S3 = d.add(e.SOURCE_I, d='left', label=str(elem.value)+'A', xy = l58.end)
                l58.color = 'none'
                if (elem.kind == 'Wire'):
                    l58.color = 'black'
            elif elem.position == '14':
                if (elem.kind == 'Resistor'):
                    R4 = d.add(e.RES, d='right', label=str(elem.value)+'$\Omega$', xy = l14.start)
                elif (elem.kind == 'Voltage Independent Source'):
                    S4 = d.add(e.SOURCE_V, d='right', label=str(elem.value)+'V', xy = l14.start)
                elif (elem.kind == 'Current Independent Source'):
                    S4 = d.add(e.SOURCE_I, d='right', label=str(elem.value)+'A', xy = l14.start)
                l14.color = 'none'
                if (elem.kind == 'Wire'):
                    l14.color = 'black'
            elif elem.position == '41':
                if (elem.kind == 'Resistor'):
                    R4 = d.add(e.RES, d='left', label=str(elem.value)+'$\Omega$', xy = l14.end)
                elif (elem.kind == 'Voltage Independent Source'):
                    S4 = d.add(e.SOURCE_V, d='left', label=str(elem.value)+'V', xy = l14.end)
                elif (elem.kind == 'Current Independent Source'):
                    S4 = d.add(e.SOURCE_I, d='left', label=str(elem.value)+'A', xy = l14.end)
                l14.color = 'none'
                if (elem.kind == 'Wire'):
                    l14.color = 'black'
            elif elem.position == '47':
                if (elem.kind == 'Resistor'):
                    R5 = d.add(e.RES, d='right', label=str(elem.value)+'$\Omega$', xy = l47.start)
                elif (elem.kind == 'Voltage Independent Source'):
                    S5 = d.add(e.SOURCE_V, d='right', label=str(elem.value)+'V', xy = l47.start)
                elif (elem.kind == 'Current Independent Source'):
                    S5 = d.add(e.SOURCE_I, d='right', label=str(elem.value)+'A', xy = l47.start)
                l47.color = 'none'
                if (elem.kind == 'Wire'):
                    l47.color = 'black'
            elif elem.position == '74':
                if (elem.kind == 'Resistor'):
                    R5 = d.add(e.RES, d='left', label=str(elem.value)+'$\Omega$', xy = l47.end)
                elif (elem.kind == 'Voltage Independent Source'):
                    S5 = d.add(e.SOURCE_V, d='left', label=str(elem.value)+'V', xy = l47.end)
                elif (elem.kind == 'Current Independent Source'):
                    S5 = d.add(e.SOURCE_I, d='left', label=str(elem.value)+'A', xy = l47.end)
                l47.color = 'none'
                if (elem.kind == 'Wire'):
                    l47.color = 'black'
            elif elem.position == '45':
                if (elem.kind == 'Resistor'):
                    R6 = d.add(e.RES, d='down', label=str(elem.value)+'$\Omega$', xy = l45.start)
                elif (elem.kind == 'Voltage Independent Source'):
                    S6 = d.add(e.SOURCE_V, d='down', label=str(elem.value)+'V', xy = l45.start)
                elif (elem.kind == 'Current Independent Source'):
                    S6 = d.add(e.SOURCE_I, d='down', label=str(elem.value)+'A', xy = l45.start)
                l45.color = 'none'
                if (elem.kind == 'Wire'):
                    l45.color = 'black'
            elif elem.position == '54':
                if (elem.kind == 'Resistor'):
                    R6 = d.add(e.RES, d='up', label=str(elem.value)+'$\Omega$', xy = l45.end)
                elif (elem.kind == 'Voltage Independent Source'):
                    S6 = d.add(e.SOURCE_V, d='up', label=str(elem.value)+'V', xy = l45.end)
                elif (elem.kind == 'Current Independent Source'):
                    S6 = d.add(e.SOURCE_I, d='up', label=str(elem.value)+'A', xy = l45.end)
                l45.color = 'none'
                if (elem.kind == 'Wire'):
                    l45.color = 'black'
            elif elem.position == '56':
                if (elem.kind == 'Resistor'):
                    R7 = d.add(e.RES, d='down', label=str(elem.value)+'$\Omega$', xy = l56.start)
                elif (elem.kind == 'Voltage Independent Source'):
                    S7 = d.add(e.SOURCE_V, d='down', label=str(elem.value)+'V', xy = l56.start)
                elif (elem.kind == 'Current Independent Source'):
                    S7 = d.add(e.SOURCE_I, d='down', label=str(elem.value)+'A', xy = l56.start)
                l56.color = 'none'
                if (elem.kind == 'Wire'):
                    l56.color = 'black'
            elif elem.position == '65':
                if (elem.kind == 'Resistor'):
                    R7 = d.add(e.RES, d='up', label=str(elem.value)+'$\Omega$', xy = l56.end)
                elif (elem.kind == 'Voltage Independent Source'):
                    S7 = d.add(e.SOURCE_V, d='up', label=str(elem.value)+'V', xy = l56.end)
                elif (elem.kind == 'Current Independent Source'):
                    S7 = d.add(e.SOURCE_I, d='up', label=str(elem.value)+'A', xy = l56.end)
                l56.color = 'none'
                if (elem.kind == 'Wire'):
                    l56.color = 'black'
            elif elem.position == '78':
                if (elem.kind == 'Resistor'):
                    R8 = d.add(e.RES, d='down', label=str(elem.value)+'$\Omega$', xy = l78.start)
                elif (elem.kind == 'Voltage Independent Source'):
                    S8 = d.add(e.SOURCE_V, d='down', label=str(elem.value)+'V', xy = l78.start)
                elif (elem.kind == 'Current Independent Source'):
                    S8 = d.add(e.SOURCE_I, d='down', label=str(elem.value)+'A', xy = l78.start)
                l78.color = 'none'
                if (elem.kind == 'Wire'):
                    l78.color = 'black'
            elif elem.position == '87':
                if (elem.kind == 'Resistor'):
                    R8 = d.add(e.RES, d='up', label=str(elem.value)+'$\Omega$', xy = l78.end)
                elif (elem.kind == 'Voltage Independent Source'):
                    S8 = d.add(e.SOURCE_V, d='up', label=str(elem.value)+'V', xy = l78.end)
                elif (elem.kind == 'Current Independent Source'):
                    S8 = d.add(e.SOURCE_I, d='up', label=str(elem.value)+'A', xy = l78.end)
                l78.color = 'none'
                if (elem.kind == 'Wire'):
                    l78.color = 'black'
            elif elem.position == '36':
                if (elem.kind == 'Resistor'):
                    R9 = d.add(e.RES, d='right', label=str(elem.value)+'$\Omega$', xy = l36.start)
                elif (elem.kind == 'Voltage Independent Source'):
                    S9 = d.add(e.SOURCE_V, d='right', label=str(elem.value)+'V', xy = l36.start)
                elif (elem.kind == 'Current Independent Source'):
                    S9 = d.add(e.SOURCE_I, d='right', label=str(elem.value)+'A', xy = l36.start)
                l36.color = 'none'
                if (elem.kind == 'Wire'):
                    l36.color = 'black'
            elif elem.position == '63':
                if (elem.kind == 'Resistor'):
                    R9 = d.add(e.RES, d='left', label=str(elem.value)+'$\Omega$', xy = l36.end)
                elif (elem.kind == 'Voltage Independent Source'):
                    S9 = d.add(e.SOURCE_V, d='left', label=str(elem.value)+'V', xy = l36.end)
                elif (elem.kind == 'Current Independent Source'):
                    S9 = d.add(e.SOURCE_I, d='left', label=str(elem.value)+'A', xy = l36.end)
                l36.color = 'none'
                if (elem.kind == 'Wire'):
                    l36.color = 'black'
            elif elem.position == '69':
                if (elem.kind == 'Resistor'):
                    R10 = d.add(e.RES, d='right', label=str(elem.value)+'$\Omega$', xy = l69.start)
                elif (elem.kind == 'Voltage Independent Source'):
                    S10 = d.add(e.SOURCE_V, d='right', label=str(elem.value)+'V', xy = l69.start)
                elif (elem.kind == 'Current Independent Source'):
                    S10 = d.add(e.SOURCE_I, d='right', label=str(elem.value)+'A', xy = l69.start)
                l69.color = 'none'
                if (elem.kind == 'Wire'):
                    l69.color = 'black'
            elif elem.position == '96':
                if (elem.kind == 'Resistor'):
                    R10 = d.add(e.RES, d='left', label=str(elem.value)+'$\Omega$', xy = l69.end)
                elif (elem.kind == 'Voltage Independent Source'):
                    S10 = d.add(e.SOURCE_V, d='left', label=str(elem.value)+'V', xy = l69.end)
                elif (elem.kind == 'Current Independent Source'):
                    S10 = d.add(e.SOURCE_I, d='left', label=str(elem.value)+'A', xy = l69.end)
                l69.color = 'none'
                if (elem.kind == 'Wire'):
                    l69.color = 'black'
            elif elem.position == '89':
                if (elem.kind == 'Resistor'):
                    R11 = d.add(e.RES, d='down', label=str(elem.value)+'$\Omega$', xy = l89.start)
                elif (elem.kind == 'Voltage Independent Source'):
                    S11 = d.add(e.SOURCE_V, d='down', label=str(elem.value)+'V', xy = l89.start)
                elif (elem.kind == 'Current Independent Source'):
                    S11 = d.add(e.SOURCE_I, d='down', label=str(elem.value)+'A', xy = l89.start)
                l89.color = 'none'
                if (elem.kind == 'Wire'):
                    l89.color = 'black'
            elif elem.position == '98':
                if (elem.kind == 'Resistor'):
                    R11 = d.add(e.RES, d='up', label=str(elem.value)+'$\Omega$', xy = l89.end)
                elif (elem.kind == 'Voltage Independent Source'):
                    S11 = d.add(e.SOURCE_V, d='up', label=str(elem.value)+'V', xy = l89.end)
                elif (elem.kind == 'Current Independent Source'):
                    S11 = d.add(e.SOURCE_I, d='up', label=str(elem.value)+'A', xy = l89.end)
                l89.color = 'none'
                if (elem.kind == 'Wire'):
                    l89.color = 'black'
            elif elem.position == '25':
                if (elem.kind == 'Resistor'):
                    R12 = d.add(e.RES, d='right', label=str(elem.value)+'$\Omega$', xy = l25.start)
                elif (elem.kind == 'Voltage Independent Source'):
                    S12 = d.add(e.SOURCE_V, d='right', label=str(elem.value)+'V', xy = l25.start)
                elif (elem.kind == 'Current Independent Source'):
                    S12 = d.add(e.SOURCE_I, d='right', label=str(elem.value)+'A', xy = l25.start)
                l25.color = 'none'
                if (elem.kind == 'Wire'):
                    l25.color = 'black'
            elif elem.position == '52':
                if (elem.kind == 'Resistor'):
                    R12 = d.add(e.RES, d='left', label=str(elem.value)+'$\Omega$', xy = l25.end)
                elif (elem.kind == 'Voltage Independent Source'):
                    S12 = d.add(e.SOURCE_V, d='left', label=str(elem.value)+'V', xy = l25.end)
                elif (elem.kind == 'Current Independent Source'):
                    S12 = d.add(e.SOURCE_I, d='left', label=str(elem.value)+'A', xy = l25.end)
                l25.color = 'none'
                if (elem.kind == 'Wire'):
                    l25.color = 'black'
        d.draw()



s = sympy.Symbol('s')

class circuit():
    def __init__(self):
        self.components = []
        self.subsDic = {}
        self.meas = {}
        self.sSolution = None
        self.solution = None
        self.particular = None
        self.name = {}
        self.symbol = {}

    def addR(self,name,node1,node2,value=None):
        sy = sympy.Symbol(name)

        dict = {}
        dict['k']  = 'r'
        dict['n']  = name
        dict['n1'] = node1
        dict['n2'] = node2
        dict['v']  = value
        dict['sy'] = sy

        self.components.append(dict)

        self.symbol[name] = sy

        if value != None:
            self.subsDic[sy] = value

        return sy

    def addV(self,name,node1,node2,value=None):
        sy = sympy.Symbol(name)

        dict = {}
        dict['k']  = 'vs'
        dict['n']  = name
        dict['n1'] = node1
        dict['n2'] = node2
        dict['v']  = value
        dict['sy'] = sy
        isy = sympy.Symbol('i'+name)
        dict['isy'] = isy
        self.name[isy] = 'i'+name

        self.symbol[name] = sy
        self.symbol['i'+name] = isy

        self.components.append(dict)

        if value != None:
            self.subsDic[sy] = value
        return sy

    def addI(self,name,node1,node2,value=None):
        sy = sympy.Symbol(name)

        dict = {}
        dict['k']  = 'is'
        dict['n']  = name
        dict['n1'] = node1
        dict['n2'] = node2
        dict['v']  = value
        dict['sy'] = sy

        self.components.append(dict)

        self.symbol[name] = sy

        if value != None:
            self.subsDic[sy] = value
        return sy
#define nodes
    def _numNodes(self):
        self.nodeList = set([])


        for component in self.components:
            self.nodeList.add(component['n1'])
            self.nodeList.add(component['n2'])

        self.nodeList = list(self.nodeList)

    def _nodeVariables(self):
        self.nodeVars = {}

        zeroFound = False
        for node in self.nodeList:
            if node == 0:
                zeroFound = True
            else:
                name = 'v'+str(node)
                ns = sympy.Symbol(name)
                self.nodeVars[node] = ns
                self.unknowns.add(ns)
                #print(ns)
                #print(name)
                self.name[ns] = name

                self.symbol[name] = ns

#calculate v on r
    def _addRtoNode(self,res,eq,node):
        n1 = res['n1']
        n2 = res['n2']
        if n1 == node:
            if n2 == 0:
                eq = eq - self.nodeVars[n1]/res['sy']
            else:
                eq = eq - (self.nodeVars[n1]-self.nodeVars[n2])/res['sy']
        if n2 == node:
            if n1 == 0:
                eq = eq - self.nodeVars[n2]/res['sy']
            else:
                eq = eq - (self.nodeVars[n2]-self.nodeVars[n1])/res['sy']
        return eq

    def _addVtoNode(self,vs,eq,node):
        n1 = vs['n1']
        n2 = vs['n2']
        if n1 == node:
            eq = eq - vs['isy']
        if n2 == node:
            eq = eq + vs['isy']
        return eq

    def _addItoNode(self,isr,eq,node):
        n1 = isr['n1']
        n2 = isr['n2']
        if n1 == node:
            eq = eq + isr['sy']
        if n2 == node:
            eq = eq - isr['sy']
        return eq
#calculate at current source

    def _addKCLequations(self):
        for node in self.nodeList:
            if node != 0:
                equation = sympy.Rational(0,1)
                for cm in self.components:
                    if cm['k'] == 'r':
                        equation = self._addRtoNode(cm,equation,node)
                    elif cm['k'] == 'vs' or cm['k'] == 'cvs':
                        equation = self._addVtoNode(cm,equation,node)
                    elif cm['k'] == 'is' or cm['k'] == 'cis':
                        equation = self._addItoNode(cm,equation,node)
                self.equations.append(equation)

    def _substEqs(self,oldS,newS):
        newList = []
        for eq in self.equations:
            newList.append(eq.subs(oldS,newS))
        self.equations = newList

    def _addVequations(self):

        for cm in self.components:
            if cm['k']=='vs' :

                self.unknowns.add(cm['isy'])
                n1 = cm['n1']
                n2 = cm['n2']
                if   n1 == 0:
                    self.equations.append(sympy.Eq(cm['sy'],self.nodeVars[n2]))
                elif n2 == 0:
                    self.equations.append(sympy.Eq(cm['sy'],self.nodeVars[n1]))
                else:
                    self.equations.append(sympy.Eq(cm['sy'],self.nodeVars[n2]-self.nodeVars[n1]))



    def _showEquations(self):
        print('Circuit equations:')
        for eq in self.equations:
            print('    ',eq)

#solve the equation
    def _solveEquations(self):
        self.sSolution = sympy.solve(self.equations,list(self.unknowns))

    def _nameSolution(self):
        self.solution = {}
        for sym in self.sSolution:
            key = self.name[sym]
            self.solution[key] = self.sSolution[sym]

    def _substituteSolution(self):
        self.particular = {}
        for key in self.solution:
            self.particular[key] = self.solution[key].subs(self.subsDic)

    def solve(self):

        self.equations  = []
        self.unknowns = set([])
        self._numNodes()
        self._nodeVariables()
        self._addKCLequations()
        self._addVequations()
        self._solveEquations()
        self._nameSolution()
        self._substituteSolution()
        return self.particular

    def subs(self):
        return self.particular

def expr2func(expr,*vars):
    return sympy.lambdify(vars,expr)

def evalList(expr,var,set):
    f = expr2func(expr,var)
    return np.array(f(np.array(set)))

if __name__ == "__main__":
    window = Tk()
    mywin = MyWindow(window)
    window.title('Circuit Analysis')
    window.geometry("530x550")
    window.mainloop()

























    elements = mywin.elements