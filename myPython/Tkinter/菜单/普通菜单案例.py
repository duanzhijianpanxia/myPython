import tkinter

baseFrame = tkinter.Tk()
baseFrame.wm_title("普通菜单案例")

menubar = tkinter.Menu(baseFrame)

for item in ["File", "Edit", "View", "Help"]:
    menubar.add_command(label=item)

baseFrame['menu'] = menubar

baseFrame.mainloop()