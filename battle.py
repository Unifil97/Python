from random import randint
red='\033[31m' #alustetaan värit
white='\033[37m'
green="\033[0;32m"
lauta = []


for i in range(6): #tehdään lauta 
    lauta.append(["O"] * 6)
   

def nayta(lauta):# functio näytä (lauta) ja numero rivien lisäys
    print("   ","  ".join("012345"))
    for i,rivi in  zip("012345",lauta) :    
        print(i," ","  ".join(rivi))
        

print("Laivan upotus")
def randomrivi(lauta):# arvotaan tietokoneen laivan paikka
    return randint(0, len(lauta)-1 )
def randomsarake(lauta):
    return randint(0, len(lauta[0])-1 )
laiva_rivi = randomrivi(lauta)
laiva_sarake = randomsarake(lauta)


nayta(lauta)
print("------------------")

#print(laiva_rivi,laiva_sarake) voidaan katsoa laivan paikka
for vuorot in range(8): 
    try:
            
            print ("Arvaus ", vuorot+1)
            print("---------------")
            
            rivi =  int(input("Anna rivi: "))
            sarake =  int(input("Anna sarake: "))
            
            if rivi == laiva_rivi and sarake == laiva_sarake :
                lauta[laiva_rivi][laiva_sarake] = green+ "X"+white
                print("____________")
                print("Voitit!")
                nayta(lauta)
                break
                
            # katsotaan että syötteet mahtuu kenttään
            if (rivi < 0 or rivi > 5) or (sarake < 0 or sarake > 5):
                    nayta(lauta)
                    print("Ei riittänyt kenttä")
                    print("---------------")
            # tarkistetaan onko arvattu jo
            elif(lauta[rivi][sarake] == red+ "X"+white):
                    nayta(lauta)
                    print("Arvattu jo")
                    print("---------------")
            else: #kun ammutaan ohi ilmoitus
                    lauta[rivi][sarake] = red+ "X"+white
                    nayta(lauta)
                    print("Ammuit ohi")
                    print("---------------")
                #lasketaan vuorot jos yli 8 lopetetaan ja näytetään laivan paikka            
            if vuorot == 8:       
                lauta[laiva_rivi][laiva_sarake] =(red+ "+"+white)
                nayta(lauta)
                print("Koneen laiva on ",laiva_rivi,",",laiva_sarake)
                print("Hävisit")
                vuorot =+ 1
                
                break   
    except ValueError:# virhe jos syöte on tyhjä tai kirjain
        nayta(lauta)
        print("Ei oo numero 0-5\nAarvaa uudestaan")
    continue #jatketaan vaikka tulee virhe

    

    

    
    
    

    
        
    

    