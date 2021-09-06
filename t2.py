def power(x, y):
    p = 1
    for i in range(y):
        p *= x
    return p


while True:
    try:
        x = int(input("enter x: "))
        y = int(input("enter y: "))
        print(power(x, y))
        break
    except ValueError:
        print("try again!")
