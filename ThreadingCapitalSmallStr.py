import threading

def Small(Str):
    Count = 0

    for ch in Str:
        if ch.islower():
            Count += 1

    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Small letters:", Count)
    print()

def Capital(Str):
    Count = 0

    for ch in Str:
        if ch.isupper():
            Count += 1

    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Capital letters:", Count)
    print()

def Digits(Str):
    Count = 0

    for ch in Str:
        if ch.isdigit():
            Count += 1

    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Digits:", Count)
    print()

def main():
    Value = input("Enter string: ")

    T1 = threading.Thread(target=Small, args=(Value,), name="Small")
    T2 = threading.Thread(target=Capital, args=(Value,), name="Capital")
    T3 = threading.Thread(target=Digits, args=(Value,), name="Digits")

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

if __name__ == "__main__":
    main()