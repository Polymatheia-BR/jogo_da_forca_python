#Respostas dos níveis e suas respectivas dicas
palavras_dicas = [["Eclipse","Astronomia"],["Risoto","Gastronomia"],["Balsa","Transporte"],["Python", "Linguagem de Programação"], ["Impressora", "Dispositivo"]]
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



while True:
    if vidas == 0:
        print(boneco[vidas])
        print(f'Você perdeu')
        break
    
    print(f'NIVEL: {nivel+1}')
    print(f'DICA: {palavras_dicas[nivel][1]}')
    print(f'VIDAS: {vidas}')
    print(boneco[vidas])
    print(f'PALAVRA: {"".join(palavra_atual)}')
    print(f'LETRAS DIGITADAS: {" ".join(letras_digitadas).upper()}')
    letra = input('Digite uma letra: ')
    letras_digitadas = letras_digitadas + [letra]
    print('----------')
    
    #Checa e substitui caso encontre uma letra    
    achou = False    
    for x in range(len(palavras_dicas[nivel][0])):
        if letra.upper() == palavras_dicas[nivel][0][x].upper():
            palavra_atual[x] = palavras_dicas[nivel][0][x]
            achou = True
            
    if achou == False:
        vidas -= 1

    #Checa se ainda existem letras a serem achadas
    proximo_nivel = True
    for x in range(len(palavras_dicas[nivel][0])):
        if palavra_atual[x] == '_':
            proximo_nivel = False

    if proximo_nivel == True: #Avança para o proximo nível se não encontrar undeline
        nivel += 1
        if nivel == 5:
            print(f'Você ganhou o jogo! Receba aqui seu premio 🏆')
            break
        palavra_atual = list(len(palavras_dicas[nivel][0]) * '_')
        vidas = 6
        print(f'==========\nPROXIMO NÍVEL\n==========')

print(f'FIM DE JOGO')
