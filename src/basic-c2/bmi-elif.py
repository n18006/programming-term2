weight = float(input('体重(kg)は ? '))
height = float(input('身長(cm)は ? '))

height = height / 100
bmi = weight / (height * height)

result = ""
if bmi < 18.5:
    result = "痩せ型"
elif (18.5 <= bmi) and (bmi < 25):
    result = "標準体重"
elif (25 <= bmi) and (bmi < 30):
    result = "肥満軽"
else:
    result = "肥満重"

print("BMI :", bmi)
print("判定:", result)
