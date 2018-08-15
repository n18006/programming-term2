while True:
    try:
        weight = float(input("体重は"))
        height = float(input("身長は"))

        height = height / 100
        bmi = weight / (height * height)
        break;
    except:
        print("入力ミスがあります。再度入力してください")


result = ""
if bmi < 18.5: result ="痩せ型"
elif bmi < 25: result = "標準体重"
elif bmi < 30: result = "軽い肥満"
else : result = "重い肥満"

print("BMI :", bmi)
print("判定 :", result)

