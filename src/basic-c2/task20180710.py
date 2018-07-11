#  自分が絶対に勝てないじゃんけんプログラム

print('私とじゃんけんをしよう。あなたは絶対私に勝つことはできない。')
user = int(input('何を出しますか? 数値を入力してね！ 1:グー、2:チョキ、3:パー>>>'))

# 変数の設定
rock = 'CPUがグーを出しました。あなたの負けです。'
scissors ='CPUがチョキを出しました。あなたの負けです。'
paper = 'CPUがパーを出しました。あなたの負けです。'
error ='入力が不正です。終了します。'

# 判定
if user == 1: #userが1:グーを出した時の判定
    print(paper)
elif user == 2: #userが2:チョキを出した時の判定
    print(rock)
elif user == 3: #userが3:パーを出した時の時の判定
    print(scissors)
else: #userが1,2,3以外の数値を出した時の判定
    print(error)
