# Crie uma função para verificar se houve um vencedor.
# Crie uma função para verificar se houve um empate.
# Crie uma função para verificar se uma jogada é válida.

def verificarVencedor(tabuleiro): # Puxa a variavel do tabuleiro como parametro e faz quatro verficações 
    for linha in tabuleiro: # aq verifica se as linhas são iguais e não estão vazias
        if linha[0] == linha[1] == linha[2] and linha[0] != " ":
            return linha[0]
        
    for col in range(3): # aq verifica as colunas
        if tabuleiro[0][col] == tabuleiro[1][col] == tabuleiro[2][col] and tabuleiro[0][col] != " ":
            return tabuleiro[0][col]
        
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro [2][2] and tabuleiro[0][0] != " ": # aq verifica a diagonal da superior esquerda até inferior direita
        return tabuleiro[0][0]
    
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != " ": # aq verifica a dagonal da superior direita até inferior direita
        return tabuleiro[0][2]
    
    return None # e aqui caso não houver vitória, não retorna nada

def verificarEmpate(tabuleiro): # aq eu fiz a função puxar a verificação de vitória e caso não retornar nada então consequentemente será empate
    for linha in tabuleiro:
        for elemento in linha:
            if elemento == " ":
                return False
    if verificarVencedor(tabuleiro) == None:
        return True
    
def verificarJogada(tabuleiro, posx, posy): # Aq eu usei um valor de X e Y q o jogador deverá usar para selecionar a jogada, e caso o espaço for vazio retorna verdadeiro
    if tabuleiro[posx][posy] != " ":
        return False
    else:
        return True
    