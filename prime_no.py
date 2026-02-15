#prime number


no=int(input("Enter a number :-"))

unit_pl= no%10
once_pl = no/10
sum= unit_pl+once_pl

if(sum==no):
    print("perfect number")
else:
    print("not perfect number")

