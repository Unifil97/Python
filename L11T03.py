"""Tehtävä L11T03 (3 pistettä)
Tee ohjelma, joka kysyy oppilaitten nimiä niin kauan kunnes käyttäjä antaa tyhjän syötteen. 
Ohjelma kertoo tämän jälkeen montako nimeä annettiin ja 
näyttää ne yhtenä rivinä pilkulla erotettuna."""
lkm=0
nimet=""
while True:#jatketaan niin pitkään kun tosi
    nimi = input("Anna nimiä ")
    if (nimi==""):#jos tyhjä syöte
        print("Et antanut nimeä")       
        break
    nimet =nimet+nimi+","#erotellaan nimet pilkulla
    lkm += 1
print("Annoit ",lkm," nimeä ",nimet)#tulostetaan lukumäärä ja nimet