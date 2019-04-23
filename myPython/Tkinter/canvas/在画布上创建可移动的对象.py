import tkinter

baseFrame = tkinter.Tk()
baseFrame.wm_title("画布上的可移动对象案例")

def btnclick(event):
    global cv
    cv.move(id_ball, 11, 3)
    cv.move('fall', 11, 7)


cv = tkinter.Canvas(baseFrame, width=500, height=300, background="gray")
cv.pack()
cv.bind("<Button-1>", btnclick)


# 创建组件后返回ID
# 正方形是特殊的矩形，正圆是特殊的椭圆
id_ball = cv.create_oval(30, 30, 50, 50, fill="yellow")

# 创建组件使用tag属性
cv.create_text((123, 55), text="I love Wang Xiaomei", tag='fall')
# 创建的时候如果没有指定tag可以利用addtag_withtag添加
# 同类函数还有addtag_all, addtag_above, addtag_xxx等等
id_rectangle = cv.create_rectangle(78, 45, 121, 131, fill="purple")
cv.addtag_withtag('fall', id_rectangle)


baseFrame.mainloop()
