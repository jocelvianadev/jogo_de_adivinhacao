""""
POR JOCEL VIANA
11/04/2024

JOGO DE ADIVINHAÇÃO:

O JOGO FUNCIONARÁ DA SEGUINTE MANEIRA: O JOGO VAI PROPOR UMA PALAVRA SECRETA QUALQUER E VAI DA A POSSIBILIDADE
PARA O USUÁRIO DIGITAR APENAS UMA LETRA. QUANDO ELE DIGITAR A LETRA, O JOGO CONFERE SE A LETRA DIGITADA ESTÁ
NA PALAVRA SECRETA.

    ° SE A LETRA DIGITADA ESTIVER NA PALVRA SECRETA, O JOGO EXIBE A LETRA.
    ° SE NÃO ESTIVER, EXIBE UM ASTERISCO (*)

ALÉM DISSO, O JOGO FARÁ A CONTAGEM DE TENTATIVAS DO USUÁRIO.

"""
import os

palavra_secreta = 'maionese'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Por favor, digite apenas uma letra')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(f'\nPalavra formada: {palavra_formada}')

    if palavra_formada == palavra_secreta:
        os.system('cls') # Limpar o terminal
        print(f'Parabéns, você completou a palavra secreta!')
        print(f'A palavra era {palavra_secreta}')
        print(f'Tentativas: {numero_tentativas}')
        break

print("Fim de jogo")







































