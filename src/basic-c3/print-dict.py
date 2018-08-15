fruits = {'banana': 300,
            'orange': 240,
            'ichigo': 350,
            'mango': 400
           }

for name in fruits.keys():
    price = fruits[name]
    s = "{0}は、{1}円です。".format(name, price)
    print(s)
