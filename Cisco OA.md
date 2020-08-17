# Count bits
```Python
num = int(input())
#print(bin(num))
print(bin(num).count("1"))
```

# Length of list
```Python
nums = input()
print(len(nums.split()))
```
# Prime and Composite
```Python
def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True

n = int(input())
nums = input().split()
nums = [int(i) for i in nums]
res = []
for n in nums:
    if isPrime(n):
        res.append("Prime")
    else:
        res.append("Composite")
print(" ".join(res))

```
# Mean and Mode
```n = int(input())
nums = input().split()
nums = [int(i) for i in nums]
mean = sum(nums) / len(nums)
mean = round(mean, 4)
freq = collections.Counter(nums)
sorted_nums = list(sorted(freq.items(), key = lambda x: -x[1]))
mode = sorted_nums[0][0]
print(mean, mode)
```
# Decode ways
```Python

```
