import random


def retirar(baraja):
    random.shuffle(baraja)
    carta = baraja.pop()
    return carta


def suma(mano):
    a = False
    listasemas = []
    i = 0
    while i < len(mano):
        if mano[i] != 1:
            listasemas.append(mano[i])
            i += 1
        elif mano[i] == 1 and '1' not in listasemas:
            a = True
            for e in mano[i + 1:]:
                if mano[i] == e:
                    listasemas.append(e)
            i += 1
    sumatoriosemas = 0
    for g in listasemas:
        sumatoriosemas = sumatoriosemas + g
    if sumatoriosemas <= 10 and a == True:
        suma = sumatoriosemas + 11
    elif sumatoriosemas > 10 and a == True:
        suma = sumatoriosemas + 1
    else:
        suma = sumatoriosemas
    return suma


def mayorSuma(jugadores, dic_valores):
    sumatorias_jugadores = []
    for e in jugadores:
        sumatorias_jugadores.append(suma(dic_valores[e]))
    return max(sumatorias_jugadores)


def valor(carta):
    a = carta[1]
    if a == 'J' or a == 'Q' or a == 'K':
        a = 10
    elif a == 'A':
        a = 1
    else:
        a = int(carta[1])
    return a

n = input('Cuantas personas van a jugar?? ')
nv = n.isdigit()
while nv is False:
    print('Por favor digite un numero valido')
    n = input('Cuantas personas van a jugar?? ')
    nv = n.isdigit()
n = int(n)

jugadores = []
dic_saldo = {}

i = 0
while i < n:
    nombre = str(input('\nNombre del jugador: '))
    saldo = input('{}, Cuanto saldo tiene? '.format(nombre))
    saldov = saldo.isdigit()
    while saldov is False:
        print('Por favor digite un numero valido')
        saldo = input('{}, Cuanto saldo tiene? '.format(nombre))
        saldov = saldo.isdigit()
    saldo = int(saldo)

    jugadores.append(nombre)
    dic_saldo[jugadores[i]] = saldo
    i += 1

numeroBarajas = input('\nCuantas barajas??')
numeroBarajasv = numeroBarajas.isdigit()
while numeroBarajasv is False:
    print('Por favor digite un numero valido')
    numeroBarajas = input('Cuantas barajas?? ')
    numeroBarajasv = numeroBarajas.isdigit()
numeroBarajas = int(numeroBarajas)

numeros = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * numeroBarajas
naipes = ['♠', '♥', '♣', '♦'] * numeroBarajas
baraja = [[j + i, j] for i in naipes for j in numeros]

restaurar = False
jugar = True

while jugar:
    dic_cartas = {}
    dic_valores = {}
    dic_apuestas = {}
    valor_dealer = []
    cartas_dealer = []
    
    if restaurar == True:
        novo_baraja = input('Digite [1] para restaurar o baraja e [2] para manter: ')
        while novo_baraja != '1' and '2':
            novo_baraja = input('Digite [1] para restaurar o baraja e [2] para manter: ')

        if novo_baraja == '1':
            numeroBarajas = input('Cuantas barajas?? ')
            numeroBarajasv = numeroBarajas.isdigit()
            while numeroBarajasv is False:
                print('Por favor digite un numero valido')
                numeroBarajas = input('Cuantas personas van a jugar?? ')
                numeroBarajasv = numeroBarajas.isdigit()
            numeroBarajas = int(numeroBarajas)

            numeros = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * numeroBarajas
            naipes = ['♠', '♥', '♣', '♦'] * numeroBarajas
            baraja = [[j + i, j] for i in naipes for j in numeros]

    
    e = 0
    # Contador que revisa el saldo del diccionario de cada jugador
    while e < len(jugadores):
        apuesta = input('{}, Cuanto quiere apostar? '.format(jugadores[e]))
        apuesta = int(apuesta)
        while apuesta > dic_saldo[jugadores[e]] or apuesta <= 0:
            apuesta = int(input('Digite un valor posible: '))
        dic_apuestas[jugadores[e]] = apuesta
        e += 1

    if len(jugadores) < 1:
        break

    i = 0
    while i < len(jugadores):
        carta1 = retirar(baraja)
        carta2 = retirar(baraja)
        lista_valores = [valor(carta1), valor(carta2)]
        lista_cartas = [carta1[0], carta2[0]]
        dic_valores[jugadores[i]] = lista_valores
        dic_cartas[jugadores[i]] = lista_cartas

        """if suma(dic_valores[jugadores[i]]) == 21:
            print('BLACKJACK!.{}, Tiene 21'.format(jugadores[i]))
            dic_saldo[jugadores[i]] = dic_saldo[jugadores[i]] + dic_apuestas[jugadores[i]] * 1.5
            del (jugadores[i])
            i -= 1"""
        i += 1

    print("-"*50)
    print('Mano:{}.'.format(dic_cartas))

    # FEATURE LIVRE:CARTA VIRADA PARA CIMA DO DEALER
    baixo_dealer = retirar(baraja)
    cima_dealer = retirar(baraja)
    valor_dealer.append(valor(baixo_dealer))
    valor_dealer.append(valor(cima_dealer))
    cartas_dealer.append(baixo_dealer[0])
    cartas_dealer.append(cima_dealer[0])
    
    print('» Carta encima de dealer → {}\n'.format(cima_dealer[0]))

    i = 0
    while i < len(jugadores):
        continua = input('{}, digite [1] para pedir mas cartas o [2] para parar:'.format(jugadores[i]))
        while continua != "1" and continua != '2':
            print("No digito un valor valido!")
            continua = input('{}, digite [1] para pedir mas cartas o [2] para parar:'.format(jugadores[i]))

        if continua == '1':
            carta_extra = retirar(baraja)
            dic_valores[jugadores[i]].append(valor(carta_extra))
            dic_cartas[jugadores[i]].append(carta_extra[0])
            print('{}, Su nueva mano: {}'.format(jugadores[i], dic_cartas[jugadores[i]]))
            print('{} suma: {}'.format(jugadores[i],suma(dic_valores[jugadores[i]]) ))

            if suma(dic_valores[jugadores[i]]) > 21:
                print('{}, Se PASO!\n'.format(jugadores[i]))
                dic_saldo[jugadores[i]] = dic_saldo[jugadores[i]] - dic_apuestas[jugadores[i]]
                del (jugadores[i])
                break
            elif suma(dic_valores[jugadores[i]]) == 21:
                print('BLACKJACK!.{}\n    '.format(jugadores[i]))
                dic_saldo[jugadores[i]] = dic_saldo[jugadores[i]] + dic_apuestas[jugadores[i]] * 2
                del (jugadores[i])
                i -= 1
                break
        else:
            print('{} suma: {}'.format(jugadores[i],suma(dic_valores[jugadores[i]]) ))
            print("-"*50)
            i += 1

    if len(jugadores) > 0:
        while suma(valor_dealer) < 17:
            carta_extra_dealer = retirar(baraja)
            valor_dealer.append(valor(carta_extra_dealer))
            cartas_dealer.append(carta_extra_dealer[0])
        while suma(valor_dealer) < mayorSuma(jugadores, dic_valores):
            carta_extra_dealer2 = retirar(baraja)
            valor_dealer.append(valor(carta_extra_dealer2))
            cartas_dealer.append(carta_extra_dealer2[0])
        print('Nueva mano del dealer: {}.\nLa suma del dealer fue {}'.format(cartas_dealer,suma(valor_dealer)))

        for e in jugadores:
            if suma(valor_dealer) > 21:
                print('{}, GANO!'.format(e))
                dic_saldo[e] = dic_saldo[e] + dic_apuestas[e]
            elif suma(dic_valores[e]) < suma(valor_dealer) and suma(valor_dealer) <= 21:
                print('{}, PERDIO!'.format(e))
                dic_saldo[e] = dic_saldo[e] - dic_apuestas[e]
            elif suma(dic_valores[e]) == suma(valor_dealer):
                print('{}, EMPATO!'.format(e))

    print('-'*50 +'\nRESULTADOS')
    print('-'*50 +'\nManos de los jugadores:{}'.format(dic_cartas))
    print('Mano del dealer:{}'.format(cartas_dealer))
    print('Saldos:{}'.format(dic_saldo))

    e = 0
    while e < len(jugadores):
        if dic_saldo[jugadores[e]] <= 0:
            print('{}, No tiene saldo, Alguien desea ayudar a {}?'.format(
                jugadores[e], jugadores[e]))
            donar = str(input('Si si digite el nombre del jugador. Si no digite "no":'))
            if donar == 'no':
                print('{}, Mas suerte a la proxima!'.format(jugadores[e]))
                del (dic_saldo[jugadores[e]])
                del (jugadores[e])
                del (jugadores[e])
                e -= 1
            else:
                donacion = input('{}, Cuanto desea donar?:'.format(donar))
                donacionv = donacion.isdigit()
                while donacionv is False:
                    print('Digite un valor valido.')
                    donacion = input('Cuanto desea donar? ')
                    donacionv = donacion.isdigit()
                donacion = float(donacion)

                dic_saldo[jugadores[e]] = donacion
                dic_saldo[donar] = dic_saldo[donar] - donacion
            print('Saldos:{}'.format(dic_saldo))
        e += 1

    restaurar = True

    for e in jugadores:
        del (dic_apuestas[e])

    if len(jugadores) < 1:
        jugar = False

    continuar = str(input('Digite [1] para continuar a jugar e [2] para salir:'))
    if continuar == '2':
        jugar = False

print('--- BLACK JACK ---')