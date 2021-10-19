# This is example of recursion

def fibonacci(n):
    if n < 0:
        print("Cannnot find the fiboncci of a negative number.")

    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


number = int(input("Enter an integer:"))
result = fibonacci(number)
print("Fabonacci(%d) = %d." % (number, result))
