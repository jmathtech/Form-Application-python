from tkinter import *

#Main Window - Form Application

master = Tk()
master.title('Form Application')

# Height and width

height = master.winfo_screenmmheight()
width = master.winfo_screenmmwidth()
master.geometry('350x450')
master.configure(background = 'silver')

# Entry - Form Application

Label(master, text = 'First Name').grid(row = 0)
Label(master, text = 'Last Name').grid(row = 1)
Label(master, text = 'Address').grid(row = 2)
Label(master, text = 'City').grid(row = 3)
Label(master, text = 'State').grid(row = 4)
Label(master, text = 'Country').grid(row = 5)
Label(master, text = 'Business Phone No.').grid(row = 6)
Label(master, text = 'Business Tax ID').grid(row = 7)
Label(master, text = 'Business Name').grid(row = 8)
Label(master, text = 'Date of Birth').grid(row = 9)
Label(master, text = 'Email').grid(row = 10)
Label(master, text = 'Course Material').grid(row = 11)
Label(master, text = 'Course Date').grid(row = 12)
Label(master, text = 'Data Map').grid(row = 13)
Label(master, text = 'Form Agreement').grid(row = 14)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)
e7 = Entry(master)
e8 = Entry(master)
e9 = Entry(master)
e10 = Entry(master)
e11 = Entry(master)
e12 = Entry(master)
e13 = Entry(master)
e14 = Entry(master)
e15 = Entry(master)
e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)
e3.grid(row = 2, column = 1)
e4.grid(row = 3, column = 1)
e5.grid(row = 4, column = 1)
e6.grid(row = 5, column = 1)
e7.grid(row = 6, column = 1)
e8.grid(row = 7, column = 1)
e9.grid(row = 8, column = 1)
e10.grid(row = 9, column = 1)
e11.grid(row = 10, column = 1)
e12.grid(row = 11, column = 1)
e13.grid(row = 12, column = 1)
e14.grid(row = 13, column = 1)
e15.grid(row = 14, column = 1)

# Submit Button - Form

submit = Button(master, text='Submit', fg='White', bg='Red')
submit.grid(row=16, column=1)
 
# Menu - Form Application

menu = Menu(master)
master.config(menu = menu)
filemenu = Menu(menu)
menu.add_cascade(label = 'File', menu = filemenu)
filemenu.add_command(label = 'New')
filemenu.add_command(label = 'Open')
filemenu.add_separator()
filemenu.add_command(label = 'Exit', command = master.destroy)
helpmenu = Menu(menu)
menu.add_cascade(label = 'Help', menu = helpmenu)
filemenu.add_separator()
helpmenu.add_command(label = 'About')
helpmenu.add_command(label = 'License')
mainloop()

# Exit the Application

master.destroy()
