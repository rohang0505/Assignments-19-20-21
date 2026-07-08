import threading

def EvenList(Data):
    Sum = 0

    for i in Data:
        if i % 2 == 0:
            Sum = Sum + i

    print("Sum of Even Elements:", Sum)

def OddList(Data):
    Sum = 0

    for i in Data:
        if i % 2 != 0:
            Sum = Sum + i

    print("Sum of Odd Elements:", Sum)

def main():
    Size = int(input("Enter number of elements: "))

    Arr = []

    print("Enter elements:")
    for i in range(Size):
        No = int(input())
        Arr.append(No)

    T1 = threading.Thread(target=EvenList, args=(Arr,), name="EvenList")
    T2 = threading.Thread(target=OddList, args=(Arr,), name="OddList")

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()