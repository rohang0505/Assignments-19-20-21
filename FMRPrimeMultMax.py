from functools import reduce

def CheckPrime(No):
    if No < 2:
        return False
    for i in range(2, No):
        if No % i == 0:
            return False
        
    return True

MapX = lambda No : No * 2
ReduceX = lambda A, B: A if A > B else B

def main():
    Size = int(input("Enter numbers of Elements :"))

    Arr = []

    print("Enter Elements :")
    for i in range(Size):
        No = int(input())
        Arr.append(No)

    FData = list(filter(CheckPrime,Arr))
    print("After Filter is :",FData)

    MData = list(map(MapX,FData))
    print("After Map is :",MData)

    RData = reduce(ReduceX,MData)
    print("Reduce is :",RData)

if __name__ == "__main__":
    main()