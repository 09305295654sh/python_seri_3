import random
import math
print("lotfan do adad ra vared konid:")
a=int (input())
b=int (input())
aray_1=[]
aray_2=[]
aray_3=[]
for i in range(a):

  if a%(i+1)==0:
    
    aray_1.append(int(i+1))
print(aray_1)

for j in range(b):
   if b%(j+1)==0:
    aray_2.append(int(j+1))
print(aray_2)
array_1_as_set = set(aray_1)
intersection = array_1_as_set.intersection(aray_2)

intersection_as_list = list(intersection)
print(intersection_as_list)
max(intersection_as_list)
print(max(intersection_as_list))