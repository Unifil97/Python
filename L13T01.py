"""Tehtävä A
Toteuta ohjelma, joka kysyy käyttäjältä autojen rekisterinumeroita 
(siis esim 'ABC-123' jne) ja tallentaa ne listaan. 
Käyttäjä voi syöttää niin monta rekisterinumeroa kuin haluaa, 
syöttäminen lopetetaan tyhjällä syötteellä. 
Näytä syötetyt rekisterinumero aakkosjärjestyksessä."""

reknro=[]
while True:
    nro = input("Anna rekisterinumero: ")
    if nro != "":
        reknro.append(nro)
    else:
        break
    reknro.sort()
print("Rekkarinumerot =",",".join(reknro))
    
    
        
        
    
