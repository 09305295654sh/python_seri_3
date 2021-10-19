import math
aray_1=[]
aray_2=[]
print("lotfan do adad vared konid")
a=int(input())
b=int(input())
#c=a*b
for i in range(max(a,b)):
  f1=a*(i+1)
  aray_1.append(f1)
print(aray_1)

for j in range(max(a,b)):
    f2=b*(j+1)
    aray_2.append(f2)
print(aray_2)
array_1_as_set = set(aray_1)
intersection = array_1_as_set.intersection(aray_2)

intersection_as_list = list(intersection)
print(intersection_as_list)
min(intersection_as_list)
print(min(intersect