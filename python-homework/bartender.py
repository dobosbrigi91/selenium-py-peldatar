age = int(input('Hány éves?'))
drink = input('Mit iszik?')

if age < 18:
    if drink == 'sör':
        print('Nem adhatok sört')
    elif drink == 'kóla':
        print('Tessék')
    else:
        print('Csak sör és kóla van')
elif age > 60:
    if drink == 'sör':
        print('Tessék')
    elif drink == 'kóla':
        print('A koffein megemeli a vérnyomást')
    else:
        print('Csak sör és kóla van')
else:
    if drink == 'sör':
        print('Tessék')
    elif drink == 'kóla':
        print('Tessék')
    else:
        print('Csak sör és kóla van')