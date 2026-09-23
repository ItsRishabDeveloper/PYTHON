def two_sum(nums, target):
  seen = {}
  for index , value in enumerate(nums):
      complement = target - value
      if complement in seen:
        return[seen[complement],index]
      seen[value] = index
print(two_sum([3, 8, 4, 12],11))