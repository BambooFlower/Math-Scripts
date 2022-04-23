import random


def coin_toss():
    coin = random.randint(0,1)
    
    if coin == 0:
        return 'Head'
    else: 
        return 'Tail'
    
    
n_simulations = 10000
n_games = 100
game_wins = 50
a_wins = 0
b_wins = 0
a_game_wins = 0
b_game_wins = 0


for i in range(n_simulations):
    game = 0
    a_wins_game_2 = 0
    b_wins_game_2 = 0 
    while game < n_games:

        player_a = 2000
        player_b = 3000
        
        while (player_a > 0) and (player_b > 0):
            toss = coin_toss()
            
            if toss == 'Head':
                player_a += 1000
                player_b -= 1000
            else:
                player_a -= 1000
                player_b += 1000
                
            if player_a == 0:
                b_game_wins += 1
                b_wins_game_2 += 1
            elif player_b == 0:
                a_game_wins += 1
                a_wins_game_2 += 1
        
        game += 1
        
    if a_wins_game_2 >= game_wins: 
        a_wins += 1
    elif b_wins_game_2 >= game_wins: 
        b_wins += 1
                
        
                
            
print(f'Player A has a {a_game_wins/n_simulations} probability of winning')
print(f'Player B has a {b_game_wins/n_simulations} probability of winning')
print(f'''Player A has a {a_wins/n_simulations} probability of winning {
    game_wins} out of {n_games}''')
print(f'''Player B has a {b_wins/n_simulations} probability of winning {
    game_wins} out of {n_games}''')


            
    