brojevi = range(1,5) # u pozadini: 1,2,3,4 opseg

for broj in brojevi:
    print(broj)

poruka = "Hello!" #sting
for x in range(0, len(poruka)): #prolazak kroz opseg, brojeve koristimo za pozicije
    print(poruka[x])

for slovo in poruka: #prolazak kroz clanove kolekcije
    print(slovo)

poruka = "Zdravo kako ste"
print(len(poruka))


#poruka[0] = "P" # string je nemutabilan. Ne moze da se menja

# print(poruka[0])
# print(poruka[1])
# print(poruka[2])
# print(poruka[3])
# print(poruka[4])
# print(poruka[5])
# for slovo in poruka:
#     print(slovo)

poruka = "Hello World"
print(poruka.upper())
print(poruka.lower())
print(poruka.capitalize())