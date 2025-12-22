# ATM modul

Omogucava korisniku interakciju sa bankovnim racunom
![bankomat_slika](https://investinatmmachines.com/wp-content/uploads/2024/04/Different-Types-of-ATMs-for-Business.jpg)

## Funkcionalnosti
- Provera stanja
- Podizanje novca
- Uplata novca

# Metod za podizanje novca
Ulazni parametri:
- Iznos

Povratna vrednost:
- True/False - u zavisnosti od uspesnosti 

`    def podigni_novac (self, iznos):
        if iznos >= self.stanje:
            self.stanje -= iznos
            return True
        return False
    `
## Scenariji
### Podizanje novca  - uspesan slucaj
- Pocetno stanje: 10.000
- Zahtev za podizanje: 2.000
- Ocekivani rezultat:
    - Transakcija uspesna (True)
    - Novo stanje: 8.000


## Kodovi gresaka
| Kod  | Opis                         |
|------|------------------------------|
| E001 | Nedovoljno sredstava         |
| E002 | Nevalidan iznos              |
| E003 | Nedovoljno novca u bankomatu |