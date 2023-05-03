from random import randint
from time import sleep

num = randint(0,100)
answer = int(input('Chute um valor de 0 até 100: '))
ok = 'ok'

while ok == 'ok':
    if answer == num:
        print('Você acertou, parabéns!')
        sleep(1)
        ok = str(input('Gostaria de tentar novamente? [S/N]: ')).upper().strip()
        if ok == 'S':
            sleep(1)
            print('Então vamos lá :D')
            num = randint(0,100)
            sleep(1)
            answer = int(input('Chute um valor de 0 até 100: '))
            sleep(1)
            ok = 'ok'
        elif ok == 'N':
            ok = '#'
    elif answer > num:
        answer = int(input('Foi um bom chute, mas tente um número MENOR: '))
    else:
        answer = int(input('Foi um bom chute, mas tente um número MAIOR: '))

sleep(1)
print('Que pena, até a próxima então :/')
sleep(1)
print('Não esqueça de testar também os outros')
sleep(1)
print('Disponíveis no meu GitHub')

sleep(1.5)