##### Tye Hickman -- SWDV610 -- Final Project Submission

## Description

For this project I decided to tackle the Knight's Tour. Graph data structures have given me a bit of trouble during this class so I wanted to make sure I finished the course with a better understanding of them.
To begin, I worked my way through the Knight's Tour example provided by the online text [Beginning Here.](https://runestone.academy/runestone/books/published/pythonds/Graphs/TheKnightsTourProblem.html)

I had some issues implementing the solution, namely discerning the correct parameters to pass to the `knightTour` function.
I also had some trouble understanding the importance of the `orderByAvail` function that allows the algorithm to look ahead to squares or nodes with the _least_ number of valid moves connected to it.

I found this paper to be extremely helpful when researching Warnsdorff's rule: [How good is the Warnsdorff’s knight’s tour heuristic?](https://arxiv.org/pdf/0803.4321.pdf)

---
## Visualization

I'm a very visual learner and thought it would be interesting to show the progression of a Knight's Tour visually like some of the animated examples in the text. 
For this I used the `graphics.py` library that I used in the previous python class to draw a simple representation of a chessboard and then highlight the combination of squares that represent the Knight's Tour. I ended up having to make the program wait between moves for about half a second to make the visualization clear.

## Usage

Adding the visualization as well as allowing the user to select the board size for the Knight's Tour presented a bit of an issue with usability for me. The first thing the program does is get the board size from the user. It uses this board size to draw the window for the chessboard so I wasn't able to find a good way to keep the user in one place. The result is that the user needs to enter the board size in the terminal then once the calculation is complete, the window is drawn. Once the user selects a starting square, the solution path is calculated and the visual progression takes place.