from tkinter import *
from tkinter import messagebox
import tkinter
master = tkinter.Tk();

master.title("First Form");
master.geometry("400x400");
#master.pack(padx=20, pady=20);

Label (master , text = "Enter Name:").grid(row=0);
Label (master , text = "Enter Salary:").grid(row=1);
e1=Entry(master);
e2=Entry(master);
e1.grid(row=0, column=1);
e2.grid(row=1, column=1);


def save_click():
    s=e1.get()+","+e2.get()+"\n";
    f=open("user.txt",'a');
    #s=input(e1.get()+","+e2.get());
    f.write(s);
    f.close();
    messagebox.showinfo("Save Window", "Data Saved " );
    clear_click();

def clear_click():
    e1.delete(0,"end");
    e2.delete(0,"end");
    messagebox.showinfo("Message Title", "Data cleared !");

b1=Button(master, text="Save", fg="green", command=save_click);
b2=Button(master, text="Clear", fg="red", command=clear_click);

b1.grid(row=2, column=0);
b2.grid(row=2, column=1);

master.mainloop();
