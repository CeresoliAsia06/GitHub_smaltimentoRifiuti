import time
import os

def ripulisci():
    time.sleep(2)
    os.system("cls")

def stampa():
    file = open('r1.txt', 'r')
    riga_f = file.readline().replace("\n", " ")
    while riga_f:
        print(riga_f)
        riga_f = file.readline().replace("\n", " ")
    file.close()

def R1():
    ripulisci()
    file = open('r1.txt', 'r')
    oggetto = input("inserisci l'oggetto da buttare: ")

    riga_f = file.readline().replace("\n", "")
    while riga_f:
        if oggetto.lower() == riga_f.lower():
            print("Ogetto accettato")
            file.close()
            return riga_f

        riga_f = file.readline().replace("\n", "")
    
    while True:
        file.close()
        file = open('r1.txt', 'r')
        ripulisci()
        print("!!! Errore !!!")
        print("Non trovato")
        ripulisci()

        stampa()

        oggetto_2 = input("\ninserisci l'oggetto da buttare dalla lista (oppure scrivi \"exit\" per uscire): ")
        if oggetto_2.lower() == "exit":
            return "e"
        
        riga_f_2 = file.readline().replace("\n", "")
        while riga_f_2:
            if oggetto_2.lower() == riga_f_2.lower():
                file.close()
                print("Ogetto accettato")
                return riga_f_2

            riga_f_2 = file.readline().replace("\n", "")