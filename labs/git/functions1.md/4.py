newlist =[]
def isPrime(nums):
    cnt = 0
    for i in range(0,len(nums)):
        if nums[i]==0 or nums[i]==1:
            continue
        else:
            for x in range(2, (nums[i]//2)+1):
                if nums[i] % x == 0:
                    cnt += 1
        if cnt == 0:
            newlist.append(nums[i])
        else:
            cnt = 0
nums = [int(x) for x in input().split()]
isPrime(nums)
print(newlist)