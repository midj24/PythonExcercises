############################################################################
print("Dobrodosli u proveru parnog broja! \nOvo je jednostavni test slucaj gde se proverava da li je uneti broj paran ili neparan.")
# trazimo od korisnika broj i proveravamo da li je paran broj
uneti_broj = int(input("Unesite broj: "))
# Proveravamo da li je uneti broj i paran broj
#print(uneti_broj % 2) # proveravam da li je deljiv sa 2
# broj je paran ako je ostatak pri deljenju sa 2 jednak 0
# == vraca True; != vraca False
ostatak_pri_deljenju_sa_dva = uneti_broj % 2
broj_je_paran = ostatak_pri_deljenju_sa_dva == 0 #true ili false
#print(broj_je_paran)

# test plan:
# test_broj 15
# ocekivano - nije paran broj - Rezultat: False
ocekivano = False
print("Neparni broj:", broj_je_paran == ocekivano)



#Test slucaj za parne brojeve:
# test_broj 16
# ocekivano - da je paran - Rezultat: True
ocekivano_2 = True
print("Parni broj:", broj_je_paran == ocekivano_2)

# Opis Bug-a
# Provera da li je broj paran
# Reprodukcija bug-a:
# 1. Unet je broj 16
# 2. Kilik na Enter
# Dobijeno: False - da broj nije paran
# Ocekivano: True - da broj je paran

# Proveravamo oba slucaja - Bug je ispravljen