brojevi = [3, 10, 12, 2, 7]
for broj in brojevi:
    print(broj)

for x in range(0, len(brojevi)):
    print(brojevi[x])


korisnicka_imena = ["gost54", "petar123", "jovana555"]
for x in range(len(korisnicka_imena)):
               print(korisnicka_imena[x])

#dodavanje novog clana liste
korisnicka_imena.append("marko332")

print(korisnicka_imena)
#menjanje clana liste
korisnicka_imena[1] = "marija221"
print(korisnicka_imena)

#brisanje korisnika
korisnicka_imena.remove("marija221")
print(korisnicka_imena)
korisnicka_imena.pop(0)
print(korisnicka_imena)
del korisnicka_imena [0]
print(korisnicka_imena)
#brisanje cele liste
korisnicka_imena.clear()
print(korisnicka_imena)

korisnici = ["petar", "ana", "jovana", "tijana", "jovan","milica"]
for i in range(len(korisnici)):
        print(f"Index: {i}, Vrednost: {korisnici[i]}")

for indeks, vrednost in enumerate(korisnici):
        print(f"Indeks je: {indeks}, Vrednost je: {vrednost}")

#slice-ovi
izdvojeni_korisnici = korisnici[1:5]
print(izdvojeni_korisnici)
