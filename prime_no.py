#prime number


#no=int(input("Enter a number :-"))

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

# if(is_prime(no)):
#     print("prime number")
# else:
#     print("not prime number")

def prime_numbers_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

i = int(input("Enter the start of the range: "))
j = int(input("Enter the end of the range: "))
primes_in_range = prime_numbers_in_range(i, j)
print(f"Prime numbers between {i} and {j}: {primes_in_range}")