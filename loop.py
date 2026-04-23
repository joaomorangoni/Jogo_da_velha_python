jogo_ativo = True
jogador = "X"

while jogo_ativo:
    mostrar_tabuleiro()
    
    pos = int(input(f"jogador {jogador}, escolha posição: ")) #pro jogador escolher a posição dele

    if jogada_valida(pos):     #vai verificar se a jogada vai ser valida, caso o campo esteja ou nao preenchido
        tabuleiro[pos] = jogador
    
        if verificar_vencedor(jogador): #vai verificar se o jogaodor venceu
            print(f"{jogador} venceu")
            jogo_ativo = False
    
        elif verificar_empate():  #vai verificar se deu empate, e se nao, o jogo continua
            print("empate")
            jogo_ativo = False

        else: #pra trocar os jogadores caso o outro ja tenha jogado
            if jogador == "X":
                jogador = "O"
            else:
                jogador = "X"

    else:
        print("jogada invalida")