print('H O T E L  D O S  A N I M A I S')
print(' ')
print('REGRAS')
print('• O rato não pode ficar ao lado do gato. \n• O cão não pode ficar ao lado do osso. \n• O gato não pode ficar ao lado do cão. \n• O queijo não pode ficar ao lado do rato')
print(' ')
print('Os quartos com * estão indisponíveis\nOs quartos com _ estão disponíveis' )
print(' ')
print('SÍMBOLOS')
print('G – GATO \nC – CÃO \nR – RATO \nO – OSSO \nQ – QUEIJO')
print(' ')
print('Especificando posições:\n[1,2,3,4]\n[5,6,7,8]')
print(' ')
print('Bem vindo a fase 1!')
print('')
print('Aloque o GATO e o RATO abaixo:')
print('')
print('[*,*,_,G]\n[R,_,*,*]')
p1 = int(input('Onde você quer alocar o gato?'))
p2 = int(input('Onde você quer alocar o rato?'))
while True:
    if p1 == 3 and p2 == 6:
        print('Parabéns, você passou de fase!')
        print('Bem vindo a fase 2!')
        print('Aloque CÃO, CÃO e OSSO abaixo:')
        print('')
        print('[_,*,*,*]\n[*,C,_,_]')
        p1 = int(input('Onde você quer alocar o primeiro cão?'))
        p2 = int(input('Onde você quer alocar o segundo cão?'))
        p3 = int(input('Onde você quer alocar o osso?'))

        while True:
            if p1 == 7 and p2 == 8 and p3 == 1 or p1 == 8 and p2 == 7 and p3 == 1:
                print('Parabéns, você passou de fase!')
                print('Bem vindo a fase 3!')
                print('Aloque GATO, RATO e OSSO abaixo:')
                print('')
                print('[_,*,*,*]\n[_,G,_,*]')
                p1 = int(input('Onde você quer alocar o GATO?'))
                p2 = int(input('Onde você quer alocar o RATO?'))
                p3 = int(input('Onde você quer alocar o osso?'))

                while True:
                    if p1 == 7 and p2 == 1 and p3 == 5:
                        print('Parabéns, você passou de fase!')
                        print('Bem vindo a fase 4!')
                        print('Aloque QUEIJO, QUEIJO e OSSO abaixo:')
                        print('')
                        print('[_,_,_,*]\n[*,R,*,*]')
                        p1 = int(input('Onde você quer alocar o primeiro QUEIJO?'))
                        p2 = int(input('Onde você quer alocar o segundo QUEIJO?'))
                        p3 = int(input('Onde você quer alocar o OSSO?'))

                        while True:
                            if p1 == 1 and p2 == 3 and p3 == 2 or p1 == 3 and p2 == 1 and p3 ==2:
                                print('Parabéns! Você ganhou o jogo!')
                                break
                            else:
                                print('Game over!')
                                break

                    else:
                        print('Game over!')
                        break

            else:
                print('Game over!')
                break
    else:
        print('Game over!')
        break









