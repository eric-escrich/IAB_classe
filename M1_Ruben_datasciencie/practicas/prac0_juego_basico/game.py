import random
import os

class RangeError(Exception):
    pass

menu = '''\nSelecciona un joc:
    1. Adivina número
    2. Pedra - Paper - Tisores
    3. Ahoracado
    4. Sortir'''

menuPedraPaperTisores = '''\nSelecciona una opció:
    1. Pedra
    2. Paper
    3. Tisores'''

def validateOpc(validOptions):
    optionOk = False
    while not optionOk:
        try:
            option = int(input('\n -> '))
            if option in validOptions:
                optionOk = True
            else:
                print('Opció no vàlida')
        except ValueError:
            print('Si us plau, introdueix un número vàlid.')
    return option

def adivinarNumero():
    print('\nBenvingut al joc de l\'Adivina número!!!')
    print('\nHas d\'endevinar un número entre 1 i 10 en 3 intents.\nPer cada error es mostrarà per pantalla si el número és major o menor a l’indicat.')
    randomNum = random.randint(1, 10)
    intents = 0
    isGuess = False

    while intents != 3 and not isGuess:
        intents += 1
        print('\nIntrodueix un número entre 1 i 10:')
        endevina = validateOpc([i for i in range(1, 11)])

        if endevina == randomNum:
            isGuess = True
        elif endevina < randomNum:
            print('\nEl número a endevinar és major')
        else:
            print('\nEl número a endevinar és menor')
    
    if isGuess:
        print(f'\nFelicitats, has encertat!!!')
    
    else:
        print(f'\nHas esgotat els 3 intents. El número a endevinar era {randomNum}')

    input('\nPrem una tecla per continuar...')  

def piedraPapelTijeras():
    print('\nBenvingut al joc de Pedra, Paper, Tisores!!!\nGuanya el primer que guanyi 3 partides.')
    opcions = ['Pedra', 'Paper', 'Tisores']
    validOptions = [1, 2, 3]
    ptsUser = 0
    ptsCpu = 0

    while ptsCpu != 3 and ptsUser != 3:
        print(f'\nPuntuació: Usuari {ptsUser} - Ordinador {ptsCpu}')
        randomNum = random.randint(0, 2)
        print(menuPedraPaperTisores)
        opcio = validateOpc(validOptions)
        opcio -= 1
        print(f'\nHas seleccionat {opcions[opcio]}')
        print(f'L\'ordinador ha seleccionat {opcions[randomNum]}')

        if opcio == randomNum:
            print('Empat')
        elif opcio == 0 and randomNum == 2:
            print('Sumes un punt!!!')
            ptsUser += 1
        elif opcio == 1 and randomNum == 0:
            print('Sumes un punt!!!')
            ptsUser += 1
        elif opcio == 2 and randomNum == 1:
            print('Sumes un punt!!!')
            ptsUser += 1
        else:
            print('L\'ordinador suma un punt !!!')
            ptsCpu += 1
    
    if ptsUser == 3:
        print(f'\nPuntuació: Usuari {ptsUser} - Ordinador {ptsCpu}')
        print('Has guanyat el joc!!!')
    else:
        print(f'\nPuntuació: Usuari {ptsUser} - Ordinador {ptsCpu}')
        print('Has perdut el joc!!!')
    
    input('\nPrem una tecla per continuar...')

def ahoracado():   
    try:
        words = open("paraules.txt","r")
    except Exception as e:
        print('No existeix l\'arxiu paraules.txt a la carpeta del programa') 
    else:
        lines = [line.strip() for line in words]
        words.close()
        word = random.choice(lines)
        wordToGuess = ['_' for letter in word]
        inputLetters = []

        print('\nBenvingut al joc de l\'Ahoracado!!!')
        print(f'Tens {len(word)*2} intents per endevinar la paraula')
        print(f'La paraula té {len(word)} lletres')

        for i in range(len(word)*2):
            print('\n' + ''.join(wordToGuess))

            if '_' not in wordToGuess:
                break

            print(f'\nIntents restants: {len(word)*2 - i}')
            while True:
                letter = input('\nDigues una lletra: ')
                if len(letter) == 1:
                    break
                else:
                    print('Introdueix una sola lletra')

            if letter in inputLetters:
                print('Ja has introduït aquesta lletra')
                continue
            
            inputLetters.append(letter)

            if letter in word:
                print('La lletra està a la paraula!')
                for i in range(len(word)):
                    if word[i] == letter:
                        wordToGuess[i] = letter

            else:
                print('La lletra no està a la paraula!')

        if '_' in wordToGuess:
            print(f'\nHas esgotat els {len(word)*2} intents. La paraula era {word}')
        else:
            print('\nHas guanyat!!!')

    input('\nPrem una tecla per continuar...')

def main():
    print('BENVINGUT A LA PRÀCTICA 1!!!')
    while True:
        print(menu)
        validOptions = [1, 2, 3, 4]
        option = validateOpc(validOptions)
        if option == 1:
            adivinarNumero()
        elif option == 2:
            piedraPapelTijeras()
        elif option == 3:
            ahoracado()
        elif option == 4:
            print('Adéu!!!')
            break

main()

