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

# 注文した内容@メインメニュー
order_list = []
order_price = []

# 処理開始
while True:
    user = input('メインメニューを選んでください>>>')
    if user == "" or user == "q" or user == "Q":
        print('キャンセルされました。またのご利用お待ちしております。')
        break

    elif user not in main_menu:
        print('選択されたメニューはありません。')
        continue
    else:
        order_list.append(user)
        order_price.append(main_menu[user])
    break

# 注文内容の結果表示
print('以下の内容で注文を承りました。')
print(order_list)
print(order_price)
print('右奥のカウンターにてお待ちくださいませ。')
#　メインメニューの選択、表示までは動作確認できたので、ひとまず提出します。
