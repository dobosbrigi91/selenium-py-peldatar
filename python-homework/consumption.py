# Az autód 7 litert fogyaszt országúton és 9-et városban. A hévízi üdülésedre 170 kilómétert utazol országúton
# és 35-öt
# városban. Mennyit fogyaszt az autód csak oda? És oda-vissza? Mennyibe kerül a teljes út, ha 350 Ft a benzin?
# Oldd meg ezt feladatot úgy, hogy nem előre megadott értékekkel (országúti fogyasztás, városi fogyasztás, országúton
# megtett út, városban megtett út, benzin ára) dolgozol, hanem a felhasználótól kéred ezeket be. Ahol szükséges, ne
# feledd konvertálni az értékeket!
országút = 7
város = 9
benzin = 350

országút_km = 170
város_km = 35

print('Csak oda: ', int(((országút_km / országút) + (város_km / város))), ' litert fogyaszt')
print('Oda-vissza: ', int((2 * ((országút_km / országút) + (város_km / város)))), ' litert fogyaszt')
print('Teljes út: ', int((2 * ((országút_km / országút) + (város_km / város)))) * benzin, ' Ft-ba kerül')

user_országút = int(input('Országúti fogyasztás: '))
user_város = int(input('Városi fogyasztás: '))
user_benzin = int(input('Mennyibe kerül a benzin?'))
user_országútkm = int(input('Megtett km országúton: '))
user_városkm = int(input('Megtett km városban: '))
print('Csak oda: ', int(((user_országút / user_országútkm) + (user_városkm / user_város))), ' litert fogyaszt')
print('Oda-vissza: ', int((2 * ((user_országút / user_országútkm) + (user_városkm / user_város)))), ' litert fogyaszt')
print('Teljes út: ', int((2 * ((user_országút / user_országútkm) + (user_városkm / user_város)))) * user_benzin, ' Ft-ba kerül')