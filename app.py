import tkinter as tk
from tkinter import messagebox
from trans import get_word_list
import random
# 单词列表
a=0
b=5
words_list = get_word_list(a,b)

word_count = 0 # 第几个词
word_current = ""

# 显示解释和词性


def get_word():
    global word_count
    global word_current
    words_len = len(words_list)

    if word_count < words_len:
        print(words_list[word_count])
        word_label.config(text= words_list[word_count]["word"])
        trans_label.config(text="")
        word_count += 1
    else:
        messagebox.showinfo("MicroWord", "Over,Reloading-*-*----*****----")
        word_count = 0


def show_definition():
    # try:
    if word_count==0:
        word_info = words_list[word_count]["translations"]
    word_info = words_list[word_count-1]["translations"]
    print(words_list[word_count-1])
    word_trans=""
    word_type=""
    for trans_type in word_info:
        word_trans+=trans_type["translation"]
        word_type+=trans_type["type"]
    trans_label.config(text=f"解释：{word_trans}\n词性：{word_type}")
    # except Exception:
        # messagebox.showerror("MicroWord", "Error--->-->->Boom!!!!")
def on_enter_key(event):
    get_word()
def on_space_key(event):
    show_definition()
def on_esc_key(event):
    window.destroy()
window = tk.Tk()
# 提示标签
word_label = tk.Label(window, text="", font=("Times New Roman", 24,"bold"),fg="black", bg="SlateGrey")
word_label.pack(pady=5)

# 解释标签
trans_label = tk.Label(window, text="", font=("SongTi", 15,"bold"),fg="black", bg="SlateGrey")
trans_label.pack(pady=10)

# 查看解释按钮
trans_button = tk.Button(window, text="查看解释", font=("Arial", 16), command=show_definition)
# trans_button.place(relx=0.3, rely=0.6, anchor=tk.CENTER)

# 下一个单词按钮
next_button = tk.Button(window, text="下一个单词", font=("Arial", 16), command=get_word)
# next_button.place(relx=0.7, rely=0.6, anchor=tk.CENTER)

# 关闭按钮
close_button = tk.Button(window, text="关闭", font=("Arial", 16), command=window.destroy)
# close_button.place(relx=1, rely=0, anchor=tk.NE)
# word_label.config(highlightthickness=0)
# trans_label.config(highlightthickness=0)
window.bind("<Return>",on_enter_key)
window.bind("<space>",on_space_key)
window.bind("<Escape>",on_esc_key)
# 默认可以随机挑选一个单词
word_label.config(text= words_list[random.randint(a,b)]["word"])
# 启动主循环
window.config(bg="SlateGrey")
window.title("")
window_width = 450
window_height = 250
window.overrideredirect(True)
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = screen_width - window_width
y = 0
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.wm_attributes("-transparentcolor","SlateGrey")
# window.attributes("-alpha", 0.2)
window.mainloop()
