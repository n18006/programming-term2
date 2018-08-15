animal_dict = {
    "lion": 58,
    "cheater": 110,
    "zebla": 60,
    "tonakai": 80,
}

li = sorted(
    animal_dict.items(),
    key=lambda x : x[1],
    reverse=True)
for name,speed in li:
    print(name, speed)
