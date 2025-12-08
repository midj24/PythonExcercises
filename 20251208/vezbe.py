a = [1,2,3]
b = [4,5,6]
c = []

#print(a+b) #ovo nadovezuje liste jednu na drugu
# print(a[0]+b[0])
# print(a[1]+b[1])
# print(a[2]+b[2])
for i in range(len(a)):
    c.append(a[i]+b[i]) #dodaje clan u listu c

print(c)
c.clear() #uklanja sve iz liste
print(c)

##################################################
#korisnicko ime mora imati 5 ili vise karaktera i ne sme da ima razmake
registrovani_korisnici = ["jovana", "a n a", "x", "marijana123"]
ispravna_imena = []

for korisnik in registrovani_korisnici:
    formatirano_ime = korisnik.replace(" ", "") #strip() sa kraja i pocetka
    if len(formatirano_ime) >=5:
        ispravna_imena.append(formatirano_ime)
    else:
        print(f"Neispravno: {korisnik}")
    
print(ispravna_imena)

ispravna_imena.sort()
print(ispravna_imena)
##################################################
#korisnik, test 1, test 2, test 3
#ana       85       90      60
#jovana    75       60      90

korisnik1 = ["ana", 85, 90, 60, 55] #korisnik1[0]
korisnik2 = ["jovana", 75, 60, 90] #korisnik2[0]

#polaznici = [["ana", 85, 90, 60, 55], ["jovana", 75, 60, 90] ]
polaznici = [korisnik1, korisnik2 ]

# ana = polaznici[0]
# jovana = polaznici[1]

# print(ana[2])
# print(jovana[1])
# #skratiti sve ovo i prikazi 85 iz Ane
# print(polaznici[0][1])
# #prikazi 75 iz Jovane
# print(polaznici[1][1])

for polaznik in polaznici:
   # print(polaznik)
    for informacija in polaznik:
        print(informacija)
    print("#######################")


korpa = [["patike addidas", 15000, 1], 
         ["patike nike", 13000, 2]]
print(f"Ukupno proizvoda u korpi: {len(korpa)}")
#ispisi detalje clanova korpe
for proizvod in korpa:
    for informacija in proizvod:
        print(informacija)
    print("***************")