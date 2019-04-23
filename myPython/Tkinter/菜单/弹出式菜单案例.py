import tkinter


def makelabel():
    global baseFrame
    lb = tkinter.Label(baseFrame, text="PHP是最好的语言，我用的是Python")
    lb.pack()


baseFrame = tkinter.Tk()

baseFrame.wm_title("弹出式菜单/上下文菜单 案例")

menubar = tkinter.Menu(baseFrame)
for x in ['麻辣香菇', '汽锅鸡', '东坡肘子']:
    menubar.add_separator()
    menubar.add_command(label=x)

menubar.add_command(label='重庆火锅', command=makelabel)
# 事件处理函数一定至少有一个参数，且第一个参数表示的是系统事件


def pop(event):
    # 注意使用event.x 和event.x_toot 的区别
    menubar.post(event.x_root, event.y_root)


baseFrame.bind("<Button-3>", pop)


baseFrame.mainloop()