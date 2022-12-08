nums = [54, -1, 56, 425, 5, 1444, 4134, 1, 46, 75, 34]
max_num = max(nums[0:2])
sec_max = min(nums[0:2])
for num in nums:
    if num < sec_max:
        continue
    if num > sec_max and num < max_num:
        sec_max = num
    if num > max_num:
        sec_max = max_num
        max_num = num
print(sec_max)