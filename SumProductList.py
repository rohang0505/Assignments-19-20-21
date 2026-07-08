import threading
Sum = 0
Product = 1

def SumList(Data):
    global Sum

    for i in Data:
        Sum = Sum + i

def ProductList(Data):
    global Product

    for i in Data:
        Product = Product * i

def main():
    Size = int(input("Enter Number of Elements :"))

    Arr = []

    print("Enter Elements :")
    for i in range(Size):
        No = int(input())
        Arr.append(No)

        T1 = threading.Thread(target=SumList, args=(Arr,))
        T2 = threading.Thread(target=ProductList, args=(Arr,))

        T1.start()
        T2.start()

        T1.join()
        T2.join()

    print("Sum of Elements :",Sum)
    print("Product of Elements :",Product)

if __name__ == "__main__":
    main()