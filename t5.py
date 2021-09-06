from random import randint

m = 1
n = 100
# x = randint(m, n)    --> it's false; but test it..
x = randint(m, n - 1)
print(x)
while True:
    guess = input('enter "k" or "b" or "d": ').strip()
    if guess == 'd':
        print("that's true!")
        break
    elif guess == 'k':
        n = x
        x = (x + m) // 2
        print(x)
    elif guess == 'b':
        m = x
        x = (x + n) // 2
        print(x)
