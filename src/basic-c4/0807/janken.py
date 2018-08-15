import random

hand = ["goo", "choki", "pa-", "game set"]

print("=== Let it play Jyanken ===")
while True:
    com = random.randint(0,2)
    for i,desc in enumerate(hand):
        print(i, ":", desc)
    you = int(input("出す手を数値で入力: "))
    if you == 3: break
    if you < 0 or you > 2:
        print("0 kara 3 の間で入力してね")
        continue

    print("---")
    print("自分:", hand[you])
    print("相手:", hand[com])
    print("---")

    j = (you - com + 3) % 3
    if j == 0:
        print("あいこ")
    elif j == 1:
        print("負け")
    else:
        print("勝ち")
    input("---")


