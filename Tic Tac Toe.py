from random import choice

player_1 = input("Player 1, Enter Your Name: ")
player_2 = input("player 2, Enter Your Name: ")
play = True
while play:
    game = list(range(0, 9))
    win = False
    occupied_cases = 0
    player_turn = choice([player_1, player_2])
    if player_turn == player_1:
        print(player_1,"You are X :)", player_2,"You are Y :)")
    else:
        print(player_2,"You are X :)", player_1,"You are Y :)")
    while not win and occupied_cases <= 8:
        print("\n" + str(game[0]), game[1], game[2])
        print(game[3], game[4], game[5])
        print(game[6], game[7], game[8], "\n")
        move = int(input("Player 'X' make a move: "))
        while move not in range(0,9) or game[move] not in range(0, 9):
            move = int(input("Invalid input make a new move: "))
        game[move] = "X"
        print("\n" + str(game[0]), game[1], game[2])
        print(game[3], game[4], game[5])
        print(game[6], game[7], game[8], "\n")
        occupied_cases += 1
        win = (game[0] == game[1] == game[2] or game[3] == game[4] == game[5] or game[6] == game[7] == game[8] or
               game[0] == game[3] == game[6] or game[1] == game[4] == game[7] or game[2] == game[5] == game[8] or
               game[0] == game[4] == game[8] or game[2] == game[4] == game[6] )
        if win:
            print("Well Done! PLayer X. You Won the Game")
            play_again = input("You want to play again?(y = yes and n = no): ").lower()
            while play_again != 'y' and play_again != 'n':
                play_again = input("Invalid input,You want to play again?(y = yes and n = no): ").lower()
                play_again = play = 'y'
                if play:
                    print("----NEW GAME----")
                else:
                    break
        elif occupied_cases > 8:
            print("Oh Sooooo Close. Its a Draw !")
            play_again = input("You want to play again?(y = yes and n = no): ").lower()
            while play_again != 'y' and play_again != 'n':
                play_again = input("Invalid input,You want to play again?(y = yes and n = no): ").lower()
                play_again = play = 'y'
                if play:
                    print("----NEW GAME----")
                else:
                    break
        else:
            move = int(input("Player 'O' make a move: "))
            print("\n" + str(game[0]), game[1], game[2])
            print(game[3], game[4], game[5])
            print(game[6], game[7], game[8], "\n")
            while move not in range(0,9) and game[move] not in range(0,9):
                move = int(input("Ah! Thats already choosen, make a new move:"))
            game[move] = "O"
            occupied_cases += 1
            win = (game[0] == game[1] == game[2] or game[3] == game[4] == game[5] or game[6] == game[7] == game[8] or
                   game[0] == game[3] == game[6] or game[1] == game[4] == game[7] or game[2] == game[5] == game[8] or
                   game[0] == game[4] == game[8] or game[2] == game[4] == game[6])
            if win:
                print("Well Done! PLayer O. You Won the Game")
                play_again = input("You want to play again?(y = yes and n = no): ").lower()
                while play_again != 'y' and play_again != 'n':
                    play_again = input("Invalid input,You want to play again?(y = yes and n = no): ").lower()
                    play_again = play = 'y'
                    if play:
                        print("----NEW GAME----")
                    else:
                        break