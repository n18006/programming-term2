anumal = [
("lion", 58),
("cheater", 110),
("zebla", 60),
("tonakai", 80),

]

faster_list = sorted(
            anumal,
            key = lambda ani : ani[1],
            reverse = True)

for i in faster_list: print(i)
