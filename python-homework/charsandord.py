abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n = 1
for i in abc:
    print(i, ord(i), end=' ')
    if n % 4 == 0:
        print('')
    n = n + 1