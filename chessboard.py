from graphics import * 
# import graphedKnightsTour as gkt
from graphedKnightsTour import *
import time

WN_MULT = 100

def getBoard(boardSize):
    # bSize = int(input("Board Size: "))
    bSize = boardSize * WN_MULT
    win = GraphWin("ChessBoard " + str(boardSize)+"x"+str(boardSize), bSize,bSize)
    return win

# Returns a dictionary with a key of column/row coordinate like "a1" and 
# Value needed to draw the corresponding rectangle
def genSquares(boardSize):
    sqDict  = {}
    #This loop applies chr and ord to generate a letter of a column
    for i in range(boardSize):
        x = i * WN_MULT
        x2 = x + WN_MULT
        for j in range(boardSize):
            y = j * WN_MULT
            y2 = y + WN_MULT
            sqId = (i*boardSize) + j
            sqRect = Rectangle(Point(x,y),Point(x2,y2))
            sqDict[sqId] = sqRect
    return sqDict

def genLabels(boardSize):
    labels = []
    for i in range(boardSize):
        # create column chars
        colChar = chr(ord('A') + i)
        for j in range(boardSize):
            # create row nums
            rowNum = j + 1
            labelId = colChar + str(rowNum)
            labels.append(labelId)
    return labels

def main():
    bSize = int(input("Board Size: "))

    #Start drawing some stuff
    bWin = getBoard(bSize)
    # Now I have a nice dictionary with all my squares
    squares = genSquares(bSize)
    
    # This loop draws our squares and labels to the window
    i = 0
    labelList = genLabels(bSize)
    for key in squares:
        label = Text(squares[key].getCenter(),labelList[i])
        squares[key].draw(bWin)
        label.setSize(20)
        label.draw(bWin)
        i = i + 1

    #This loop takes a mouse click and determines which square it lands in
    # it then sets the start for the knights tour to the key of the vertex
    # which also happens to be the key of the square.
    start = None
    clicker = bWin.getMouse()
    for key in squares:
        cx = clicker.getX()
        cy = clicker.getY()
        rp1x = squares[key].getP1().getX()
        rp1y = squares[key].getP1().getY()
        rp2x = squares[key].getP2().getX()
        rp2y = squares[key].getP2().getY()
        if cx >= rp1x and cy >= rp1y and cx < rp2x and cy < rp2y:
            start = key

    #now that the board is ready;
    #Get graph of all legal moves
    knightsGraph = knightGraph(bSize)

    # initialize this for the tour to keep track of the path to a solution
    knightsPath = []

    # We need to tell the knight's tour how many edges in the graph 
    # we consider to be a solution. ex: 8*8 = 64 vertices - a starting vertex = 63 edges to explore.
    searchLimit = (bSize*bSize) - 1

    knightsTour = knightTour(0,knightsPath,knightsGraph.getVertex(start),searchLimit)

    # There is a lot happening here but basically, now that we know the path for the
    # knight's tour, we update the squares on the window and draw some lines to indicate
    # the path to better visualize the knight's tour solution.
    # use the GraphWin.flush to update the squares with an arrow and setfill
    oldVertCenter = squares[knightsTour[0].getId()].getCenter()
    for vert in knightsTour:
        sqId = vert.getId()
        if sqId in squares.keys():
            # Wait about half a second so the progression is clear
            time.sleep(.4)
            squares[sqId].setFill('dark gray')
            currentVertCenter = squares[sqId].getCenter()
            connectLine = Line(oldVertCenter,currentVertCenter)
            connectLine.setWidth(2)
            connectLine.setArrow('last')
            connectLine.setFill('dark blue')
            connectLine.draw(bWin)
            bWin.flush()
            oldVertCenter = currentVertCenter

    #Once our tour is done, click again and close our window.
    bWin.getMouse()
    bWin.close()

#Make Magic!
main()
