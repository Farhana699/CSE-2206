def check_greater(num1:int, num2:int, num3:int) :
    if num1>num2 and num1>num3:
        print(f"{num1} is greater")
    elif num2>num1 and num2>num3:
        print(f"{num2} is greater")
    elif num3>num1 and num3>num2:
        print(f"{num3} is greater")
    else:
        print(f"Three numbers are equal")

def input_value() :
    num1: int = int(input("Enter first number : "))
    num2: int = int(input("Enter second number : "))
    num3: int = int(input("Enter third number : "))
    return num1,num2,num3

def main() :
    num = input_value()
    check_greater(num[0],num[1],num[2])

if __name__ == "__main__":
    main()