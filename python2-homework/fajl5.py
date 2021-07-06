forrasfajl = open('adat.txt')
celfajl = open('new.txt', 'w')
for sor in forrasfajl:
    print(sor, end='', file=celfajl)
forrasfajl.close()
celfajl.close()