from tkinter import *
from tkinter import messagebox
import tkinter;
master = tkinter.Tk();

master.title("Wish Form");
master.geometry("300x200");

Label (master , text = "Enter Name:").grid(row=0);
e1=Entry(master);
e1.grid(row=0, column=1);

def wish_click():
    messagebox.showinfo("Message Title", "Welcome " + e1.get());

def clear_click():
    e1.delete(0,"end");
    messagebox.showinfo("Message Title", "Text box cleared !");

b1=Button(master, text="Wish", fg="red", command=wish_click);
b2=Button(master, text="Clear", fg="blue", command=clear_click);

b1.grid(row=2, column=0);
b2.grid(row=2, column=1);

master.mainloop();
