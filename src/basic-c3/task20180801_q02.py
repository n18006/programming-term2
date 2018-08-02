nums = [13600, 14500, 16000, 11111, 11667]
TAX_RATE = 10

TAX = (1 + TAX_RATE / 100)
x8 = lambda x : round(x * TAX)
print(list(map(x8, nums)))
