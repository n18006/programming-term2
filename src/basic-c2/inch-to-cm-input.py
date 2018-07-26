# 変換の元になる値
per_inch = 2.54
user = input('何インチですか?')
inch = float(user)
cm = inch * per_inch

desc = '{0}インチ = {1}センチ'.format(inch, cm)
print(desc)
