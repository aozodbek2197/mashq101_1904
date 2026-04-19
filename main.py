# 1-mashq
nums = list(map(int,input().split()))
res = 0
for n in nums:
    res ^= n
print(res)
# 2-mashq
h = list(map(int,input().split()))
stack=[]
res=0

for i in range(len(h)+1):
    while stack and (i==len(h) or h[stack[-1]]>h[i]):
        height = h[stack.pop()]
        width = i if not stack else i-stack[-1]-1
        res = max(res, height*width)
    stack.append(i)

print(res)
# 3-mashq
s = input()
seen=set()
l=0
res=0

for r in range(len(s)):
    while s[r] in seen:
        seen.remove(s[l]); l+=1
    seen.add(s[r])
    res=max(res,r-l+1)

print(res)
# 4-mashq
s = input()
seen=set()
l=0
res=0

for r in range(len(s)):
    while s[r] in seen:
        seen.remove(s[l]); l+=1
    seen.add(s[r])
    res=max(res,r-l+1)

print(res)
# 5-mashq
m = [["1","0"],["1","1"]]

dp = [[0]*(len(m[0])+1) for _ in range(len(m)+1)]
res = 0

for i in range(1,len(m)+1):
    for j in range(1,len(m[0])+1):
        if m[i-1][j-1]=="1":
            dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
            res = max(res, dp[i][j])

print(res*res)
