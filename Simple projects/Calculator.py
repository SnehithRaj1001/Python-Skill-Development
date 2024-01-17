num1 = 0
num2 = 0
result = 0

def takeNum():
    global num1, num2
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))

def addNum():
    global num1, num2, result
    result = num1 + num2

def subNum():
    global num1, num2, result
    result = num1 - num2

def mulNum():
    global num1, num2, result
    result = num1 * num2

def divNum():
    global num1, num2, result
    result = num1 / num2
    
def printNum():
    global result
    print("Result is", result, "\n")


choice = 0
takeNum()
while choice != 6:
    choice = int(input("Enter choice(1. Add, 2. Subtract, 3. Multiply, 4. Divide, 5. Change Number, 6. Exit): "))
    if choice == 1:
        addNum()
        printNum()
    elif choice == 2:
        subNum()
        printNum()
    elif choice == 3:
        mulNum()
        printNum()
    elif choice == 4:
        divNum()
        printNum()
    elif choice == 5:
        takeNum()
    elif choice == 6:
        print("Exit")
    else:
        print("Invalid choice")