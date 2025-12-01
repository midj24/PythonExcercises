age = 10
# prikazi igru ako ima vise od 13 godina
print(age > 13) # true ili false
if age > 13:
    print ("Prikazi sadrzaj")
else: 
    print("Nedovoljno godina. Pristup nije odobren!")

# logicki operatori i kontrola toka
email_baza = "korisnik@gmail.com"
sifra_baza = "123"

uneti_email = "korisnik@gmail.com"
uneta_sifra = "123"

# ispisi uspesno logovanje ukoliko su ispravni i email i sifra
if email_baza == uneti_email and sifra_baza == uneta_sifra:
    print("Uspesno logovanje!")

#if unutar if-a
brzina_vozila = 50
ogranicenje = 50
urucena_kazna = False

if brzina_vozila > 50:
    # if urucena_kazna == False:
    if not urucena_kazna: # false --> true
        print("Dodajte kaznene poene")
    print("Posaljite kaznu")


# prikazati korisniku uspesno ili nesupesno logovanje, u zavisnosti od ispravnosti podataka
if uneti_email == email_baza and sifra_baza == uneta_sifra:
    print("Uspesno logovanje!")
else:
    print("Neispravni podaci!!!!")

print("\nlinija koja se izvrsava u svakom slucaju")



novac_na_racunu = 1200
cena_proizvoda = 500

# Uspesna / Neuspesna kupovina

if novac_na_racunu >= cena_proizvoda:
    print("Uspesna kupovina!")
    novac_na_racunu -= cena_proizvoda
    print(f"Novo stanje na racunu: {novac_na_racunu}")
else:
    print("Nemate dovoljno sredstava na racunu.")



# Kanban
# prikazujemo razlicitu boju taskova i raspored u zavisnosti od dana u nedelji

dan_u_nedelji = "ponedeljak"

if dan_u_nedelji == "ponedeljak":
    print("postavi boju na: crvenu")
elif dan_u_nedelji == "utorak":
    print("postavi boju na: zelenu")
elif dan_u_nedelji == "sreda":
    print("postavi boju na: zutu")
elif dan_u_nedelji == "cetvrtak":
    print("postavi boju na: plavu")
else:
    print("Postavi boju na: belu")


print("\nPrva sledeca linija")


broj = 10
#broj je veci od 0, broj je manj od nule, i broj je jednak nuli
if broj > 0:
    print("Broj je veci od 0")
elif broj == 0:
    print("Broj je jednak 0")
else: 
    print("Broj je manji od 0")


#ternarni operator
#light / dark tema
trenutna_tema = "dark"
#na sajtu primeni temu u skladu sa temom na racunaru korisnika

odabrana_tema_u_aplikaciji = "light" if trenutna_tema == "light" else "dark"
print(f"tema je: {trenutna_tema}")



#####################################################
uneti_broj = int(input("\nUnesite broj: "))
if uneti_broj % 2 == 0:
    print("Broj je paran")
else:
    print("Broj je neparan")