## # Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát így,
# ahogy beolvastad, soronként egy szóval egy másik fájlba!
with open('adat.txt', 'r') as file4:
    list4 = list(file4.readlines())
with open('list4.txt', 'w') as f4:
    for alatt in list4:
        f4.write(alatt)