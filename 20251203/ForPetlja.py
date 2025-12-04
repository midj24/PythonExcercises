import time

for x in range(10):
    print("Hello", x)
    print("*******")

print("Prva sledeca linija\n")

pocetna_godina = 2010
krajnja_godina = 2025
print("**********Dozvoljene godine**********")
for godina in range(pocetna_godina, krajnja_godina + 1):
    print(godina)
print("************************************\n")


#tablica mnozenja
# opseg brojeva do unetog broja (1,2,3,4,5) pomnoziti sa 1, 2, 3
# broj = int(input("Unesite broj: "))
# print("1\t2\t3\t")
# print(20*"*")
# for x in range (1, broj + 1):
#     print(f"{x*1}\t{x*2}\t{x*3}")
# print(20*"*")



#Stampati samo parne brojeve - simulacija continue
for broj in range(10):
    if broj % 2 != 0:
        continue
    print(broj)