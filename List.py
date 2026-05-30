#list in python
"""
sequence type 
mutable
"""
a=[1,2,3,4,5]
print(a)
print(type(a))
a[0]=100
print(a)
print("Slicing")
print(a[1])
print(a[-1])
print(a[0:3])
print(a[2:])
print(a[:3])

print("==========")

a=[1,True,'ram',2.5,[1,2,3,4,5]]
print(a)
print(type(a))
print(a[0], "type is ",type(a[0]))
print(a[1], "type is ",type(a[1]))
print(a[2], "type is ",type(a[2]))
print(a[3], "type is ",type(a[3]))
print(a[4], "type is ",type(a[4]))
print(a[4][1])

print("==========")

a=[10,20,30,40,50]
print(a)
a.clear()
print(a)
a=[10,30,30,42,13,20,45,42,30,50]
print(a.count(30))
print(a.index(30))
print(len(a))
print(max(a))
print(min(a))
print(a)
a.pop(0)#remove elemenet using index
print(a)
a.remove(30)#values
print(a)

print("==========")

name=["yuvaraj"]
print(name)
name.append("sam")
name.append("kavin")
name.append("praveen")
print(name)
name.insert(0,"suriya")
print(name)

print("==========")
print(list(range(5)))
print(list("yuvaraj"))

print("==========")

a=[19,34,54,67,89,100,322]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)

print("==========")

a=["yuvaraj","kavinkumar","praveen"]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a.sort(key=len)
print(a)




