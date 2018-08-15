def genodd():
    i = 1 
    while i <= 30:
        yield i
        i += 2

it = genodd()
for v in it:
    print(v, end=",")
