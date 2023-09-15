low = 1
high = 100
CountOfTotalSymmetricNum = 0
for i in range(low, high+1):
    
    n = i
    res = [int(x) for x in str(n)]
    if len(res)%2 == 0:
        q = len(res)//2
        sum1 = sum(res[:q])
        sum2 = sum(res[q:])
        if sum1==sum2:
            CountOfTotalSymmetricNum +=1
print(CountOfTotalSymmetricNum)

