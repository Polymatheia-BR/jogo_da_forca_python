import random

#Respostas dos níveis e suas respectivas dicas
palavras_dicas = [["Eclipse","Astronomia"],["Risoto","Gastronomia"],["Balsa","Transporte"],["Python", "Linguagem de Programação"], ["Impressora", "Dispositivo"]]
#Aleatoriza os elementos da lista anterior
random.shuffle(palavras_dicas)
letras_digitadas = []
vidas = 6
nivel = 0
palavra_atual = list(len(palavras_dicas[nivel][0]) * '_')
boneco = [
'''
----------
|.         |
|.         @
|.        /|\\
|.         /\\
|.
''',
'''
----------
|.         |
|.         @
|.        /|\\
|.         /
|.
''',
'''
----------
|.         |
|.         @
|.        /|\\
|.         
|.
''',
'''
----------
|.         |
|.         @
|.        /|
|.         
|.
''',
'''
----------
|.         |
|.         @
|.         |
|.         
|.
''',
'''
----------
|.         |
|.         @
|.        
|.         
|.
''',
'''
----------
|.         |
|.         
|.        
|.         
|.
'''
]

#Checa e substitui caso encontre uma letra
def checar_letra(vidas):    
    achou = False    
    for x in range(len(palavras_dicas[nivel][0])):
        if jogador_input.upper() == palavras_dicas[nivel][0][x].upper():
            palavra_atual[x] = palavras_dicas[nivel][0][x]
            achou = True

    #Se não achar nenhuma letra, subtrai uma vida
    if achou == False:
        vidas -= 1

    return vidas

#Checa se ainda existem letras a serem achadas
def avancar_nivel(nivel,palavra_atual):
    proximo_nivel = True
    for x in range(len(palavras_dicas[nivel][0])):
        if palavra_atual[x] == '_':
            proximo_nivel = False

    return proximo_nivel

def mostrar_jogo():
    print(f'NIVEL: {nivel+1}')
    print(f'DICA: {palavras_dicas[nivel][1]}')
    print(f'VIDAS: {vidas}')
    print(boneco[vidas])
    print(f'PALAVRA: {"".join(palavra_atual)}')
    print(f'LETRAS DIGITADAS: {" ".join(letras_digitadas).upper()}')
    jogador_input = input('Digite uma letra: ')
    while len(jogador_input) > 1:
        jogador_input = input('Valor invalido! Digite apenas uma letra: ')
    print('----------')

    return jogador_input
    
#Loop principal do jogo
while True:
    if vidas == 0:
        print(boneco[vidas])
        print(f'Você perdeu')
        break
    
    jogador_input = mostrar_jogo()
    letras_digitadas = letras_digitadas + [jogador_input]
    vidas = checar_letra(vidas)

    #Avança para o proximo nivel
    if avancar_nivel(nivel, palavra_atual): 
        nivel += 1
        if nivel == 5:
            print(f'Você ganhou o jogo! Receba aqui seu premio 🏆')
            break
        palavra_atual = list(len(palavras_dicas[nivel][0]) * '_')
        vidas = 6
        letras_digitadas = []
        print(f'==========\nPROXIMO NÍVEL\n==========')

print(f'FIM DE JOGO')
