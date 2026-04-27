from functions.jogo_da_velha import exibir_tabuleiro
from functions.verificacoes import verificarVencedor
from functions.verificacoes import verificarJogada
from functions.verificacoes import verificarEmpate

jogo_ativo = True
jogador = "X"
tabuleiro = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

while jogo_ativo:
    exibir_tabuleiro(tabuleiro)

    posX = int(input(f"jogador {jogador}, escolha posição horizontal: ")) - 1#pro jogador escolher a posição dele
    posY = int(input(f"jogador {jogador}, escolha posição vertical: ")) - 1

    if verificarJogada(tabuleiro, posX, posY):     #vai verificar se a jogada vai ser valida, caso o campo esteja ou nao preenchido
        tabuleiro[posX][posY] = jogador
    
        if verificarVencedor(tabuleiro) != None: #vai verificar se o jogaodor venceu
            exibir_tabuleiro(tabuleiro)
            print(f"o jogador '{verificarVencedor(tabuleiro)}' venceu")
            jogo_ativo = False
    
        elif verificarEmpate(tabuleiro):  #vai verificar se deu empate, e se nao, o jogo continua
            exibir_tabuleiro(tabuleiro)
            print("empate")
            jogo_ativo = False

        else: #pra trocar os jogadores caso o outro ja tenha jogado
            if jogador == "X":
                jogador = "O"
            else:
                jogador = "X"

    else:
        print("jogada invalida")