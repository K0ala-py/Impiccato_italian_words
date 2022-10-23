from dataclasses import replace
import os
import time
import random

# PAROLA RANDOM
file = open('C:\\Users\\user\\Desktop\\Proggetti_Python\\altro\\passatempi\\impiccato\\wordlists.txt','r')
content = file.readlines()
while True:
    casuale = random.randint(0,1159)
    stringa = content[casuale]
    if len(stringa) > 5:
        print(stringa)
        break

os.system('cls')

stringa = stringa.replace('\n','')
lista = list(stringa)



# variabili e dati
parola = []
lunghezza = len(lista)
parola.append(stringa[0])
for i in range(len(lista)-2):
    parola.append('_')
parola.append(stringa[-1])
errori = []
errore = 0

x = 0
for i in parola:
    if lista[x] == stringa[0]:
        parola[x] = stringa[0]
    x+=1

x = 0
for i in parola:
    if lista[x] == stringa[-1]:
        parola[x] = stringa[-1]
    x+=1

# GIOCO
while True:
    print("Lettere errate: "+' '.join(errori))
    print("Errori: "+str(errore)+"/6")
    print('')
    tutto = ' '.join(parola)
    print(tutto)

    carattere_inserito = input("\nInserisci lettera ---> ")
    for carattere in lista:

        x = 0
        for i in parola:
            if lista[x] == carattere_inserito:
                parola[x] = carattere_inserito
            x+=1

        # carattere errato
        if carattere_inserito != carattere and (carattere_inserito not in errori and carattere_inserito not in parola):
            errore += 1
            errori.append(carattere_inserito)

    # hai perso
    if errore == 6:
        print("Hai perso!")
        print('LA PAROLA ERA: ',stringa)
        exit()
    # hai vinto
    if '_' not in parola:
        os.system('cls')
        tutto = ' '.join(parola)
        print(tutto)
        print("Hai vinto!")
        exit()
    os.system('cls')
    time.sleep(0.1)

