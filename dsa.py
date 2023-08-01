import math

# user_num=int(input("Upper limit for prime: "))

# def is_prime(num):
#     for i in range(2, int(math.sqrt(num)+1)):
#         if num % i == 0 : 
#             return False
#     return True

# for i in range(2,user_num+1):
#     if is_prime(i):
#         print(i)    
        
n = int(input("Enter the upper limit: "))
def isPrime(x):
    # if x is even than it's not prime number. 
    if x%2==0:
        return False
    # Even number is not prime number unless it's 2.
    if x==2:
        return True
    # I have to check only odd numbers.
    upper_limit=int(math.sqrt(x)+1)
    for i in range(3,upper_limit,2):
        if x%i==0:
            return False
    return True


for i in range(1,n+1):
    if isPrime(i):
        print(i)