def sum67(nums):
  found = False
  sum = 0
  for i in nums:
    if found==False:
      if i==6:
        found=True
      else:
        sum+=i
    else:
      if i==7:
        found=False
  return sum
