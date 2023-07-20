# prime number
def is_prime():
    num = int(input("Enter a number: "))
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                break
            else:
                print(num, "is a prime number")
    else:
        print(num, "is not a prime number")


# is_even:
def is_even():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")