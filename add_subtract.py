def add(x, y):
    return x + y
def subtract(x, y):
    return x - y

if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    print("Addition: ", add(num1,num2))
    print("Subtraction: ", subtract(num1, num2))
    