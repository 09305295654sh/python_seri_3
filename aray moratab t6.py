import math
import random
print ('lotfan tool araye ra vared konid:')
len=int(input())
aray=[]
print("anasor araye ra vared konid:")
for i in range(len):
  a=int(input()) 
  aray.append(a)
print(aray)
for j in range(len-1):
  if int(aray[j])>int(aray[j+1]):
     break
if(j+2==len):
 print("moratab hast")
else:
  print("moratab nist")