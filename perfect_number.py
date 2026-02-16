#perfect number 
no= int(input("Enter a number: "))
count=0

for  i in range (1,no):
   if no%i==0:
      count+=i
if count==no:
            print("Perfect number")
else:
          print("Not a perfect number")
      