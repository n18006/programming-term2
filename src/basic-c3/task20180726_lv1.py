import random

goal_pos = 10 #双六のゴール位置
cur_x = 0 #現在位置.初期化の為０を代入
dice_value = 0 #サイコロの出た目を代入する変数。初期化の為０を代入。

# 関数の設定
def shake_dice():
    '''
    1~6までのサイコロの目をランダムな数字で出力

    Parameters
    ----------
    なし

    Returns
    -------
    int : 1~6までのランダムな数値

    '''
    return random.randint(1, 6)


def go_forward(n):
    '''
    進んだマスの合計値

    Parameters
    ----------
    n : int
    進む数値

    Returns
    -------
    なし

    '''

    global cur_x
    cur_x += n

# メイン処理
while cur_x < goal_pos:
    input("サイコロを振ってください>>>")
    dice_value = shake_dice()
    go_forward(dice_value)
    if cur_x < goal_pos:
        print(dice_value, "が出ました。現在位置は", cur_x, "です。")
    else:
        print(dice_value, "が出ました。おめでとうございます、ゴールしました。")
