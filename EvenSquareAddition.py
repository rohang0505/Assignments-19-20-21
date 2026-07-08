from functools import reduce

FilterX = lambda No: No % 2 == 0
MapX = lambda No : No * No
ReduceX = lambda A, B : A + B

def main():
    Size = int(input("Enter Number of Element :"))

    Arr = []

    print("Enter Element :")
    for i in range(Size):
        No = int(input())
        Arr.append(No)

    FData = list(filter(FilterX,Arr))
    print("After Filter is :",FData)

    MData = list(map(MapX,FData))
    print("After Map is :",MData)

    RData = reduce(ReduceX,MData)
    print("Reduce is :",RData)

if __name__ == "__main__":
    main()