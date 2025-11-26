broj = 50
#uvecavanje broja
broj = broj + 10
print(broj)

# kraca varijanta koja je ista kao i ovo gore
broj += 10

#dupliranje broja
broj = broj * 2
print(broj)
#brza varijanta
broj *= 2

###############################################
#Vezba:
# Trazi od korisnika da unese dva broja, nakon toga ih saberi.


x = int(input("Unesite prvi broj: "))
y = int(input("Unesite drugi broj: "))
rezultat = x + y
print("Zbir ova dva broja je:", rezultat)
broj_je_pozitivan = rezultat > 0
print("Broj je pozitivan", broj_je_pozitivan)