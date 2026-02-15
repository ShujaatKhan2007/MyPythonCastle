#prime number


no=int(input("Enter a number :-"))

# unit_pl= no%10
# once_pl = no/10
# sum= unit_pl+once_pl

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

if(is_prime(no)):
    print("prime number")
else:
    print("not prime number")

