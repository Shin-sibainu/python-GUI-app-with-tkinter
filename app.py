import tkinter as tk
from tkinter import Pack, filedialog, Text
import os
import pathlib

root = tk.Tk()
apps = []

# save.txtがあれば、そこに追加していく
if os.path.isfile("save.txt"):
    with open("save.txt", "r") as f:
        # 開いたファイル全体を文字列として取得する
        tempApps = f.read()
        # print(type(tempApps))
        # ,のあるところでアプリを区切る。
        tempApps = tempApps.split(",")
        print(tempApps)
        apps = [x for x in tempApps if x.strip()]  # 自動で両端の空白を削除
        print(apps)


# ボタンを押したときにエクスプローラーを開く、そして追加。
def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("exexutables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

# ファイルを起動


def runApps():
    for app in apps:
        os.startfile(app)

# ファイルを全て削除


def deleteAllApps():
    apps.clear()
    with open("save.txt", "r+") as f:
        f.truncate(0)
    for widget in frame.winfo_children():
        widget.destroy()


canvas = tk.Canvas(width=700, height=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10,
                    pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()

deleteApps = tk.Button(root, text="Delete Apps", padx=10,
                       pady=5, fg="white", bg="#263D42", command=deleteAllApps)
deleteApps.pack()


for app in apps:
    label = tk.Label(frame, text=app, bg="gray")
    label.pack()

root.mainloop()

with open("save.txt", "w") as f:
    for app in apps:
        f.write(app + ",")
