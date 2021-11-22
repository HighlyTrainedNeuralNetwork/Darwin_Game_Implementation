# Bots take in two arrays of moves from a round, one of their opponents and one of their own, to generate a new move.

def bot_1(your_history, their_history):
	r1 = random.randint(2, 3)
	r2 = random.randint(2, 3)
	if len(your_history) == 0 or r1 == r2:
		return r1
	if your_history[-1] + their_history[-1] < 5:
		return my[-1] + 1
	if your_history[-1] + their_history[-1] > 5:
		return your_history[-1] - 1
	return your_history[-1]

def bot_2(your_history, their_history):
    if len(your_history) == 0:
        return 0
    else:
        if their_history[0] == 0:
            if their_history[-1] != your_history[-1]:
                return your_history[-1]
            else:
                return random.randint(2, 3)
        else:
            return 3

def bot_3(your_history, their_history):
    handshake = [2,4,3]
    if len(your_history) < 3:
        return handshake[len(your_history) ]
    else:
        if their_history[:3] == [2,4,3]:
            if their_history[-1] > your_history[-1]:
                if len(your_history) % 2 == 0:
                    return 2
                else:
                    return 3
            elif their_history[-1] < your_history[-1]:
                if len(your_history) % 2 == 0:
                    return 3
                else:
                    return 2
            else:
                if random.randint(1, 2) == 1:
                    return 2
                else:
                    return 3
        elif all(i == 0 for i in their_history[-5:]) == True:
            return 5
        elif all(i == 1 for i in their_history[-10:]) == True:
            return 4
        elif all(i == 2 for i in their_history[-15:]) == True:
            return 3
        elif all(i == 3 for i in their_history[-20:]) == True:
            return 4
        elif all(i == 4 for i in their_history[-20:]) == True:
            return 4
        elif all(i == 5 for i in their_history[-20:]) == True:
            return 4
        else:
            if your_history[-1] + their_history[-1] == 5:
                return their_history[-1]
            elif len(your_history) % 2 == 0:
                if random.randint(1, 100) > 90:
                    return 3
                else:
                    return 2
            else:
                return 3
