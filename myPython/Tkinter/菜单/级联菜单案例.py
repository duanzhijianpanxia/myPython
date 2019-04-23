import tkinter

baseFrame = tkinter.Tk()
baseFrame.wm_title("级联菜单案例")

menubar = tkinter.Menu(baseFrame)

emenu = tkinter.Menu(menubar)
for item in ['Copy', 'Past', 'Cut']:
    emenu.add_command(label=item)

menubar.add_cascade(label='File')
menubar.add_cascade(label='Edit', menu=emenu)
menubar.add_cascade(label='Help')

baseFrame['menu'] = menubar

baseFrame.mainloop()