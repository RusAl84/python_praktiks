from tkinter import *

root = Tk()
root.title("Первая графическая программа на Python")
# root.geometry("800x300")

def btn_click():
    count_clicks.set(count_clicks.get()+ 1)


count_clicks=IntVar
count_clicks.set(0)

btn = Button(textvariable=count_clicks,
             background="#005500",
             foreground="#FFFFFF",
             padx="10",
             pady="20",
             font="20",
             command=btn_click)

btn.pack()

root.geometry("800x300+300+200")
root.mainloop()


