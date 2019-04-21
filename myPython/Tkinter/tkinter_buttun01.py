import tkinter

def showlabel():
    global baseFrame
    # 在函数中创建了一个label
    # label的父组件是baseFrame
    lb = tkinter.Label(baseFrame, text = "显示label", background = "yellow")
    lb.pack()

baseFrame = tkinter.Tk()
# 生成一个button,
# command参数的意义在于按下button后该执行什么函数或者命令
# 如果没有command参数的话，所生成的button是一个死的button，除了会动之外没有任何的执行结果，参见下面的#注释

bt = tkinter.Button(baseFrame, text = "show Label", command = showlabel)
# bt = tkinter.Button(baseFrame, text = "show Label")
bt.pack()

tkinter.mainloop()

