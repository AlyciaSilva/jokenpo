#Jogo de pedra papel e tesoura
import random, emojis
def resultado (a,b):
    if lista[a] == b - 1:
        print(emojis.encode('Empate:exclamation::exclamation:'))
    elif lista [a] == lista[0] and escolha == 2: #usuário ganha
        print(emojis.encode('Parabéns:unamused:, você ganhou:rage:'))
    elif lista [a] == lista[1] and escolha == 1: #máquina ganha
        print(emojis.encode('Você perdeu:sunglasses::laughing::stuck_out_tongue_closed_eyes:!!'))        
    elif lista [a] == lista[2] and escolha == 1: #usuário ganha
        print(emojis.encode('Parabéns:unamused:, você ganhou:rage:'))
    elif lista [a] == lista[0] and escolha == 3:# máquina ganha
        print(emojis.encode('Você perdeu:sunglasses::laughing::stuck_out_tongue_closed_eyes:!!'))       
    elif lista [a] == lista[1] and escolha == 3:#usuário ganha
        print(emojis.encode('Parabéns:unamused:, você ganhou:rage:'))
    elif lista [a] == lista[2] and escolha == 2:#máquina ganha
        print(emojis.encode('Você perdeu:sunglasses::laughing::stuck_out_tongue_closed_eyes:!!'))       

print('Jogo de jokenpo')
print(emojis.encode('(1):fist:\n(2):hand:\n(3):v: '))
escolha = int(input('Pedra, papel ou tesoura? '))
if escolha != 1 and escolha != 2 and escolha != 3:
    print('Numero inválido')
else:
    lista = ['Pedra', 'Papel', 'Tesoura']
    sorteado = random.randint(0,2)
    resultado(sorteado,escolha)