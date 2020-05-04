# A knight moves in one of the following ways:
#  (x,y)
# x = -1 = move down by one square
# x = 1 = move up by one square
# y = -2 = move left by two squares
# y = 2 = move right by two squares
MOVE_OFFSETS = (
              (-1, -2), ( 1, -2),
    (-2, -1),                     ( 2, -1),
    (-2,  1),                     ( 2,  1),
              (-1,  2), ( 1,  2),
)
from Graph import *

# Create a graph of legal moves.
def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            # print("("+str(row)+"*"+str(bdSize)+")+"+str(col)+"="+str(posToNodeId(col,row,bdSize)))
            nodeId = posToNodeId(row,col,bdSize)
            newPositions = genLegalMoves(row,col,bdSize)
            for e in newPositions:
                nid = posToNodeId(e[0],e[1],bdSize)
                ktGraph.addEdge(nodeId,nid)
    return ktGraph

# This function also helps map the graph vertices to the chessboard visualization later.
def posToNodeId(row, column, board_size):
    return (row * board_size) + column

def genLegalMoves(x,y,bdSize):
    newMoves = []
    moveOffsets = MOVE_OFFSETS
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        # Recursively check coordinate is on board
        if legalCoord(newX,bdSize) and legalCoord(newY,bdSize):
            newMoves.append((newX,newY))
    return newMoves

# Verify that the coordinate is on the board.
def legalCoord(x,bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return False

def knightTour(n,path,u,limit):
        u.setColor('gray')
        path.append(u)
        if n < limit:
            nbrList = orderByAvail(u)
            i = 0
            done = False
            while i < len(nbrList) and not done:
                if nbrList[i].getColor() == 'white':
                    done = knightTour(n+1, path, nbrList[i], limit)
                i = i + 1
            if not done:  # prepare to backtrack
                path.pop()
                u.setColor('white')
        else:
            done = True
        return path

# Warnsdorff's Rule is applied here as a heuristic
def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c = c + 1
            resList.append((c,v))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]