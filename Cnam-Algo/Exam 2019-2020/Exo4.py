class CheckerBoard:
    def __init__(self, taille : int):
        if (taille < 0):
            raise ValueError("Taille inférieur à 0")
        else:
            self.size = taille
            self.board = [False]*int(taille*taille)
        #endif
    #enddef

    def set_queen(self, x : int, y : int):
        if (self.__checkCoords(x, y) != ValueError):
            position = y * self.size + x
            self.board[position] = True
    #endef

    def is_queen(self, x : int, y : int):
        if (self.__checkCoords(x, y) != ValueError):
            return True if self.board[y * self.size + x] else False
        #endif
    #enddef

    def __checkCoords(self, x : int, y : int):
        if (x < 0 or x >= self.size or y < 0 or y >= self.size):
            raise ValueError("La position est impossible")
        #endif
    #endef

    def copy(self):
        newBoard = CheckerBoard(self.size)
        for i in range (len(self.board)):
            if (self.board[i]):
                newBoard.board[i] = True
        return newBoard
    #enddef

    def is_attack(self, x : int, y : int):
        position = y * self.size + x
        if (self.board[position]):
            return False
        else:

            #Verification de la ligne
            numeroLigne = x-1
            for i in range (numeroLigne*self.size, (numeroLigne*self.size)+self.size):
                if (self.board[i]):
                    return True
                #endif
            #endfor

            #Verification de la colonne
            numeroColonne = y-1
            for i in range (len(self.board)):
                if (i % self.size == numeroColonne):
                    if (self.board[i]):
                        return True
                    #endif
                #endif
            #endfor

            #Verification autour de la reine
            #Verification de la diagonale

            return False
    #enddef

    def fill_queens(self):
        return self.__fill_queens(0)
    #enddef

    def __fill_queens(self, y : int):
        if (y == self.size):
            return self
        else:
            for x in range (self.size):
                position = y * self.size + x
                if (self.is_attack(x, y) == False):
                    P = self.copy()
                    P.set_queen(x, y)
                    P = self.__fill_queens(y+1)
                    if (P is not None):
                        return P
            #endfor
        return None
        #endif
    #endef

    def __str__(self):
        res = ""
        for i in range (len(self.board)):
            if (i % self.size == 0 and i != 0):
                res += "\n"
            if (self.board[i]):
                res += "X"
            else:
                res += "|"
        return res
    #endef
#endclass

d = CheckerBoard(10)
print("Empty 10x10 checkboard")
print(d)
print()

d.set_queen(1,3)
print("10x10 checkboard with queen at position (x=1, y=3)")
print(d)
print()

d2 = d.copy()
print("Same checkboard duplicated")
print(d2)
print()

print("Is attacked at position (x=3, y=5) : "+str(d.is_attack(3,5)))
print("Is attacked at position (x=0, y=2) : "+str(d.is_attack(0,2)))
print("Is attacked at position (x=2, y=2) : "+str(d.is_attack(2,2)))
print("Is attacked at position (x=0, y=4) : "+str(d.is_attack(0,4)))
print("Is attacked at position (x=0, y=0) : "+str(d.is_attack(0,0)))
print()

# print("8x8 checkboard with 8 queens that does not attack themselves.")
# nqueens = CheckerBoard(8)
# print(nqueens.fill_queens())