import sys
import tkinter

# メインウインドウの作成
root = tkinter.Tk()

# メインウインドウのタイトルを変更
root.title("Tkinter test")

# メインウインドウを640*480にする
root.geometry("1020x720")

# ステータスバーの設定
status = tkinter.Label(root, text="練習", borderwidth=2, relief="groove")
status.pack(side=tkinter.BOTTOM, fill=tkinter.X)


# メイン
root.mainloop()
