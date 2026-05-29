m1=int(input("Enter Mark-1 : "))
m2=int(input("Enter Mark-2 : "))
m3=int(input("Enter Mark-3 : "))
m4=int(input("Enter Mark-4 : "))
m5=int(input("Enter Mark-5 : "))
total = m1 + m2 + m3 + m4 + m5
average = total / 5.0
print("Total : ",total)
print("Average : ",average)
if m1 >= 35 and m2 >= 35 and m3 >= 35 and m4 >= 35 and m5 >= 35:
    print("Result : pass ")
if average >= 90 and average <= 100:
    print("Grade A")
elif average >= 80 and average <= 89:
    print("Grade B")
elif average >= 70 and average <= 79:
    print("Grade C")
elif average >= 60 and average <= 69:
    print("Grade D")
elif average >=50 and average <= 59:
    print ("Grade E")
else:
    print("Result : fail ")