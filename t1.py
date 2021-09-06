while True:
    try:
        x = int(input("enter a number: "))
        p = x
        for i in range(9):
            p *= x
            print(p, end=' ')
        break
    except ValueError:
        print("Please just integer")