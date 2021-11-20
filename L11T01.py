"""Tehtävä L11T01 (2 pistettä)
Kysy käyttäjältä aika sekunteina kokonaislukuna, 
ja muuta se muotoon tunnit:minuutit:sekunnit
Esimerkiksi käyttäjä antaa luvun 10000, niin
ohjelma näyttää sen muodossa "2:46:40".
Kokeile ohjelmasi toimivuus vähintään viidellä eri arvolla."""
import datetime
sekunnit=int(input("Anna sekunnit "))
  
def convert(sekunnit):
    return str(datetime.timedelta(seconds = sekunnit))
      
print(convert(sekunnit))