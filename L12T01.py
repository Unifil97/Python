"""Tehtävä L12T01 (2 pistettä)
Tee luokka Human. Luokalla on kaksi ominaisuutta name ja age. 
Luo Human-luokasta kaksi olioita, 
joitten arvot asetat. Tulosta olioiden tiedot konsolille"""


class Human:
    #luokan muodostaja
    def __init__(self,name="",  age=0):
        self.name =name       
        self.age = age
        
    # muunnetaan stringiksi
    def __str__(self):
        return self.name + " " +  str(self.age) +" vuotta "

    name = ""   
    age = 0   
    #oliot ukko ja ukko2 luokasta Human
ukko = Human("Epäkesko Esko", 10)

ukko2 = Human("Iippa Vinetto",93)

# tulosta ukot
print(ukko)
print(ukko2)




