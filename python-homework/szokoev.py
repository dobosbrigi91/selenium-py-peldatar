def szokoev(evszam):
    return (evszam % 4 == 0 and evszam % 100 !=0 or evszam % 400 == 0)
x = szokoev(400)
print(x)

x = szokoev(int(input('Írj be egy évszámot: ')))
if x == True:
    print('Szökőév')
else:
    print('Nem szökőév')
