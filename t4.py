def comb(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return comb(n - 1, k - 1) + comb(n - 1, k)


while True:
    try:
        n = int(input("enter n: "))
        k = int(input("enter k: "))
        if n >= 0 and k >= 0:
            print(comb(n, k))
            break
        else:
            print('try again!')
    except ValueError:
        print("please ineger!")
