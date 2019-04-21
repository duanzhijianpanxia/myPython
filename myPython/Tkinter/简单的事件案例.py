import tkinter
# 这里定义了一个简单函数，作用是在GUI框架内显示"谢谢点击"
def basebutton(event):
    global baseFrame
    lb = tkinter.Label(text="谢谢点击")
    lb.pack()


# 画出程序总框架
baseFrame = tkinter.Tk()
baseFrame.wm_title("简单事件案例")

btn = tkinter.Button(baseFrame, text="just test",background="yellow", foreground="black")
# button/label绑定相应的消息和处理函数
# 自动获取鼠标左键点击就，并启动相应的处理函数basebutton
btn.bind("<Button-1>", basebutton)
btn.pack()

# 启动消息循环
# 到此，表示程序开始运行
baseFrame.mainloop()