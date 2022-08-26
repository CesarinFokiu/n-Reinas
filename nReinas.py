import plistlib
import numpy

import matplotlib.pyplot as plt


class estadoTablero:
    modelBoard = [None for _ in range(8)]
    numQueen = 3

    def setQueen(self, row, col):
        self.modelBoard[col] = row
        self.numQueen += 1
    
    def lostQueen(self,row,col):
        if self.modelBoard:
            self.modelBoard[col] = None
            self.numQueen -= 1

    def numQueens(self):
        return self.numQueens

    def get_board(self):
        return self.modelBoard
    
    x= range(numQueen)
    x= numpy.array(x)
    print(x)
    y= range(numQueen)
    y = numpy.array(y)
    print(y)
    x = x + 0.5
    y = y + 0.5
    plt.figure()
    plt.scatter(x,y)
    plt.xlim(0,numQueen)
    plt.ylim(0,numQueen)
    plt.xticks(x-0.5)
    plt.yticks(y-0.5)
    plt.grid(True)
    plt.title(u"Reinas")
    plt.show() 

Tablero = estadoTablero()
print (Tablero.get_board())

Tablero.setQueen(1, 2)
print (Tablero.get_board()) 