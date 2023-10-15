#Jogo de pedra papel e tesoura
import random, emojis
def resultado (a,b):
    if a == b - 1:
        print(emojis.encode('Empate:exclamation::exclamation:'))
    elif (a == 0 and b == 2) or (a == 1 and b == 0) or (a == 2 and b == 1): #usuário ganha
        print(emojis.encode('Parabéns:unamused:, você ganhou:rage:'))
    else: #máquina ganha
        print(emojis.encode('Você perdeu:sunglasses::laughing::stuck_out_tongue_closed_eyes:!!'))   

print('Jogo de jokenpo')
print(emojis.encode('(1):fist:\n(2):hand:\n(3):v: '))
escolha = int(input('Pedra, papel ou tesoura? '))
if escolha != 1 and escolha != 2 and escolha != 3:
    print('Numero inválido')
else:
    lista = ['Pedra', 'Papel', 'Tesoura']
    sorteado = random.randint(0,2)
    print('Máquina: ', lista[1])
    resultado(sorteado,escolha)
    
