# python code to check if a number or string is a palindrome or not
numorstring= input("enter a number:- ")
rev=numorstring[::-1]
if(rev==numorstring):
    print("palandrome")
else:
    print("not palandrome")