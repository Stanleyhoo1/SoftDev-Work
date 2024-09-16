def sum13(nums):
  found = False
  sum = 0
  for i in nums:
    if found==False:
      if i==13:
        found=True
      else:
        sum+=i
    else:
      found=False
  return sum

print(sum13([1, 2, 2, 1]))
print(sum13([1, 1]))
print(sum13([1, 2, 2, 1, 13]),
sum13([1, 2, 13, 2, 1, 13]),
sum13([13, 1, 2, 13, 2, 1, 13]),
sum13([]),
sum13([13]),
sum13([13, 13]),
sum13([13, 0, 13]),
sum13([13, 1, 13]),
sum13([5, 7, 2]),
sum13([5, 13, 2]),
sum13([0]),
sum13([13, 0]))
