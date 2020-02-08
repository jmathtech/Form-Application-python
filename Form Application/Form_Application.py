import tkinter
from tkinter import *

# Form Application
master = Tk()

# Height and width
height = master.winfo_screenmmheight()
width = master.winfo_screenmmwidth()

# Entry - Form Application
Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=1)
Label(master, text='Address').grid(row=2)
Label(master, text='Phone Number').grid(row=3)
Label(master, text='Email').grid(row=4)
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)

# Menu - Form Application
menu = Menu(master)
master.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=master.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
mainloop()

# Exit the Application
master.destroy()