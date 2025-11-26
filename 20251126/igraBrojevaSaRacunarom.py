import random

print("🎲 Dobrodošli u igru pogađanja broja!")
print("Pokušajte pogoditi broj koji je računar zamislio (od 1 do 10).")

# Generisanje broja
broj_od_racunara = random.randint(1, 10)

# Validacija unosa
while True:
    try:
        korisnikov_broj = int(input("Unesite broj od 1 do 10: "))
        if 1 <= korisnikov_broj <= 10:
            break
        else:
            print("❗ Molimo unesite broj u opsegu 1-10.❗")
    except ValueError:
        print("❗❗ Unos mora biti ceo broj.")

# Provera pogodka
if korisnikov_broj == broj_od_racunara:
    print(f"✅ Pogodili ste! Računar je izabrao {broj_od_racunara}.")
else:
    print(f"❌ Niste pogodili. Vaš broj: {korisnikov_broj}, Računar: {broj_od_racunara}.")
