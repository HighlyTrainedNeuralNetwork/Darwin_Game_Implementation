import random
from operator import itemgetter

#players should be a list of functions where each function is a bot
players = []
population = []
for i in players:
    #x should be equal to the initial number of bot copies in the pool
    population.append([x])
def run_simulation(players, turn_number, round_number, copy_number):
    pool = list(range(len(players))) * copy_number
    eliminated =[]
    for i in range(1, round_number + 1):
        scores = [0] * len(players)
        random.shuffle(pool)
        if len(pool) % 2 == 0:
            for a in range(len(pool)):
                if a % 2 == 0:
                    current_pair = pool[a:a + 2]
                    score1, score2 = run_pairing(players[current_pair[0]], players[current_pair[1]], turn_number)
                    scores[current_pair[0]] = scores[current_pair[0]] + score1
                    scores[current_pair[1]] = scores[current_pair[1]] + score2
        else:
            for a in range(len(pool)-1):
                if a % 2 == 0:
                    current_pair = pool[a:a + 2]
                    score1, score2 = run_pairing(players[current_pair[0]], players[current_pair[1]], turn_number)
                    scores[current_pair[0]] = scores[current_pair[0]] + score1
                    scores[current_pair[1]] = scores[current_pair[1]] + score2
        #Updates the pool based on the results of the round  
        total_score = sum(scores)
        new_copy_numbers = [round(copy_number * len(players) * scores[i] / total_score) for i in range(len(players))]
        pool =[]
        for count, player in zip(new_copy_numbers, players):
            pool.extend([players.index(player)] * count)
            if count == 0 and player.__name__ not in [x for y in eliminated for x in y]:
                eliminated.append((player.__name__ , i - 1))

        print('\n')
        print('End of round ' + str(i))
        for score, player in zip(scores, players):
            print(player.__name__ + ' scored ' + str(score) + ', ' + str(score / total_score * 100) + ' percent of the total score. They now have ' + str(new_copy_numbers[players.index(player)]) + ' copies in the general pool.')



        if len(set(pool)) == 1:
            print(players[pool[0]].__name__  + ' has eliminated all other agents.')
            print('\n')
            print('There were ' + str(turn_number) + ' turns in each round.')
            create_final_results(new_copy_numbers, players, eliminated)
            break

        if i == round_number:
            print('The game is now over.')
            print('\n')
            print('There were ' + str(turn_number) + ' turns in each round.')
            create_final_results(new_copy_numbers, players, eliminated)
            break

def create_final_results(final_new_copies, players, eliminated):
    not_eliminated =[]
    leaderboard =[]
    formatted_leaderboard = []
    for new_copies, player in zip(final_new_copies, players):
        if new_copies != 0:
            not_eliminated.append((player.__name__  , new_copies))
    not_eliminated = sorted(not_eliminated, key = itemgetter(1), reverse = True)
    eliminated = sorted(eliminated, key = itemgetter(1), reverse = True)
    for i in not_eliminated:
        leaderboard.append(str(i[0]) + ' survived until the end.')
    for i in eliminated:
        leaderboard.append(str(i[0]) + ' was eliminated in round ' + str(i[1]) + '.')
    for i in leaderboard:
        formatted_leaderboard.append(str(leaderboard.index(i) + 1) + '. ' + i)
    for i in formatted_leaderboard:
        print(i)

def run_pairing(player1, player2, turns):
    points1 = 0
    points2 = 0
    history1 = []
    history2 = []
    for turn in range(turns):
        player1_value = player1(history1, history2)
        player2_value = player2(history2, history1)
        history1.append(player1_value)
        history2.append(player2_value)
    return score_calculation(history1, history2), score_calculation(history2, history1)


def score_calculation(your_history, their_history):
    score = 0
    for your_move, their_move in zip(your_history, their_history):
        if your_move + their_move <= 5:
            score = score + your_move
    return score

turn_number = random.randint(90, 110)
run_simulation(players, turn_number, 200, 100)
#Creates graphical representation of population over rounds
for i in population:
    y = np.array(i)
    x = np.array([i for i in range(0,201)])
    plt.plot(x,y)
