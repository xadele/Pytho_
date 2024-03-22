#Importē bibliotēkas.
from random import randint, shuffle

# print(randint(1,100)) #atrod nejaušu skaitli no dotā intervāla

# saraksts = [1,2,3,4,5]
# a = shuffle(saraksts) #sajauc sarakstu
# print(saraksts)

# #metode try exept pārbauda vai tiek ievadīts prasītais.
# while True:
#     x = input("Ievadi veselu skaitli: ")
#     try:
#         if int(x):
#             break
#     except:
#             print(f"{x} nav vesels skaitlis")
# print(f"Ievadītais skaitlis ir {x}")


# #pārbauda, lai ievada tieši atļautos simbolus.
# x = input("Ievadi 1, 2 vai 3: ")
# while x not in["1", "2", "3"]:
#     x = input("Ievadi 1, 2 vai 3: ")


#------------------------------

glazites = ["🎁", "🎁", "✨"]
print(*glazites)

def sajauc(glazites):
    shuffle(glazites)
    return glazites 
# print(sajauc(glazites))

def mans_minejums():
    minejums = ""
    while minejums not in ["1", "2", "3"]:
        minejums = input("Ievadi 1, 2 vai 3: ")
    return int(minejums)
#print(mans_minejums())

def parbaudi_minejumu(glazites, minejums):
    if glazites[minejums-1] == "✨":
        print("Uzvarēji! 🎉")
    else:
        print("Tu neuzminēji!😢 mēģini vēlreiz😉 ")
        print(*glazites)

#Pa soļiem izsauc visas funkcijas.

#Sajauc glazītes
sajauktais = sajauc(glazites)

#Spēlētāja minejums
spele_minejums = mans_minejums()

#Pārbauda spēlētāja minējumu
parbaudi_minejumu(sajauktais, spele_minejums)





