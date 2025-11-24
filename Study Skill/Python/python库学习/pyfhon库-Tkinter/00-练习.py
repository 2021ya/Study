import tkinter
from tkinter import messagebox


window = tkinter.Tk()


window_local = window.maxsize()

window.title("练习")

window.iconbitmap(r"./images/16x16.ico")

window.attributes("-topmost", True)

window.geometry("{}x{}+{}+{}".format(int(window_local[0]/2), int(window_local[1]/2), int(window_local[0]/4), int(window_local[1]/4)))

window.resizable(False, False)

window.configure(background="white")

window.attributes("-alpha", 1)

account_label = tkinter.Label(window, text="account:", background="white", font=("黑体", 24))
password_label = tkinter.Label(window, text="password:", background="white", font=("黑体", 24))

account_label.place(x=150, y=150, width=150, height=50)
password_label.place(x=150, y=220, width=150, height=50)

account_enter_result = tkinter.StringVar()
password_enter_result = tkinter.StringVar()

account_enter_result.set("account")
password_enter_result.set("password")

account_entry_label = tkinter.Entry(window, textvariable=account_enter_result, font=("黑体", 24))
password_entry_label = tkinter.Entry(window, textvariable=password_enter_result, font=("黑体", 24))

account_entry_label.place(x=310, y=153, width=250, height=45)
password_entry_label.place(x=310, y=223, width=250, height=45)


def button_chink():
    if account_enter_result.get() == "123":
        messagebox.showinfo(title="info", message="登录成功！")
    else:
        messagebox.showwarning(title="登录失败", message="账号或密码错误！")
        pop_up = messagebox.askretrycancel(title="选择", message="是否重试")
        if pop_up:
            print("yes")
        elif not pop_up:
            print("no")


button_login = tkinter.Button(text="Login", command=button_chink)

button_login.place(x=250, y=350, width=150, height=50)

window.mainloop()
