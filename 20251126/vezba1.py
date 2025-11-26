# definisanje specifikacija telefona iz vezbe
model = "iPhone 17 Pro Max" # string tip
proizvodjac = "Apple" # string tip
url_do_slike = "apple_slika.jpg"
cena = 1200 # int tip
popust = 0.2 #float tip
umanjenje = cena * 0.2
cena_popust = cena - umanjenje

#print("Proizvodjac: ", proizvodjac, "\nModel: ",model, "\nCena: ", cena,"€", "\nURL do slike: ",url_do_slike)
#ili ovo ispod sto je lakse za koriscenje
# \t predstavlja tab (uvlaku); \n predstavlja novi red
print(f"Proizvodjac:\t{proizvodjac}\nModel:\t{model}\nCena:\t{cena} €\nCena sa popustom:\t{int(cena_popust)} €\nLink do slike:\t{url_do_slike}")