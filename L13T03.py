"""Tehtävä L13T03 (4 pistettä)
Toteuta ohjelma, johon voi tallentaa kymmenen eri auton tiedot. 
Kustakin autosta tiedetään rekisterinumero (esim ABC-123) ja autonmerkki (esim Skoda). 
Keksi itse erilaisia rekisterinumeroita ja automerkkejä. 
Tallenna tiedot valitsemaasi kokoelmaan. 
Tulosta sen jälkeen autojen tiedot ensin aakkosjärjestyksssä automerkin mukaan, 
ja sen jälkeen aakkosjärjestyksessä rekisterinumeron mukaan."""
autot = {}
for i in range(10):
    merkki = input("Auton merkki ")

    rekkari = input("Reknro ")

    autot[ merkki] = rekkari
    

print(dict(sorted(autot.items())))# tulostus merkin mukaan
print(sorted(autot.items(), key =
             lambda kv:(kv[1], kv[0])))# tulostus rekkarin mukaan
    
            





    
