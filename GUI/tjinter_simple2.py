from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Simple 2")
root.geometry("800x800")
def click_btn():
    messagebox.showwarning("","VASYA PRIVET")
for r in range(20):
    for c in range(20):
        btn = Button(text=f"{r:02.0f}_{c}", command=click_btn)
        btn.grid(row=r, column=c)

root.mainloop()
