import tkinter


window = tkinter.Tk()

window.geometry('800x500')

# frame是一个容器
frame1 = tkinter.Frame(window, width=800, height=300, background="red")
frame2 = tkinter.Frame(window, width=800, height=300, background="#FF0FFF")




frame1.pack()
frame2.pack()
window.mainloop()
