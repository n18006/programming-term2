arashi = [
   ("Aiba", 175),
   ("Matsumoto", 172),
   ("Ninomiya", 168),
   ("Oono", 166),
   ("Sakurai", 171),
]

seniority_list = sorted(
    arashi,
    key = lambda ara : ara[1],
    reverse = False)

for i in seniority_list: print(i)
