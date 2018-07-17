import random

a = ['朝飯', '昼飯', '晩飯']
gohan_time = random.choice(a)

b = ['１人で', '家族と', '友達と']
with_who = random.choice(b)

c = ['ステーキ', 'えびちり', '素麺']
food_menu = random.choice(c)

fmt = "今日の{0}は、{1}{2}を食べよう！".format(gohan_time, with_who, food_menu)
print(fmt)
