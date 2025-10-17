
'''movimentação pela casa'''
# sala | cozinha | banheiro | quarto | quintal

# Funções importantes :
import sys
import time

def escrita_lenta(texto, atraso) :
    for caractere in texto:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(atraso)
    return ''


# FORA
'''antes de entrar será necessario pegar uma chave - deve ser possivel interagi com a porta mesmo se a chave'''
''' objetos - caixa | planta | '''
print(f'{escrita_lenta('Você se aproxima da casa', 0.07)} {escrita_lenta('', 0.5)}')


# FRENTE DA CASA :
CHAVE_ENTRADA = None
NA_CASA = None
print(f'{escrita_lenta('Perto da porta você vê uma pequena planta e um tapete', 0.07)} {escrita_lenta(' ', 0.5)}')


while True and CHAVE_ENTRADA == None: # não se tem a chave para abrir a porta
    print(f'{escrita_lenta('O que você deseja fazer?', 0.07)} {escrita_lenta(' ', 0.5)}[PORTA] [VAZO DE PLANTA] [TAPETE] ', end='')
    frente_casa_escolha = input('→ ').lower()
    if frente_casa_escolha == 'porta' :
        print(f'{escrita_lenta('Você tenta gira a maçaneta da porta.', 0.07)} {escrita_lenta(' ', 0.5)} {escrita_lenta('A porta está trancada', 0.07)}')  
    elif frente_casa_escolha == 'tapete' :
        print(f'{escrita_lenta('Você levanta o tapete.', 0.07)} {escrita_lenta(' ', 0.5)} {escrita_lenta('Você não achou nada', 0.07)}')

    elif frente_casa_escolha == 'vazo' or 'vazo de planta' :
        CHAVE_ENTRADA = True
        print(f'{escrita_lenta('Você move o vazo,', 0.07)} {escrita_lenta(' ', 0.5)} {escrita_lenta('você achou uma', 0.07)} {escrita_lenta(' ', 0.5)} {escrita_lenta('CHAVE!', 0.07)}')
        print(f'{escrita_lenta('Você tem uma CHAVE', 0.07)} \n')
        break


while True and CHAVE_ENTRADA == True: # já pode aprir a porta
    print(f'{escrita_lenta('O que você deseja fazer?', 0.07)} {escrita_lenta(' ', 0.5)}[PORTA] [VAZO DE PLANTA] [TAPETE] ', end='')
    frente_casa_escolha = input('→ ').lower()
    if frente_casa_escolha == 'porta' and CHAVE_ENTRADA == True:
        print(f'{escrita_lenta('Você entou na casa', 0.07)} \n')
        NA_CASA = True
        break
    elif frente_casa_escolha == 'tapete' or 'vazo':
        print(f'{escrita_lenta('Não existem mais nada para se procurar', 0.07)} \n')


#  PRIMEIRO CÔMODO : CORREDOR | PORTAS
''' LOCAIS : SALA | BANHEIRO | COZINHA | QUARTO '''
''' aqui será apenas um local de volta '''
while NA_CASA == True :
    print(f'{escrita_lenta('Você está em um corredor com 4 portas', 0.07)} {escrita_lenta(' ', 0.5)}')
    print(f'{escrita_lenta('Para onde você gostaria de ir?', 0.07)} {escrita_lenta(' ', 0.5)}[SALA] [BANHEIRO] [COZINHA] [QUARTO] ', end='')
    CASA_COMODO = input('→ ').lower()
    print()
    break

# OBJETIVO : ENTRAR NO QUARTO
# sequência : cozinha → sala → banheiro → quarto
# objetos : comda → senha → chave

# COZINHA : COMIDA = True
''' local da comida - dentro de uma gaveta (resto ddas comidasc estão podres - o monstro não come)'''
COMIDA = None
COMIDA_ESTRAGADA = None
local_cozinha = None
while CASA_COMODO == 'cozinha':
    print(f'{escrita_lenta('Você entra na cozinha', 0.07)} {escrita_lenta(' ', 0.5)}')
    print(f'{escrita_lenta('Olhando ao redor é possivel ver alguns armários, uma mesa, uma geladeira e um forno', 0.07)} {escrita_lenta(' ', 0.5)}')
    print(f'{escrita_lenta('Investigar melhor?', 0.07)} {escrita_lenta(' ', 0.5)} [SIM] [NÃO] ', end='')
    ENTRADA_COZINHA = input('→ ').lower().replace('ã','a')

    while ENTRADA_COZINHA == 'sim' :
        print(f'{escrita_lenta('O que ver primeiro?', 0.07)} {escrita_lenta(' ', 0.5)} [ARMÁRIOS] [MESA] [GELADEIRA] [FORNO] ', end='')
        local_cozinha == input('→ ').lower()
        
        if local_cozinha == 'armario' :
            print(f'{escrita_lenta('Você abre o armário.', 0.07)} {escrita_lenta(' ', 0.5)} {escrita_lenta('A maioria das latas estão vazias, mas você ainda consegue achar uma que contenha comida', 0.07)} {escrita_lenta(' ', 0.5)}')
            print(f'{escrita_lenta('Você tem uma LATA DE COMIDA', 0.07)} \n',)
            COMIDA = True
            break

        if local_cozinha == 'mesa' :
            print(f'{escrita_lenta('Você aproxima da mesa.', 0.07)} {escrita_lenta(' ', 0.5)} {escrita_lenta('O chiero é horrivel!', 0.07)} {escrita_lenta(' ', 0.5)} {escrita_lenta('Tem alguns restos de comida, mas as moscas já comeram a maior parte', 0.07)}')
            print(f'{escrita_lenta('Deseja pegar esses restos?', 0.07)}{escrita_lenta(' ', 0.5)} [SIM] [NÂO] ', end='')
            ESCOLHA_ESTRAGADA = input('→ ').lower().replace('ã','a')
            if ESCOLHA_ESTRAGADA == 'sim' :
                ESCOLHA_ESTRAGADA = True
                print(f'{escrita_lenta('Você possui COMIDA ESTRAGADA')}')
            if ESCOLHA_ESTRAGADA == 'nao' :
                ...
            break

        if local_cozinha == 'geladeira' :
            print(f'{escrita_lenta('', 0.07)}')
            break

        if local_cozinha == 'forno' :
            print(f'{escrita_lenta('Você abre o forno', 0.07)} {escrita_lenta(' ', 0.5)} {escrita_lenta(' ', 0.07)}')   
            break

    while ENTRADA_COZINHA == 'nao':
        print('')
        break
    break




    # SALA : CODIGO = True
    ''' local do coigo → COMIDA = True (necessário)'''
    ''' caso a pessoa fique dando muita comida para o bixo seria legal ter um limite - ou ele some após comer'''
    CODIGO = None
    while CASA_COMODO == 'sala' :
        if COMIDA == True :
            CODIGO = True
            ...

        elif COMIDA == None :
            ...




    # BANHEIRO : CHAVE = True
    ''' caixa com senha - código de desbroqueio na sala '''
    ''' local da cave → CODIGO = True (necessário)'''
    CHAVE = None
    while CASA_COMODO == 'banheiro' :
        if CODIGO == True :
            ...
        if CODIGO ==  None :
            ...




    # QUARTO :  
    ''' previamente tracado → chave no banheiro dentro de uma caixa '''
    ''' CHAVE = True (necessário) '''
    while CASA_COMODO == 'quarto' :
        if CHAVE == True :
            ...
