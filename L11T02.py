"""Tehtävä L11T02 (2 pistettä)
Tee ohjelma, joka kysyy käyttäjältä ensin muutetaanko fahrenheitit celsiuksiksi vai 
celsius-asteet fahrenheitiksi. Tämän jälkeen kysytään käyttäjältä asteet ja 
muutetetaan ne toisiin asteisiin ja näytetään tulos käyttäjälle."""

kysy=input("Mihin muutetaan f=fahrenheit c=celsius ")
if (kysy == "f"):
 fasteet=int(input("Anna fahrenheit asteet "))
 celsius = (fasteet - 32) * 5.0/9.0
 print(fasteet,"fahrenheit =",round(celsius,2)," celsius astetta")   
elif (kysy == "c"):
 casteet=int(input("Anna celsius asteet "))
 fahrenheit = 9.0/5.0 * casteet + 32
 print(casteet,"celciusta =",round(fahrenheit,2)," fahrenheit astetta")
else:
    print("Anna kirjain f tai c")

