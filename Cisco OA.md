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
num = input()
num = num[1: -1]
print(num)
if len(num) == 0:
    print(0)
dp = [0 for _ in range(len(num) + 1)]
dp[0] = 1
dp[1] = 1
for i in range(2, len(num) + 1):
    dp[i] += dp[i - 1]
    if num[i - 2] != "0":
        tmp = int(num[i - 2: i])
        if 10 <= tmp <= 25:
            dp[i] += dp[i - 2]
print(dp[-1])
```
# Black and white chese board

```Python
n = int(input())
for i in range(1, n + 1):
    res = ["" for _ in range(n)]
    if i % 2 == 1:
        for j in range(1, n + 1):
            res[j - 1] = "W" if j % 2 == 1 else "B"
    else:
        for j in range(1, n + 1):
            res[j - 1] = "B" if j % 2 == 1 else "W"
    print(" ".join(res))
```
# chocolate
```Python
n = int(input())
nums = input().split()
nums = [int(i) for i in nums]
dp = [0 for _ in range(n)]
dp[0] = nums[0]
for i in range(1, n):
    if i == 1:
        dp[i] = max(dp[i - 1], nums[i])
    else:
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

print(dp[-1])

```
# Maximum difference
```Python
n = int(input())
nums = input().split()
nums = [int(i) for i in nums]
if n == 1:
    print(0)
mi = float("inf")
res = 0
for n in nums:
    res = max(res, n - mi)
    mi = min(mi, n)
print(res)

```
