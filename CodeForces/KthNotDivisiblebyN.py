t=eval(input())
nums=[]
for i in range(t):
  nums.append(input())
for num in nums:
  cur=num.split(" ")
  n,k=int(cur[0]),int(cur[1])
  new=k
  mod=k//n
  rem=k%n
  while mod:
    new+=mod
    k=rem+mod
    mod=k//n
    rem=k%n    
  print(new)
