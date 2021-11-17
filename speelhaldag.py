ticket = float(input            ('Hoeveel kost de ticket            : '))
# 7.45 euro
persoon = int(input             ('Hoeveel personen                  : '))
# 4 personen
GameseatPrijs = float(input     ('Hoeveel kost de gameseat          : '))
GameseatMinuten = int(input     ('Per hoeveel minuten               : '))
GameseatPrijsPerMinuut = GameseatPrijs/GameseatMinuten
# Gameseat prijs is 37 cent per 5 minuten
GameseatTijd = int(input        ('Hoeveel minuten in de gameseat    : ')) 
# 45 minuten
prijs = (ticket*persoon)+(GameseatPrijsPerMinuut*GameseatTijd*persoon)
print(prijs)
tekst ='Dit geweldige dagje-uit met '+ str(persoon)+' mensen in de Speelhal met '+str(GameseatTijd)+' minuten VR kost je maar '+ str(prijs)+' euro.'
print(tekst)