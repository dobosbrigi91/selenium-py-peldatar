mylist = []
with open('TEXT.txt') as file:
    text = file.read()
kisbetus = str.split(text.lower())

szavakszama = {}
for szo in kisbetus:
    if szo in szavakszama:
        szavakszama[szo] = szavakszama[szo] +1
    else:
        szavakszama[szo] = 1
print(szavakszama)

