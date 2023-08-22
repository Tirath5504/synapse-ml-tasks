""" Task 1.4 """
from tabulate import tabulate
from random import randint

class ChessPlayer():

    def __init__(self, name, age, ELO_Rating, tenacity, isBoring):
        self.name = name
        self.age = age
        self.ELO_Rating = ELO_Rating
        self.tenacity = tenacity
        self.isBoring = isBoring
        self.score = 0

def simulateMatch(player1, player2):
    
    if player1.ELO_Rating - player2.ELO_Rating > 100:
        player1.score += 1
    
    elif player2.ELO_Rating - player1.ELO_Rating > 100:
        player2.score += 1

    elif player1.ELO_Rating - player2.ELO_Rating <= 100 and player1.ELO_Rating - player2.ELO_Rating >= 50:
        if player1.ELO_Rating > (player2.ELO_Rating + randint(1, 10) * player2.tenacity):
            player2.score += 1
        else:
            player1.score += 1
    
    elif player2.ELO_Rating - player1.ELO_Rating <= 100 and player2.ELO_Rating - player1.ELO_Rating >= 50:
        if player2.ELO_Rating > (player1.ELO_Rating + randint(1, 10) * player1.tenacity):
            player1.score += 1
        else:
            player2.score += 1
    
    elif abs(player2.ELO_Rating - player1.ELO_Rating) < 50:
        if player1.tenacity > player2.tenacity:
            player1.score += 1
        else:
            player2.score += 1
    
    elif player1.isBoring or player2.isBoring and (abs(player2.ELO_Rating - player1.ELO_Rating) <= 100):
        player1.score += 0.5
        player2.score += 0.5
        

def main():

    courage = ChessPlayer("Courage the Cowardly Dog", 25, 1000.39, 1000, False)
    peach = ChessPlayer("Princess Peach", 23, 945.65, 50, True)
    walter = ChessPlayer("Walter White", 50, 1650.73, 750, False)
    rory = ChessPlayer("Rory Gilmore", 16, 1700.87, 500, False)
    anthony = ChessPlayer("Anthony Fantano", 37, 1400.45, 400, True)
    beth = ChessPlayer("Beth Harmon", 20, 2500.34, 150, False)

    players = [courage, peach, walter, rory, anthony, beth]
    played = []

    for player1 in players:
        for player2 in players:
            if player1 != player2 and (player1, player2) not in played:
                simulateMatch(player1, player2)
                simulateMatch(player1, player2)
                played.append((player1, player2))
                played.append((player2, player1))

    players.sort(key= lambda player: player.score, reverse=True)

    data = []

    for player in players:
        data.append([player.name, player.age, player.score])

    headers = ["Name", "Age", "Score"]

    table = tabulate(data, headers, tablefmt="grid")

    print(f"The winner is {players[0].name}!")
    
    print(table)

if __name__ == "__main__":
    main()