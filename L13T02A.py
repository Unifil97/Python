"""Tehtävä L13T02 (3 pistettä)

Tehtävä A
Tee ohjelma joka kysyy käyttäjältä kurssien arvosanoja 
(arvosana on kokonaisuluku 0,1,2,3,4 tai 5) ja tallentaa ne listaan. 
Käyttäjä voi syöttää niin monta kurssiarvosanaa kuin haluaa, 
syöttäminen lopetetaan tyhjällä syötteellä. 
Näytä lopuksi montako arvosanaa käyttäjä antoi ja arvosanojen keskiarvo."""
keskiarvo=0
lista = []
try:     
    while True:		    
        number = int(input("Anna numero "))

        if int(number in range(0,6)):#numero väliltä 0-5
          
            lista.append(number)
           # keskiarvo=sum(lista)/len(lista)    
            
        else :   #jos numero ei ole 0-5         
            print("Anna numero välitä 0-5 muita ei lasketa ")
            continue       		     
	# jos tyhjä syöte tulostetaan lista ja keskiarvo
except :
	
	keskiarvo=sum(lista)/len(lista)# laskrtaan keskiarvo
print("Arvosanat =",lista," ja keskiarvo = ",keskiarvo)

		
                