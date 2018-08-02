import random

goal_pos = 10
cur_x = 0
dice_value = 0

def shake_dice():
    return random.randint(1, 6)


def go_forward(n):
    global cur_x
    cur_x += n


while cur_x < goal_pos:
    input("サイコロを振ってください>>>")
    dice_value = shake_dice()
    go_forward(dice_value)
    if cur_x < goal_pos:
        print(dice_value, "が出ました。現在位置は", cur_x, "です。")
    else:
        print(dice_value, "が出ました。おめでとうございます、ゴールしました。")
