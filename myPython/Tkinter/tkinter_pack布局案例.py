# pack 布局案例
import tkinter #导入Tkinter

base = tkinter.Tk() # 创建布局框
base.wm_title("pack布局案例") # 设置标题

btn1 = tkinter.Button(base, text="a",background="yellow", foreground="red")
btn1.pack(side=tkinter.LEFT, expand=tkinter.YES, fill=tkinter.Y)

btn2 = tkinter.Button(base, text="b")
btn2.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.BOTH)

btn3 = tkinter.Button(base, text="c")
btn3.pack(side=tkinter.RIGHT, expand=tkinter.YES, fill = tkinter.X)

btn4 = tkinter.Button(base, text="d", foreground="green", background="orange")
btn4.pack(side=tkinter.LEFT, expand=tkinter.YES, fill=tkinter.BOTH)

btn5 = tkinter.Button(base, text="e")
btn5.pack(side=tkinter.TOP)

btn6 = tkinter.Button(base, text="f")
btn6.pack(side=tkinter.BOTTOM, expand=tkinter.NO, fill=tkinter.X)

btn7=tkinter.Button(base, text="g", foreground="purple", background="white")
btn7.pack(side=tkinter.TOP, anchor=tkinter.SE)

base.mainloop()