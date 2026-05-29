days=int(input("Enter The Days : "))
if(days==0):
    print("good no fine amount")
elif(days >=1 and days <=5):
    print("Fine Amount : ",days * 0.5)
elif(days >=5 and days <=10):
    print("Fine Amount : ",days * 1)
elif(days >=10 and days <=30):
    print("Fine Amount : ",days * 5)
else:
    print("Membership Cancel")