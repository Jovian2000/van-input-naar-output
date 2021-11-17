# Jovian Kartiko
# Pizza Calculator
small = 7.99
medium = 9.99
large = 10.99
# hier heb ik van elke formaat een variabel gemaakt en bepaald hoeveel de prijs is van elk formaat
print ("Pizzaria Jovi")
print ("small   : 7.99")
print ("medium  : 9.99")
print ("large   : 10.99")
# hier laat ik aan de gebruiker zien wat de prijzen zijn
s = int(input("Hoeveel small pizza's wilt u? "))
m = int(input("Hoeveel medium pizza's wilt u? "))
l = int(input("Hoeveel large pizza's wilt u? "))
# van line 12 tot en met 14 kies je hoeveel pizza's je wilt bestellen per formaat
print ("U heeft besteld")
print (str(s) + " small pizza's")
print (str(m) + " medium pizza's")
print (str(l) + " large pizza's")
# hier laat de app zien wat je allemaal hebt besteld
prijs = (small * s) + (medium * m)  + (large * l)
# hier word de totale prijs berekend
print ("Totaal: " + str(prijs) + " euro's") 

