email_u_bazi = "korisnik@gmail.com"
password_u_bazi = "12345"

uneti_email = "korisnik@gmail.com"
uneti_password = "12345"

print(email_u_bazi == uneti_email) # rezultat je True ili False
print(uneti_password == password_u_bazi) # rezultat je True ili False

# and operater u pythonu je samo 'and'
# rezultat ove provere znaci da ce biti True samo ako su obe provere tacne
print(email_u_bazi == uneti_email and uneti_password == password_u_bazi)

# or operator je u pythonu 'or'
# rezultat ove provere znaci da je dovoljno barem jedan izraz tacan
print(email_u_bazi == uneti_email or uneti_password == password_u_bazi)

#primer - registracija
# unesite email adresu ili broj telefona
email = ""
broj_telefona = "0644444444"
print(email != "" or broj_telefona != "" )

# not operator je u pythonu 'not'
imao_uplatu = False
#korisnik izvrsava transakciju
imao_uplatu = not imao_uplatu

# binarni brojevi
broj = 3
print(broj)
print(bin(broj))
print(3 & 2)