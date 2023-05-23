from datetime import *
import time
import os

import Smalt_R1
import Smalt_R2
import Smalt_R3
import Smalt_R4
import Smalt_R5

import scorrimento


def ripulisci():
    time.sleep(2)
    os.system("cls")

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
            cat = "R1"
        case 2:
            x = Smalt_R2.R2()
            cat = "R2"
        case 3:
            x = Smalt_R3.R3()
            cat = "R3"
        case 4:
            x = Smalt_R4.R4()
            cat = "R4"
        case 5:
            x = Smalt_R5.R5()
            cat = "R5"

    if x == "e":
        ripulisci()
        x, cat = non_sai_dove()
        print(f"L'oggetto va smaltito in categoria: {cat}")
        tmp = input("Continua... ")

    ora = datetime.today()
    lista_caratt = caratteristiche()

    file.write(f"Ora: {ora}\n   Oggetto: {x}\n   Categoria: {cat}\n   Caratteristiche: {lista_caratt}\n\n")

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

def sai_dove():
    while True:
        scelta= input("""
Sai dove si smaltisce:
                        Y - So dove si smaltisce
                        N - Non  so dove si smaltisce
Scelta: """).upper()
        if scelta == "Y":
            print("Scelta accettata")
            return True
        elif scelta == "N":
            print("Scelta accettata")
            return False
        else:
            print("!!! Errore !!!")
            print("Riprova a inserire Y/N")
            ripulisci()

def non_sai_dove():
    ripulisci()
    oggetto, cat = scorrimento.main()
    if oggetto == "Oggetto non trovato":
        print("!!! Errore !!!")
        print("Oggetto non trovato")
        ripulisci()
        main()

    return oggetto, cat

def scelta_generale():
    while True:
        try:
            scelta = int(input("""
Scelta: 
        1 - Smaltisci rifiuto
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
            x = sai_dove()
            if x:
                x = Raggruppamenti()
                caso_num(x)
            else:
                file = open('oggetti_smaltiti.txt','a')
                oggi = datetime.today()
                
                ripulisci()
                x, cat = non_sai_dove()
                print(f"L'oggetto va smaltito in categoria: {cat}")
                tmp = input("Continua... ")

                ora = datetime.today()
                lista_caratt = caratteristiche()

                file.write(f"Ora: {ora}\n   Oggetto: {x}\n   Categoria: {cat}   Caratteristiche: {lista_caratt}\n\n")
                file.close()
        case 2:
            ripulisci()
            stampa()
            x = input("\nContinua... ")

#############################################  PROGRAMMA PRINCIPALE  #############################################

fine = True
while fine:
    main()

    ripulisci()
    x = input("Vuoi finire inserisci \"Y\" se no qualsiasi altro carattere: ").upper()
    if x == "Y":
        ripulisci()

        print("Fine del programma\n")
        print("Grazie per aver usato SmaltimentoRifiuti")

        fine = False
