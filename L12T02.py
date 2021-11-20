"""Tehtävä L12T02 (2 pistettä)
Tee luokka Cat. Tee luokalla on kaksi ominaisuutta name ja color, sekä yksi metodi miau. 
Luo Cat-luokasta vähintään kaksi erilaista kissa-oliota. 
Näytä kissa-olioiden ominaisuudet konsolille, laita kissat myös naukumaan."""

class Cat:
    def __init__(self,name="",  color=0):
        self.name =name       
        self.color = color
        
        
    # muunnetaan stringiksi
    def __str__(self):
        return "Kissan nimi on "+self.name + " väriltään " +  self.color+" ja sanoo"

    name = ""   
    color = ""

    def miau(self):#metodi miau()
     return "miau"   
    

kissa = Cat("Katti", "punainen")

kissa2 = Cat("Matti","musta")


# tulosta kissat ja kutsutaan miau()
print(kissa,"",kissa.miau())
print(kissa2,"",kissa2.miau())
