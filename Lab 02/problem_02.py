def check_greater(num1:int, num2:int) :
    if num1>num2:
        print(f"{num1} is greater")
    elif num2>num1:
        print(f"{num2} is greater")
    else:
        print(f"Two numbers are equal")


def main() :
    num1: int = int(input("Enter first number : "))
    num2: int = int(input("Enter second number : "))
    check_greater(num1,num2)

if __name__ == "__main__":
    main()