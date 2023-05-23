from datetime import *
import time
import os

import Smalt_R1
import Smalt_R2
import Smalt_R3
import Smalt_R4
import Smalt_R5


def ripulisci():
    time.sleep(2)
    os.system("cls")

############################# contiene errore non stampa tutto
def stampa():
    file = open('oggetti_smaltiti.txt', 'r')
    riga_f = file.readline().replace("\n", " ")
    while riga_f:
        print(riga_f)
        riga_f = file.readline().replace("\n", " ")

    file.close()

def caratteristiche():
    lista_caratt = []
    var_contr = True
    while var_contr:
        ripulisci()
        try:
            peso = float(input("inserisci il peso in kg (la virgola indicala con il punto): "))
            peso = str(peso)+" Kg"

            var_contr = False
        except:
            print("!!! Errore !!!")
            print("Rinserisci le caratteristiche")
    
    print("Caratteristiche accetate")

    lista_caratt = [peso]
    return lista_caratt

def caso_num(scelta):
    file = open('oggetti_smaltiti.txt','a')
    oggi = datetime.today()
    ripulisci()

    match scelta:
        case 1:
            x = Smalt_R1.R1()
        case 2:
            x = Smalt_R2.R2()
        case 3:
            x = Smalt_R3.R3()
        case 4:
            x = Smalt_R4.R4()
        case 5:
            x = Smalt_R5.R5()

    #§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§
    if x == "e":
        ripulisci()
        x = Raggruppamenti()
        caso_num(x)

    ora = datetime.today()
    lista_caratt = caratteristiche()

    file.write(f"Ora: {ora}\n   Oggetto: {x}\n   Caratteristiche: {lista_caratt}\n\n")

    file.close()
    ripulisci()
    print("Oggetto smaltito")

def Raggruppamenti():
    while True:
        try:
            scelta= int(input("""
Scegli uno dei 5 raggruppamenti:    
                                1 - R1 Grande bianco freddo -grandi elettrodomestici per la refrigerazione: frigoriferi, 
                                    congelatori, condizionatori

                                2 - R2 Grande bianco non freddo -grandi elettrodomestici come lavatrici, 
                                    lavastoviglie

                                3 - R3 TV Monitor a tubo catodico

                                4 - R4 Elettronica di consumo, Telecomunicazioni, Informatica, piccoli elettrodomestici, 
                                    elettroutensili, giocattoli, apparecchi di illuminazione, dispositivi medici

                                5 - R5 Sorgenti luminose a scarica: lampade fluorescenti e sorgenti luminose compatte

scelta numero: """))   
            if scelta >= 1 and scelta <=5:
                print("Scelta accettata")
                return scelta
            
            print("!!! Errore !!!")
            print("Riprova a inserire un numero della categoria")
            ripulisci()

        except:
            print("!!! Errore !!!")
            print("Riprova a inserire un numero della categoria")
            ripulisci()

def scelta_generale():
    while True:
        try:
            scelta = int(input("""
Scelta: 
        1 - Butta la spazatura
        2 - Visualizza oggetti buttati

scelta numero: """))
            if scelta >= 1 and scelta <=2:
                print("Scelta accettata")
                return scelta
            
            print("!!! Errore !!!")
            print("Riprova a inserire un numero della categoria")
            ripulisci()

        except:
            print("!!! Errore !!!")
            print("Riprova a inserire un numero della categoria")
            ripulisci()
    

def main():
    scelta = scelta_generale()
    match scelta:
        case 1:
            ripulisci()
            x = Raggruppamenti()
            caso_num(x)
        case 2:
            ripulisci()
            stampa()

#############################################  PROGRAMMA PRINCIPALE  #############################################

fine = True
while fine:
    main()

    ripulisci()

    x = input("vuoi finire inserisci \"Y\" se no qualsiasi altro carattere: ").upper()
    if x == "Y":
        ripulisci()

        print("Fine del programma\n")
        print("Grazie per aver usato SmaltimentoRifiuti")

        fine = False
