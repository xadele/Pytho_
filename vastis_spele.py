from random import randint

valstis = {
    'Igaunija': 'Tallina',
    'Kipra': 'Nikosija',
    'Itālija':'Roma',
    'Latvija': 'Rīga',
    'Malta' : 'Valeta',
    'Spānija': 'Madrida',
    'Krivija':'Maskava',
    'Norvēģija':'Oslo',
    'Lietuva' : 'Viļņa',
    'Islande': 'Reikjavika'
 }

valstis1 = list(valstis.keys())
#print(valstis1)

punkti = 0
jautajumi = 0

while True:
    gadijums = randint(0,len(valstis1)-1)
    galvaspilseta = input(f"Kas ir {valstis1[gadijums]}s galvaspilsēta?: ")

    if galvaspilseta.lower() == "q":
        break
    elif galvaspilseta.capitalize() == valstis[valstis1[gadijums]]:
        print("Pareizi")
        punkti += 1
    else:
        print("nepareizi")
    jautajumi += 1


if punkti <=5:
    print(f"Tev vēl ir jāpamācās😕, tu atbildēji uz {jautajumi} jautājumiem un ieguvi {punkti} punktus.")
elif punkti > 5:
    print(f"Tu esi malacis🤩! Tu atbildēji uz {jautajumi} jautājumiem un ieguvi {punkti} punktus!")  