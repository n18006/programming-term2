# 関数の外側でVALUEに100を代入
value = 100

def changevalue():
    #valueをグローバル宣言
    global value
    # 関数の内側でvalueを変更
    value = 20

changevalue()
print("value=",value)
