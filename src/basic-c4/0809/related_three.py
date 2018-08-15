import glob

# line4 str(nums).find("3") !=
# line4 if "3" in str(i) else str(i)

a = [
    "アホ" if i % 3 == 0 else str(i)
           if "3" or  in str(i) else str(i)
    for i in range(1,41) ]

print(a)
