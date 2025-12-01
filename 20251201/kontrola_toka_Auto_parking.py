pozicija_automobila = 0
pozicija_parkinga = 30
brzina_automobila = 10

pozicija_automobila += 10
print(pozicija_automobila)
if pozicija_automobila == pozicija_parkinga:
    print("Automobil je stigao na parking")
else: 
    pozicija_automobila += brzina_automobila
    if pozicija_automobila == pozicija_parkinga:
        print("Stigli ste na parking")
    else:
        pozicija_automobila += brzina_automobila
        if pozicija_automobila == pozicija_parkinga:
            print("Stigli ste na parking")
        else:
            pozicija_automobila += brzina_automobila


print("izvrsava se u svakom slucaju")