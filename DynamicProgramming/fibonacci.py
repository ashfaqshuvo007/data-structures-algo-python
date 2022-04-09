
#recursion
def fibRecursion(n):
    if n==1 or n==2:
        return 1
    else:
        fibSeries =  str(fibRecursion(n-1)) + str(fibRecursion(n-2))
    
    return fibSeries


if __name__ == '__main__':
    n = input("Enter Number: ").strip()

    print(fibRecursion(n),end=" ")