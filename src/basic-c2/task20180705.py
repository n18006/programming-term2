# ビールの合計
bear = 100 * 2

# おつまみの合計
otumami = 100 * 1

# 焼鳥の合計　※セールで２割引
yakitori = (100 * 0.2) * 2

# ポイントカード
point_card  = 150

# 総合計
sum_t = bear + otumami + yakitori

# お会計
print('お支払は',sum_t - point_card,'円です。')
