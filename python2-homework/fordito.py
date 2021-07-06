mylist = []

while True:
    number = int(input('Írj egy pozitív számot: '))
    if number > 0:
        mylist.append(number)
    elif number == 0:
        mylist.sort(reverse=True)
        print(mylist)
        break
    else:
        print('Pozitív számot kérek')