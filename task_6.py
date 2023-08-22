class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass

def rps_game_winner(game):
    if len(game) != 2:
        raise WrongNumberOfPlayersError("There should be exactly 2 players")

    valid_strategies = ["R", "P", "S"]
    player1, move1 = game[0]
    player2, move2 = game[1]

    if move1 not in valid_strategies or move2 not in valid_strategies:
        raise NoSuchStrategyError("Invalid strategy")

    if move1 == move2:
        return str(game[0][0]+" "+game[0][1])  

    if (move1 == "R" and move2 == "S") or (move1 == "S" and move2 == "P") or (move1 == "P" and move2 == "R"):
        return str(game[0][0]+" "+game[0][1])

    return str(game[1][0]+' '+game[1][1])  


game1 = [["player1", "P"], ["player2", "S"]]
winner1 = rps_game_winner(game1)
print(winner1)  # Вывод: ["player2", "S"]

game2 = [["player1", "R"], ["player2", "R"]]
winner2 = rps_game_winner(game2)
print(winner2)  # Вывод: ["player1", "R"]

game3 = [["player1", "R"], ["player2", "R"],['fdgdfg','T']]
winner3 = rps_game_winner(game3)
print(winner3)  # Вывод: WrongNumberOfPlayersError: There should be exactly 2 players
