#スーパの割引計算

def calcvalue(who, hour, count, value):
    '''あるスーパーの割引を計算する関数'''

    info = "割引なし"

    #１４時に商品を３つ以上で１割引
    if (hour == 14) and (count >= 3):
        value *= 0,9
        info = '１割引'

    # １５時に商品５つ以上で二割引き
    elif (hour == 15) and (count >= 5):
        value *= 0.8
        info = '二割引'

    # 結果を表示
    value = int(value)
    print("{0}さんは{1}={2}円".format(who, info, value))

#a/b/cさん、それぞれの支払い金額を求める
calcvalue("a", 15, 3, 1200)
calcvalue("b", 14, 5, 2000)
calcvalue("c", 15, 8, 5400)
