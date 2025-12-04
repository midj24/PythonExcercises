import random
# Potrosnja goriva i kretanje vozila

gorivo = 40
potrosnja = 5

while gorivo > 0:
    print("Voznja u toku")
    gorivo -= random.randint(6,15)
print(">> Nema vise goriva. Idi na pumpu")
