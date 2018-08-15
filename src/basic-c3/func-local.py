# 関数の外側でVALUEに100を代入
value = 100

def changevalue():
    # 関数の内側でVALUEを変更
    value = 20

changevalue()
print("value=",value)#<===はたしてこの値は？
