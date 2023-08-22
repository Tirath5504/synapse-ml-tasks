""" Task 1.4 """
from tabulate import tabulate

class ChessPlayer():

    def __init__(self, name, age, ELO_Rating, tenacity, isBoring):
        self.name = name
        self.age = age
        self.ELO_Rating = ELO_Rating
        self.tenacity = tenacity
        self.isBoring = isBoring
        self.score = 0

def simulateMatch(player1, player2):
    ...

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

    players.sort(key= lambda player: player.score)

    data = []

    for player in players:
        data.append([player.name, player.age, player.score])

    headers = ["Name", "Age", "Score"]

    table = tabulate(data, headers, tablefmt="grid")

    print(table)

    print(f"The winner is {players[0].name}!")

if __name__ == "__main__":
    main()