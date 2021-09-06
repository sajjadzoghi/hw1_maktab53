while True:
    n = input('enter "up" or "down": ').strip()
    if n == "up":
            while True:
                try:
                    x = int(input("enter a number: "))
                    if x >= 1:
                        for i in range(1, x + 1):
                            print(i, end=' ')
                        break
                    else:
                        for i in range(1, x - 1, -1):
                            print(i, end=' ')
                        break
                except ValueError:
                    print('enter an integer!')
            break
    elif n == 'down':
        if ' ' in n or ' ' not in n:
            while True:
                try:
                    x = int(input("enter a number: "))
                    if x < 20:
                        for i in range(20, x - 1, -1):
                            print(i, end=' ')
                        break
                    else:
                        print('sorry just >20 !')
                except ValueError:
                    print('enter an integer!')
            break
    else:
        print('just "up" or "down"')