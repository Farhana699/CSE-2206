def summation(num:list, size:int):
    sum=0
    for i in range(size):
        sum+=num[i]
    return sum

def multiplication():
    print

def get_numbers(size:int):
    num = []
    for i in range(size):
        n = int(input(f"Enter {i+1}. number : "))
        num.append(n)
    return num

def main():
    size:int = int(input("Total numbers to sum : "))
    num = get_numbers(size)
    print(f"Sum of {size} numbers : {summation(num,size)}")
    

if __name__ == "__main__":
    main()
    
# relative, absoulate, truePercent,