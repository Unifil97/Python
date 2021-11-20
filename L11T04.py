"""Tehtävä L11T04 (3 pistettä)
Mäkihypyssä käytetään viittä arvostelutuomaria. 
Kirjoita ohjelma, joka kysyy arvostelupisteet yhdelle hypylle ja tulostaa 
tyylipisteiden summan siten, 
että summasta on vähennetty pois pienin ja suurin tyylipiste."""

pisteet=[]

i = 1 #alustetaan i jotta saadaan numerot alkamaan ykkösestä
while i < 6:
    piste =int (input("Anna pisteet " + str(i)+ ": "  ))  #loopataan numero kyselyä 5 kertaa                                 
    pisteet.append(piste)
    i=1+i #kasvatetaan i aina yhdellä
pisteet.remove(max(pisteet))#poistetaan suurin piste
pisteet.remove(min(pisteet))#poistetaan pienin piste
    
print("Arvostelupisteet = ",sum(pisteet))#tulostetaan pisteiden summa
