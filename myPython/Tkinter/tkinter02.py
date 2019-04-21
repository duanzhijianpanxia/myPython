import tkinter

base = tkinter.Tk()
base.wm_title("Just have a try")

lb1 = tkinter.Label(base, text = "Just have a try also")
lb1.pack()

lb2 = tkinter.Label(base, text = "hello world", background = "red")
lb2.pack()

lb3 = tkinter.Label(base, text = "Just so so.", background = "yellow")
lb3.pack()

tkinter.mainloop()