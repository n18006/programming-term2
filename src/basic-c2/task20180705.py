# 値段 
beer_v = 200
otumami_v = 100
yakitori_v = 100

# 個数
beer_c = 2
otumami_c = 1
yakitori_c = 2

# 割引率
yakitori_sale = 0.2

# ポイントカード 
point = 150

# 計算
beer_sum = beer_v * beer_c
otumami_sum = otumami_v * otumami_c
yakitori_sum = yakitori_v * (1 - yakitori_sale) * yakitori_c
pay = beer_sum + otumami_sum + yakitori_sum - point

# お会計
print('お支払は', pay,'円です。')
