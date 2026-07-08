import threading

def Maximum(Data):
    Max = Data[0]

    for i in Data:
        if i > Max:
            Max = i

    print("Maximum Element :",Max)

def Minimum(Data):
    Min = Data[0]

    for i in Data:
        if i < Min:
            Min = i

    print("Minimum Element :",Min)

def main():
    Size = int(input("Enter Number of Elements :"))

    Arr = []

    print("Enter Elements :")
    for i in range(Size):
        No = int(input())
        Arr.append(No)

    T1 = threading.Thread(target = Maximum , args =(Arr,), name = "Maximum")
    T2 = threading.Thread(target = Minimum, args = (Arr,), name = "Minimum")

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()