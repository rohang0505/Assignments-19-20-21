import threading

def ChkPrime(No):
    if No < 2:
        return False
    
    for i in range(2,No):
        if No % i == 0:
            return False
        
    return True

def Prime(Data):
    print("Prime Numbers :")

    for i in Data:
        if ChkPrime(i):
            print(i, end = " ")

    print()

def NonPrime(Data):
    print("Non-Prime Numbers :")

    for i in Data:
        if not ChkPrime(i):
            print(i, end = " ")

    print()

def main():
    Size = int(input("Enter number of Elements :"))

    Arr = []

    print("Enter Elements :")
    for i in range(Size):
        No = int(input())
        Arr.append(No)

    T1 = threading.Thread(target = Prime, args =(Arr,), name = "Prime")
    T2 = threading.Thread(target = NonPrime, args =(Arr,), name = "NonPrime")

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()