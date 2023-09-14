nums = [[4,4],[9,10],[9,10],[3,8]]
listt = [] 
for i in range(len(nums)):
    FirstArray = nums[i]
    listt.extend(range(FirstArray[0],FirstArray[1]+1))
TotalPoints = set(listt)
print(len(TotalPoints))