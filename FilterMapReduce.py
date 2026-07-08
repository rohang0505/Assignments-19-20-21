from functools import reduce

FilterX = lambda No: No >= 70 and No <= 90
MapX = lambda No: No + 10
ReduceX = lambda A, B: A * B

def main():

    Size = int(input("Enter number of elements: "))

    Arr = []

    print("Enter elements:")
    for i in range(Size):
        No = int(input())
        Arr.append(No)

    FData = list(filter(FilterX, Arr))
    print("List after filter:", FData)

    MData = list(map(MapX, FData))
    print("List after map:", MData)

    RData = reduce(ReduceX, MData)
    print("reduce is:", RData)

if __name__ == "__main__":
    main()