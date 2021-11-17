AantalCroissant = int(input         ('Hoeveel croissant         : '))
#het waren 17 croissants
AantalStokbrood = int(input         ('Hoeveel stokbroden        : '))
#het waren 2 stokbroden
AantalKortingsbon = int(input       ('Hoeveel kortingsbonnen    : '))
#het waren 3 kortingsbonnen
PrijsCroissant = float(input        ('Prijs croissant           : '))
#0.39 euro
PrijsStokbrood = float(input        ('Prijs stokbrood           : '))
#2.78 euro
PrijsKortingsbon = float(input      ('Prijs kortingsbon         : '))
#0.50 euro
prijs = (AantalCroissant*PrijsCroissant)+(AantalStokbrood*PrijsStokbrood)-(AantalKortingsbon*PrijsKortingsbon)
print (prijs)
tekst='De feestlunch kost je bij de bakker '+str(prijs)+' euro voor de '+str(AantalCroissant)+" croissantjes en de "+str(AantalStokbrood)+' stokbroden als de '+str(AantalKortingsbon)+' kortingsbonnen nog geldig zijn!'
print (tekst)