i=int(input("enter a number:-"))
a=0
b=1
print(a)
print(b)

for k in range(0,i-2): 
    c=a+b
    a=b
    b=c
    print(c)