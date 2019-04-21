import tkinter

# 模拟的是登录函数
def reg():
    # 从相应的输入框中获取用户输入
    name = e1.get()
    pwd = e2.get()

    t1 = len(name)
    t2 = len(pwd)

    if name == "1111" and pwd == "2222":
        # 需要理解西面代码的含义
        lb3["text"] = "登录成功"
    else:
        lb3['text'] = "用户名或密码错误"
        # 输入框删除用户输入的内容
        # 注意delete的两个参数，表示删除从第几个开始到第几个结束
        e1.delete(0, t1)
        e2.delete(0, t2)

# 启动舞台
baseFrame = tkinter.Tk()
baseFrame.wm_title("输入框案例")

lb1 = tkinter.Label(baseFrame, text="用户名")
lb1.grid(row=0, column=0, sticky=tkinter.W)

e1 = tkinter.Entry(baseFrame)
e1.grid(row=0, column=1, sticky=tkinter.E)

lb2 = tkinter.Label(baseFrame, text="密码")
lb2.grid(row=1,column=0, sticky=tkinter.W)

e2 = tkinter.Entry(baseFrame)
e2.grid(row=1, column=1, sticky=tkinter.E)
e2['show'] = '*'

# button参数command的意思是，当按钮被点击后启动相应的处理函数
btn = tkinter.Button(baseFrame, text="登录", foreground="green", background="gray", command=reg)
btn.grid(row=2, column=1,sticky=tkinter.E)

lb3 = tkinter.Label(baseFrame, text="")
lb3.grid(row=3, column=0, sticky=tkinter.W)

# 启动主Frame
baseFrame.mainloop()