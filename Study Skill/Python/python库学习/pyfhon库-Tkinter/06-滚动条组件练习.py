import tkinter as tk

root = tk.Tk()
root.title("滚动条练习4 - 可视化")
root.geometry("500x400")

# 1. 主容器 - 黄色边框
container = tk.Frame(root, bg="yellow", bd=2)
container.pack(fill="both", expand=True, padx=20, pady=20)

# 2. Canvas - 蓝色背景
canvas = tk.Canvas(container, bg="lightblue", highlightthickness=1, highlightbackground="blue")
canvas.pack(side="left", fill="both", expand=True)

# 3. 滚动条 - 红色
scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# 画布绑定滚动条
canvas.configure(yscrollcommand=scrollbar.set)

# 4. 内部Frame - 绿色背景
inner_frame = tk.Frame(canvas, bg="lightgreen")
canvas_window = canvas.create_window((0, 0), window=inner_frame, anchor="nw")

# 5. 添加标签，带序号
for i in range(25):
    # 奇数行和偶数行用不同颜色
    color = "#e0f7e0" if i % 2 == 0 else "#c0e7c0"
    frame = tk.Frame(inner_frame, bg=color, height=30)
    frame.pack(fill="x", pady=1)

    label = tk.Label(frame, text=f"第 {i + 1:02d} 行 - 这是示例内容",
                     bg=color, font=("Arial", 11), anchor="w")
    label.pack(side="left", padx=10)

    # 添加一个按钮，证明里面可以放任何组件
    button = tk.Button(frame, text="点击")
    button.pack(side="right", padx=10)

# 6. 信息标签
info_label = tk.Label(root, text="黄色:容器 | 蓝色:Canvas | 绿色:内部Frame | 红色:滚动条",
                      font=("Arial", 10), bg="white")
info_label.pack(side="bottom", pady=5)


# 7. 绑定事件
def update_all():
    inner_frame.update_idletasks()  # 强制立即处理闲时任务
    canvas.configure(scrollregion=canvas.bbox("all"))
    canvas.itemconfig(canvas_window, width=canvas.winfo_width())


inner_frame.bind("<Configure>", lambda e: update_all())
canvas.bind("<Configure>", lambda e: update_all())

root.mainloop()
