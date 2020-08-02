import tkinter as tk
from tkinter import *
from tkinter import Menu , messagebox , ttk ,filedialog

import os
import subprocess


N_C_methods = ['integral']
E_S_methods = ['Diode rectifiers' , 'Controlled rectifier' , 'DC/AC Converters']
integral_method_items = ['Simpsone' , 'Trapezoid' , 'Gaussian 2' , 'Gaussian 3' , 'Middle point' , 'Newton Katsen' , 'Rectangular']
Engineering_Mathematics_items = ['Fourier Coefficients' , 'Fourier Transform' ]
Electronic_sanati_Diode_rectifiers_items = ['HWR_with_Resistive_load' , 'HWR_with_Resistive_Inductive_load' , 'HWR_with_RL_source_load' ]
Font = 10
class APPlication(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        master.geometry('720x480')
        master.title("Electrical Calculator" )
        master.resizable(width=True , height=True)
        master.config(bg='#81b3a6')
        self.Menubar(master)
        icon = PhotoImage(file ='D:\Electrical_app\App icon.png')
        master.tk.call('wm', 'iconphoto', master._w, icon)
        self.opening_page(master)





    def Menubar (self , master = None):
        menubar = tk.Menu(master)
        #menubar.config(bg='red')
        self.File_menubar(menubar , master)
        self.Help_menubar(menubar)
        self.View_menubar(menubar)
        self.master.config(menu=menubar)
        return 0
    def File_menubar(self , menubar = None , master = None):
        self.row = 0
        self.column = 0
        self.filemenu = tk.Menu(menubar , tearoff = 0)
        self.Lessons = tk.Menu(menubar, tearoff=0)
        self.Engineering_Mathematics_items = tk.Menu(menubar, tearoff=0)
        self.Numerical_calculations = tk.Menu(menubar, tearoff=0)
        self.Electronic_sanati = tk.Menu(menubar, tearoff=0)
        self.item_selected_val = IntVar()

        self.filemenu.add_cascade(label="Lessons", menu=self.Lessons )

        self.Lessons.add_cascade(label="Engineering Mathematics" , font = ("TimesNewRoman" , Font ) , menu=self.Engineering_Mathematics_items  )
        self.M_E_cascode()

        self.Lessons.add_cascade(label="Electronic sanati :" , font = ("TimesNewRoman" , Font ) , menu=self.Electronic_sanati )
        self.E_S_cascode()

        self.Lessons.add_cascade(label="Numerical calculations", font = ("TimesNewRoman" , Font ) , menu=self.Numerical_calculations)
        self.N_C_cascode()

        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.massage_box)
        menubar.add_cascade(label="File", menu=self.filemenu)
    def Help_menubar(self , menubar = None):
        self.Help_menu = tk.Menu(menubar , tearoff = 0)
        self.Help_menu.add_command(label="About" , command=lambda: self.callback(1))
        menubar.add_cascade(label="Help", menu=self.Help_menu)
        return 0
    def View_menubar(self , menubar = None):
        self.View_menu = tk.Menu(menubar , tearoff = 0)
        self.View_menu.add_command(label="Edit app font size" , command=lambda: self.callback('edit_font_size'))
        menubar.add_cascade(label="View", menu=self.View_menu)

    def M_E_cascode(self):
        self.Engineering_Mathematics_items.add_command(label = Engineering_Mathematics_items[0] , command=lambda: self.callback(1) )#lambda :self.callback_selected_item(self.row , self.column))
        self.Engineering_Mathematics_items.add_command(label = Engineering_Mathematics_items[1] , command=lambda: self.callback(2) )#lambda :self.callback_selected_item(self.row , self.column))
    def E_S_cascode(self):
        self.Electronic_sanati.add_command(label=E_S_methods[0], command=lambda: self.callback(3))
        self.Electronic_sanati.add_command(label=E_S_methods[1], command=lambda: self.callback(4))
        self.Electronic_sanati.add_command(label=E_S_methods[2], command=lambda: self.callback(5))
    def N_C_cascode(self):
        self.Numerical_calculations.add_command(label=N_C_methods[0], command=lambda: self.callback('integral'))
    def E_M1_cascode(self):
        pass

    def opening_page(self , master = None):
        self.lab1 = Label(master, text="Hi every body. I am here to solve your questions", fg='blue', bg='#81b3a6', font="TimesNewRoman").pack()

    def Integral_item_response(self , master = None):
        self.math_function = tk.StringVar()
        self.First_interval = tk.IntVar()
        self.Second_interval = tk.IntVar()
        frame = Frame(master)
        frame.pack()
        frame2 = Frame(master)
        frame2.pack()
        frame3 = Frame(master)
        frame3.pack()
        frame4 = Frame(master)
        frame4.pack()
        frame6 = Frame(master)
        frame6.pack()

        self.lab1 = Label(frame, text="integral solver", fg='blue', bg='#81b3a6' , font = "TimesNewRoman" )
        self.lab1.pack(side=TOP)

        self.lab2 = Label(frame2, text="enter your math function : ", fg='blue', bg='#81b3a6' , font = "TimesNewRoman")#.pack(pady=6, padx=3)
        self.lab2.pack(side=LEFT)

        self.Entry_function = ttk.Entry(frame2 , textvariable = self.math_function )
        self.Entry_function.pack(side=LEFT)

        self.lab3 = Label(frame3, text="Method : ", fg='blue', bg='#81b3a6' , font = "TimesNewRoman" )
        self.lab3.pack(side = LEFT)

        self.Combobox(frame3 , integral_method_items)

        self.lab4 = Label(frame3, text="Interval : ", fg='blue', bg='#81b3a6' , font = "TimesNewRoman" )
        self.lab4.pack(side = LEFT)

        self.First_number = ttk.Entry(frame3 , width = 5 , textvariable = self.First_interval )
        self.First_number.pack(side = LEFT)

        self.lab5 = Label(frame3, text="To : ", fg='blue', bg='#81b3a6', font="TimesNewRoman")
        self.lab5.pack(side = LEFT)

        self.Second_number= ttk.Entry(frame3 , width = 5 , textvariable = self.Second_interval )
        self.Second_number.pack(side = LEFT)
        #solving
        self.solve_by = Button(frame4 , text="solve" , fg='black' , bg ='white' , width = 100 , height = 1 , activebackground = 'green' , font = ("TimesNewRoman" , 8), command = self.checking_items_and_solving_integral )
        self.solve_by.pack(side = LEFT)
        self.showing_answer(self.master , 0)
        #self.definition_box(frame6)
    def checking_items_and_solving_integral(self):
        import integral
        i = integral.numeric_itegral()
        self.integral_answer = 0
        math_func = self.math_function.get()
        integral_method = self.combo_box.get()
        first_interval = self.First_interval.get()
        second_interval = self.Second_interval.get()

        if self.combo_box.get() == 'Simpsone' :
            self.integral_answer = i.Simpsone(self.math_function.get() , self.First_interval.get() , self.Second_interval.get())
        elif self.combo_box.get() == 'Trapezoid':
            self.integral_answer = i.Trapezoid(self.math_function.get(), self.First_interval.get(), self.Second_interval.get())
        elif self.combo_box.get() == 'Gaussian_2point':
            self.integral_answer = i.Gaussian_2point(self.math_function.get(), self.First_interval.get(), self.Second_interval.get())
        elif self.combo_box.get() == 'Gaussian_3point':
            self.integral_answer = i.Gaussian_3point(self.math_function.get(), self.First_interval.get(), self.Second_interval.get())
        elif self.combo_box.get() == 'Middle_point':
            self.integral_answer = i.Middle_point(self.math_function.get(), self.First_interval.get(), self.Second_interval.get())
        elif self.combo_box.get() == 'Newton_Katsen':
            self.integral_answer = i.Newton_Katsen(self.math_function.get(), self.First_interval.get(), self.Second_interval.get())
        elif self.combo_box.get() == 'Rectangular':
            self.integral_answer = i.Rectangular(self.math_function.get(), self.First_interval.get(), self.Second_interval.get())
        self.showing_answer(self.master , self.integral_answer)
        print(self.integral_answer)


    def open_help_file(self):
        File = "D:\Electrical_app\Help.pdf"
        os.system(File)
    def callback(self , var):
        self.a = []
        if var == 1 :
            self.open_help_file()
        elif var == 20:
            print("@")
        elif var == 'integral':
            self.Integral_item_response(self.master )
        #elif var == 'edit_font_size' :
            #new_page = tk.Tk()
            #new_page.geometry('350x350')
            #new_page.title("Editor")
            #new_page.resizable(width=False, height=False)
            #new_page.config(bg='white')
            #lab1 = Label(new_page ,text =  "click ok").pack()
            #self.font_size = 20
            #Font = self.font_size
            #OK_Button = Button(text = 'OK' , command = self.Editor_change(new_page)).pack()

            #new_page.mainloop()
            #new_page.destroy()

    def Editor_change(self , master = None):
        self.font_size = 20
        if self.font_size != 0 :
            Font = self.font_size
        master.destroy()


    def massage_box(self , Error = "Exit"):
        if Error == "Exit" :
            response = messagebox.askyesno("Exit", "Do you want to exit !!!")
            if response == True:
                self.master.destroy()
            elif response == False :
                pass
        return 0
    def Combobox(self , master = None , list = None , X = 100 , Y = 100):
        from tkinter import ttk
        self.integral_method = StringVar()
        self.combo_box = ttk.Combobox(master , width = 25 ,textvariable = self.integral_method , state = 'readonly' , values = list , font = ("TimesNewRoman" , 8) )
        self.combo_box.pack(side = LEFT)
        self.combo_box.current(0)
        print(self.integral_method.get())
        self.selected_item_bar = self.combo_box.get()
    def showing_answer(self , master = None , answer = 0):
        self.lab1 = Label(master , text="Answer :", fg='blue', bg='#81b3a6', font="TimesNewRoman").pack(side = LEFT)
        self.text_box = Text(master , height = 1 , width = 10)
        self.text_box.insert(INSERT , answer)
        self.text_box.pack(side = LEFT)
    def definition_box(self , master = None):
        self.lab1 = Label(master, text="Definition :", fg='blue', bg='#81b3a6', font="TimesNewRoman")
        self.lab1.pack(side = LEFT)
        self.text_box = Text(master, height=5, width=100)
        self.text_box.insert(INSERT, "hello")
        self.text_box.pack(side = LEFT)



