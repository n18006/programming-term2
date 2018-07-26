# メインメニューの商品名と価格の設定
main_menu = {'DripCoffee': 280,
             'ColdBrewCoffee': 320,
             'CafeLatte': 330,
             'SoyLatte': 380,
             'Cappuccino': 330,
             'CaramelFrappuccino': 470,
             'MacchaCreamFrappuccino': 470}

# オプションメニューの商品名と価格の設定
option_menu = {'LowFatMilk': 0,
               'NonFatMilk': 0,
               'SoyMilk': 50,
               'DeepCoffee': 60,
               'WhipCream': 70,
               'CaramelShrup': 60,
               'ChocoSource': 0,
               'DeCafe': 50}

# 注文した内容
order_list = []
order_price = []
# ループを抜けるスイッチ
cto = True #cod >> Continue to order の略
# 処理開始
while cto: #main_menuの注文
    input_val = input("メインメニューを選んでください>>>")
    if input_val == "" or input_val == "q":
        print("注文をキャンセルいたします")
        break
    elif input_val not in main_menu:
        print("選択されたメニューはありません")
        continue
    elif input_val in main_menu:
        order_list.append(input_val)
        order_price.append(main_menu[input_val])
        print("メインメニューを承りました")
        cto = False
        input_val = input("オプションメニューを選んでください>>>") #option_menuの注文
        while True:
            if input_val in option_menu:
                order_list.append(input_val)
                order_price.append(option_menu[input_val])
                input_val = input("他にオプションメニューの注文はございますか？>>>")
            elif input_val == "" or input_val == "q":
                break
                cto = False
    # 注文内容の確認
    print("注文内容は" ,order_list, "です")
    sum_v = sum(order_price) #合計金額の計算
    print("合計金額は", sum_v, "円です。右奥のカウンターにてお待ち下さい。")
