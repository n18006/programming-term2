nums = list(range(1, 40 + 1))

nums3 = lambda x: x % 3 == 0 or x // 10 == 3 or x % 10 == 3
print(list(filter(nums3, nums)))
