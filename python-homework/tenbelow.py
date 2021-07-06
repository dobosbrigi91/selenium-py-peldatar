x = int(input('Kérek egy számot: '))
if x < 10:
    while True:
        y = int(input('Új szám: '))
        if y > 9:
            break
        x = x+y
print('Összeg: ', x)