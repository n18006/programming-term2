arashi = [
   ("Aiba", 35),
   ("Matsumoto", 34),
   ("Ninomiya", 35),
   ("Oono", 37),
   ("Sakurai", 36),
]

seniority_list = sorted(
    arashi,
    key = lambda ara : ara[1],
    reverse = True)

for i in seniority_list: print(i)
