def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    print("Multiplication: ", multiply(num1,num2))
    print("Division: ", divide(num1, num2))

