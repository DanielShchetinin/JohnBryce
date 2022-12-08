# 10. Make a continuous two-player Rock-Paper-Scissors game. Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game). In addition, keep track of the amount of wins / draws for each round, and when the user chooses to exit your program, print all the statistics of the game - total rounds played, total wins for each player, total draws.
# The rules are:
#     - Rock beats scissors
#     - Scissors beat paper
#     - Paper beats rock

erorr = 'Error, Try again!'
player_one_win = 'Congratulations, Player 1 you win!'
player_two_win = 'Congratulations, Player 2 you win!'
draw = 'Its a draw!'

wins_one = 0
wins_two = 0
draws = 0
rounds = 0

while True:

    while True:
        player_one = input("\nWelcome to Rock-Paper-Scissors game!\n\n1. Rock\n2. Scissors\n3. Paper\n\nEnter your choose: ")
        if player_one.isdigit():
            player_one = int(player_one)
            if player_one <= 0 or player_one >= 4:
                print(erorr)
                continue
            if player_one == 1:
                choose_one = 'Rock'
                break
            if player_one == 2:
                choose_one = 'Scissors'
                break
            else:
                choose_one = 'Paper'
                break
        else:
            print(erorr)
            continue
        
    while True:
        player_two = input("\nWelcome to Rock-Paper-Scissors game!\n\n1. Rock\n2. Scissors\n3. Paper\n\nEnter your choose: ")
        if player_two.isdigit():
            player_two = int(player_two)
            if player_two <= 0 or player_two >= 4:
                print(erorr)
                continue
            if player_two == 1:
                choose_two = 'Rock'
                break
            if player_two == 2:
                choose_two = 'Scissors'
                break
            else:
                choose_two = 'Paper'
                break
        else:
            print(erorr)
            continue
        
    if choose_one == 'Rock' and choose_two == 'Rock' or choose_one == 'Scissors' and choose_two == 'Scissors' or choose_one == 'Paper' and choose_two == 'Paper':
        print(draw)
        draws += 1
        rounds += 1

    if choose_one == 'Rock' and choose_two == 'Scissors':
        print(player_one_win)
        wins_one += 1
        rounds += 1

    if choose_one == 'Scissors' and choose_two == 'Paper':
        print(player_one_win)
        wins_one += 1
        rounds += 1    

    if choose_one == 'Paper' and choose_two == 'Rock':
        print(player_one_win)
        wins_one += 1
        rounds += 1
    
    if choose_one == 'Scissors' and choose_two == 'Rock':
        print(player_one_win)
        wins_one += 1
        rounds += 1

    if choose_one == 'Paper' and choose_two == 'Scissors':
        print(player_one_win)
        wins_one += 1
        rounds += 1    

    if choose_one == 'Rock' and choose_two == 'Paper':
        print(player_one_win)
        wins_one += 1
        rounds += 1     

        
    end_choose = input("\nThe game is ended\n1. New round.\n2. Close the game and view statistics\nEnter the choose: ")
    if end_choose.isdigit():
        end_choose = int(end_choose)
        if end_choose <= 0 or end_choose >= 3:
            print(erorr)
            continue
    if end_choose == 1:
        continue
    if end_choose == 2:
        break
        
    

print(f"\nPlayer one wins: {wins_one}\nPlayer one wins: {wins_two}\nDraws: {draws}\nTotal rounds: {rounds}")
