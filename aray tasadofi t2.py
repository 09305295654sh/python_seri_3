import random
print("lotfan tool araye ra vared kon:")
n=int(input())
aray=[]
for i in range(n):
  aray.append(random.randint(0,100))
for i in range(n-1):
  if(aray[i]==aray[i+1]):
    aray.remove(i)
print(aray)

