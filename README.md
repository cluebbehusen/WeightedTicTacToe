# WeightedTicTacToe

This program uses Python to implement an automated tic tac toe program based on the weights of each potential move. Used moves are stored in a .csv file taken as a command line argument. Wins are assigned a weight of 1, losses a weight of 0, and ties a weight of .5. At each turn, the program analyzes each of its potential moves and picks the one with the highest weight. At the end of each game, the program updates the .csv file it used based on the outcome of the game. Currently, one can only play against the computer to train it or have it play against another computer using a different .csv file.

## Usage

For playing manually against the program:

```
python3 main.py [.csv file]
```

For having the programs train themselves:

```
python3 two_computers.py [.csv file 1] [.csv file 2] [number of games to play]
```