#while else & for else

i=1
while i<=5:
    print(i)
    i+=1
else:
    print("loop complete") 
    
    
i=1
for i in range(20):
    if i==5:
        break;
    print(i)
else:
    print("for loop complete")