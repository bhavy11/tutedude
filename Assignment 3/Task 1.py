def factorial(num):
    f = 1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    else:
        for i in range(1, num + 1):
            f = f * i
        print("The factorial of", num, "is", f)
num=int(input("Enter a number: "))
factorial(num)
