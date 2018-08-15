def calctime(dist, speed):
    t = dist / speed
    t = round(t, 1)
    return t

print( calctime(500, 100))
print( calctime(dist=500, speed=100))
