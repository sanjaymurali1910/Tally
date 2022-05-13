from tkinter import *
import tkinter as tk
from tkinter import messagebox
#from PIL import Image,ImageTk
from tkinter.ttk import Combobox

from tkinter import ttk


def account():
    global Canvas1
    Canvas1 = tk.Canvas( background="#B0B0B0", insertbackground="black", relief="ridge",
                                selectbackground="blue", selectforeground="white")
    Canvas1.place(relx=0.150, rely=0.100, relheight=0.8, relwidth=0.350)

    global Canvas2
    Canvas2 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="black", relief="ridge",
                            selectbackground="blue", selectforeground="white")
    Canvas2.place(relx=0.550, rely=0.100, relheight=0.8, relwidth=0.350)

    global Canvas3
    Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",
                                selectbackground="blue", selectforeground="white")
    Canvas3.place(relx=0.850, rely=0.100, relheight=0.8, relwidth=0.150)

    




global screen
screen=Tk()
w=screen.winfo_screenwidth()
h=screen.winfo_screenheight()
screen.geometry("%dx%d" %(w,h))
        
screen.title("Tally")
# p1 = PhotoImage(file='D:\\Tally\\front.jpg')
# screen.iconphoto(True, p1)
screen.configure(background="#848884")
screen.configure(cursor="arrow")
          

sbmibtn=Button(screen,text='P:Print',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=850,y=10)
sbmibtn=Button(screen,text='F2:Date',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=990,y=10)
sbmibtn=Button(screen,text='F3:Company',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=1130,y=10)


global Canvas1
Canvas1 = tk.Canvas(background="#ffffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
Canvas1.place(relx=0, rely=0.07, relheight=0.9, relwidth=0.400)



global Canvas2
Canvas2 = tk.Canvas(background="#ffffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
Canvas2.place(relx=0.400, rely=0.07, relheight=0.9, relwidth=0.450)


global Canvas3
Canvas3 = tk.Canvas(background="#99CCFF", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
Canvas3.place(relx=0.850, rely=0.07, relheight=0.9, relwidth=0.150)
screen.mainloop()