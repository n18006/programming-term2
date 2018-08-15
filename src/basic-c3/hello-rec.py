# 再帰関数を定義
def say_hello(i):
   '''
   「ハロー」を指定した回数出力する

   parameters
   ----------
   i : int
       回数

    returns
    -------
    なし
    ----
    '''

    if i <= 0: return #Iが０になったらreturn
    print("ハロー", i)
    say_hello(i-1) #say_helloを呼び出す

#実行
say_hello(10)
