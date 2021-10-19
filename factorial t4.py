import math
print('ye adad vared kon:')
n=int (input())
i=1
f=1
while True:
    i+=1
    f=f*i
    if f==n or n==1:
     print('yes')
     break
    elif f>n  and  f!=n:
     print('no')
     break
print ('end')    
