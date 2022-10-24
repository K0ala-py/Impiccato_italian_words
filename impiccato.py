import os
import random

# MODALITA

modalita = False
mod = int(input('Selezionare modalità:\n1- Giocatore Singolo\n2- Giocare in due\n---> '))
if mod == 2:
    parola = input('Quale parola vuoi far indovinare?\n---> ')
    modalita = True

if mod == 1:
    wordlist = int(input("Scegli wordlists:\n1- 1000 parole comuni\n2- 280000 parole complesse\n---> "))
    if wordlist == 1:
        wordlist = 'wordlists.txt'
        indice = 1159
    else:
        wordlist = 'wordlists_280000.txt'
        indice = 279893

    difficolta = int(input('1- Facile (3-5)\n2- Medio (6-13)\n3- Difficile (14-20)\n---> '))

    if difficolta == 1:
        difficolta_min = 3
        difficolta_max = 5

    if difficolta == 2:
        difficolta_min = 6
        difficolta_max = 13

    if difficolta == 3:
        difficolta_min = 14
        difficolta_max = 20


# PAROLA RANDOM
if mod == 1:
    file = open(f'{wordlist}','r')
    content = file.readlines()
def main():
    if mod == 1:
        while True:
            casuale = random.randint(0,indice)
            stringa = content[casuale]
            if len(stringa) > difficolta_min and len(stringa) < difficolta_max:
                break

    os.system('clear')

    if modalita:
        global parola
        stringa = parola
    if not modalita:
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
            if modalita:
                blocco = input('Invia per rigiocare!')
                os.system('clear')
                os.system('python3 impiccato.py')
            rifare = input('Rifare? [s/n]\n---> ')
            if rifare == 's':
                main()
            exit()
        # hai vinto
        if '_' not in parola:
            os.system('clear')
            tutto = ' '.join(parola)
            print(tutto)
            print("Hai vinto!")
            if modalita:
                blocco = input('Invia per rigiocare!')
                os.system('clear')
                os.system('python3 impiccato.py')
            rifare = input('Rifare? [s/n]\n---> ')
            if rifare == 's':
                main()
            exit()
        os.system('clear')

main()
