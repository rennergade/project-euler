maxn = 200000
nums = ''
for i in range(1,maxn+1):
    nums += str(i)
print nums
print len(nums)
ans = int(nums[0]) * int(nums[99]) * int(nums[999]) * int(nums[9999]) * int(nums[99999]) * int(nums[999999])
print ans
