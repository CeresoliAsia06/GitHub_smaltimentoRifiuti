import time
import os

def ripulisci():
    time.sleep(2)
    os.system("cls")

def r1(oggetto):
    ripulisci()
    file = open('r1.txt', 'r')
    riga_f = file.readline().replace("\n", "")
    while riga_f:
        if oggetto == riga_f.lower():
            print("Ogetto accettato")
            file.close()
            return riga_f
        riga_f = file.readline().replace("\n", "")
    return False

def r2(oggetto):
    ripulisci()
    file = open('r2.txt', 'r')
    riga_f = file.readline().replace("\n", "")
    while riga_f:
        if oggetto == riga_f.lower():
            print("Ogetto accettato")
            file.close()
            return riga_f
        riga_f = file.readline().replace("\n", "")
    return False

def r3(oggetto):
    ripulisci()
    file = open('r3.txt', 'r')
    riga_f = file.readline().replace("\n", "")
    while riga_f:
        if oggetto == riga_f.lower():
            print("Ogetto accettato")
            file.close()
            return riga_f
        riga_f = file.readline().replace("\n", "")
    return False

def r4(oggetto):
    ripulisci()
    file = open('r4.txt', 'r')
    riga_f = file.readline().replace("\n", "")
    while riga_f:
        if oggetto == riga_f.lower():
            print("Ogetto accettato")
            file.close()
            return riga_f
        riga_f = file.readline().replace("\n", "")
    return False

def r5(oggetto):
    ripulisci()
    file = open('r5.txt', 'r')
    riga_f = file.readline().replace("\n", "")
    while riga_f:
        if oggetto == riga_f.lower():
            print("Ogetto accettato")
            file.close()
            return riga_f
        riga_f = file.readline().replace("\n", "")
    return False

def main():
    oggetto = input("inserisci l'oggetto da buttare: ").lower()
    if r1(oggetto) == False:
        if r2(oggetto) == False:
            if r3(oggetto) == False:
                if r4(oggetto) == False:
                    if r5(oggetto) == False:
                        return "Oggetto non trovato", None
                    else:
                        return r5(oggetto), "R5"
                else:
                    return r4(oggetto), "R4"
            else:
                return r3(oggetto), "R3"
        else:
            return r2(oggetto), "R2"
    else:
        return r1(oggetto), "R1"