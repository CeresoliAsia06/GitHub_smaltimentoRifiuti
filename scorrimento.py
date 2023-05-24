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
            print("Oggetto accettato")
            file.close()
            return riga_f
        riga_f = file.readline().replace("\n", "")
    return False

def r2(oggetto):
    file = open('r2.txt', 'r')
    riga_f = file.readline().replace("\n", "")
    while riga_f:
        if oggetto == riga_f.lower():
            print("Oggetto accettato")
            file.close()
            return riga_f
        riga_f = file.readline().replace("\n", "")
    return False

def r3(oggetto):
    file = open('r3.txt', 'r')
    riga_f = file.readline().replace("\n", "")
    while riga_f:
        if oggetto == riga_f.lower():
            print("Oggetto accettato")
            file.close()
            return riga_f
        riga_f = file.readline().replace("\n", "")
    return False

def r4(oggetto):
    file = open('r4.txt', 'r')
    riga_f = file.readline().replace("\n", "")
    while riga_f:
        if oggetto == riga_f.lower():
            print("Oggetto accettato")
            file.close()
            return riga_f
        riga_f = file.readline().replace("\n", "")
    return False

def r5(oggetto):
    file = open('r5.txt', 'r')
    riga_f = file.readline().replace("\n", "")
    while riga_f:
        if oggetto == riga_f.lower():
            print("Oggetto accettato")
            file.close()
            return riga_f
        riga_f = file.readline().replace("\n", "")
    return False

def main():
    oggetto = input("inserisci l'oggetto da buttare: ").lower()
    v_r = r1(oggetto)
    if v_r == False:
        v_r = r2(oggetto)
        if v_r == False:
            v_r = r3(oggetto)
            if v_r == False:
                v_r = r4(oggetto)
                if v_r == False:
                    v_r = r5(oggetto)
                    if v_r == False:
                        return "Oggetto non trovato", None
                    else:
                        return v_r, "R5"
                else:
                    return v_r, "R4"
            else:
                return v_r, "R3"
        else:
            return v_r, "R2"
    else:
        return v_r, "R1"