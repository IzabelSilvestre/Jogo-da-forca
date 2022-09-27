
import os
import random

nome = input ("Olá! Qual é o seu nome?")
print (f'Seja Bem vindo(a) {nome} ! Vamos jogar Forca?' ) 
input ('\nPressione enter para dar start')
os.system('cls')

lista_de_palavras = ['gato', 'cachorro', 'dromedário', 'raposa']
palavra_selecionada = random.choice (lista_de_palavras).upper()
tamanho_palavra = len(palavra_selecionada)
palavra_codificada = ['_']*tamanho_palavra
quantidade_de_erros = 0

while '_' in palavra_codificada and quantidade_de_erros < 6: 
    print (f'\nSua palavra tem {tamanho_palavra} letras, o tema é animais')
    print (f'Erros: {quantidade_de_erros} de 6')
    for letra in palavra_codificada:
        print (letra , end = ' ')
    print()


    letra_escolhida = input ('Digite uma letra: ').upper()
    acertou = False
    for i in range(len(palavra_selecionada)):
         if letra_escolhida == palavra_selecionada[i]:
            palavra_codificada [i] = letra_escolhida
            acertou = True

    if acertou == True:
        print("Parabéns, acertou! Você não merece palmas, merece o Tocantins inteiro.")
    else:
        print("Errou feio, errou rude! Essa letra não tem na palavra")
        quantidade_de_erros = quantidade_de_erros + 1

if quantidade_de_erros == 6:
    print ('PERDEUUU!!!😦')
else: print ('PERD.... ah, você ganhou 🫠')

print(f'A palavra era: {palavra_selecionada}')