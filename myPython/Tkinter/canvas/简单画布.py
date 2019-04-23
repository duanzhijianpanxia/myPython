import tkinter


baseFrame = tkinter.Tk()

baseFrame.wm_title("简单的画布")

cav = tkinter.Canvas(baseFrame, width=300, height=200)
cav.pack()

cav.create_line((33, 33), (98, 100))
cav.create_text(99,177, text="I love Wang Xiaomei")

baseFrame.mainloop()