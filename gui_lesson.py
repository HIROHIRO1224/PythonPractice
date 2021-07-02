from tkinter import *
from tkinter import ttk

root = Tk()
root.title('My First App')

# ウィジェットの作成
frame1 = ttk.Frame(root, padding=16)
label1 = ttk.Label(frame1, text='画面から顔が外れたため、カメラとマイクをオフにしました')
button1 = ttk.Button(
    frame1,
    text='元に戻す',
)

# レイアウト
frame1.pack()
label1.pack(anchor=CENTER)
button1.pack(anchor=SE,side=RIGHT)

# ウィンドウの表示開始
root.mainloop()