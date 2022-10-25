import sys

m=int(sys.argv[2])
t=int(sys.argv[4])
p=int(sys.argv[6])

class Con4:

    def __init__(self,m,t):
        self.numberOfColumns = t
        self.numberOfLines = m
        self.board = [ [ '  ' for _ in range( self.numberOfColumns)] for _ in range(self.numberOfLines) ]


    def display(self):
        for i, line in enumerate(self.board):
            
            # Printing the line
            print(*line, sep=' |')
            # Printing the line separators
            print("-" * self.numberOfColumns * 4)
            #print('    '.join(str(x) for x in range(self.numberOfColumns)))

    def isAvail(self, line, column):
        #Check whether the column is available or not 
        if line[column] == '  ':
            return True
        return False

    def colu_choice(self,play):
        #Taking Column choice from both players
        choice = int(input(play+", what column do you want to put your piece: "))
        while self.board[0][choice] != '  ':
            choice = int(input("This column is full. Please choose between 0 and "+str(numberOfColumns)+" : "))
        return choice

    def col_input(self):
        #Taking Colour choice From player
        player1 = input("Player1, do you want red or yellow (r/y): ")
        while True:
            if player1.lower() == 'r':
                player2='y'
                print("You've choosen " + player1 + ". Player 2 will be " + player2)
                return player1.lower(),player2
            elif player1.lower() == 'y':
                player2='r'
                print("You've choosen " + player1 + ". Player 2 will be " + player2)
                return player1.lower(),player2
            else:
                player1 = input("Incorrect Input, Please pick a marker between 'r' and 'y' ")

    def checkLines(self, marker, board=None):
        if board is None:
            board=self.board
        # Checkin lines
        for line in board:
            for i in range(0,len(line)):
                if i < len(line) - 3:
                    if line[i] == line[i+1] == line[i+2] == line[i+3] == " " + marker:
                        return True

    def checkDiags(self, marker):
        diagBoard = []
        for i, line in enumerate(self.board):
            for idx, item in enumerate(line):
                # Find of there is some marker
                if item == ' ' + marker:
                    diagBoard.append(int(str(i)+str(idx)))

        for item in diagBoard:
            if int(item) + 11 in diagBoard and int(item) + 22 in diagBoard and int(item) + 33 in diagBoard:
                return True

        for item in reversed(diagBoard):
            if int(item) - 9 in diagBoard and int(item) - 18 in diagBoard and int(item) - 27 in diagBoard:
                return True

    def reversedBoard(self):
        reversedBoard = []
        for line in self.board:
            for index, item in enumerate(line):
                try:
                    reversedBoard[index].append(item)
                except:
                    reversedBoard.append([])
                    reversedBoard[index].append(item)
        return reversedBoard

    def play(self, playercolumn, marker):
        for item in reversed(self.board):
            if self.isAvail(item, playercolumn):
                item[playercolumn] = " " + marker
                return True
        return False

c = Con4(m,t)

game = True
while game:
    # Choose your marker
    players = c.col_input()
    # Display the board
    c.display()
    # Second while loop init
    win = False
    i = 1
    while not win:
        # Start Playing
        if i % 2 == 0:
            currentPlayer = "Player2"
            marker = players[1]
            position = c.colu_choice(currentPlayer)
        else:
            currentPlayer = "Player1"
            marker = players[0]
            position = c.colu_choice(currentPlayer)
        # Player to choose where to put the mark
        if not c.play(position, marker):
            print(f"Column {position} full")

        # Generate the reversed board
        reversedBoard = c.reversedBoard()
        # Check if won
        if c.checkLines(marker) or c.checkLines(marker, reversedBoard) or c.checkDiags(marker):
            # update the win to exit the second while loop
            win = True
            c.display()
            print(f"Game won by {currentPlayer}")
            # Ask for replay. 
            # If no, change the first loop game = True to False
            # If yes, reset our class with fresh new datas
            replay = input("Do you want to play again (0-no 1-yes) ? ")
            if replay.lower() == 'n' or replay==str(0):
                game = False
                print("Game ended !")
            else:
                c = Con4(m,t)
            break
        c.display()
        i += 1