from tkinter import *


def btnClick():
    textLabel['text'] = '我点击了按钮'


root = Tk(className="测试打包");

textLabel = Label(root, text='提示显示', justify=LEFT, padx=10)
textLabel.pack(side=TOP)

btn = Button(root)
btn['text'] = '点击测试'
btn['command'] = btnClick
btn.pack(side=BOTTOM)

mainloop()
