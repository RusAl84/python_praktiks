from tkinter import *

root = Tk()
root.title("Первая графическая программа на Python")
# root.geometry("800x300")
count = 0
def btn_click():
    global count
    count += 1
    root.title(f"{count}")

btn = Button(text="Нажми на меня",
             background="#005500",
             foreground="#FFFFFF",
             padx="10",
             pady="20",
             font="20",
             command=btn_click)

btn.pack()

root.geometry("800x300+300+200")
root.mainloop()


