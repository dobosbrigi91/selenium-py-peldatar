with open('adat.txt', 'r') as file3:
    adat = list(file3.readlines())
with open('hw.txt', 'w') as f3:
    for sor in adat:
        f3.write(sor.replace('\n', ' '))