# Conway's Game of Life

A really simple implementation of the Conway's game of life
In order to run this all you need is Python 2.7


It will create a 20x20 grid and add a glider to it. Then you can watch the magic
happen :)

To run (in a terminal window):
```
git clone https://github.com/fdosani/conways-game-of-life.git
cd conways-game-of-life
python life/simple-life.py
```

The simple-life code is a bounded box so it doesn't mirror itself, but as a
second iteration I'll implement that. Right now the glider will get stuck once
it hits the right edge.

Things you can change:
```
#edit: to change the board size
X, Y = 20, 20
#edit: to update the number of iterations
iterations = 60
```

You can also insert different shapes:
* copy the glider function or edit it with your new shape.

To do:
* Use pygames for an interface ?
* loop indefinitely (mirror/unbounded box)
