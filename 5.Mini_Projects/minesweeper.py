import random

class Cell(object):

    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col 
        self.is_bomb = False
        self.number = 0
        self.is_exposed = False
        self.is_guess = False 
    
    def flip(self):
        if self.is_guess:
            print("Cant flip unless guess is removed")
            return
        self.is_exposed = True 
        if not self.is_bomb:
            return self.number
        return -1
    
    def toggle_guess(self):
        if (not self.is_exposed):
            self.is_guess = not self.is_guess 
        return self.is_guess


class Minesweeper(object):

    def __init__(self, grid_size, mines):

        # if difficulty_level=='easy':
        #     grid_size = (16,12)
        #     mines = 16*12*5 // 100

        # if difficulty_level=='medium':
        #     grid_size = (24,16)
        #     mines = 24*26*8 // 100
        
        # if difficulty_level=='hard':
        #     grid_size = (32,24)
        #     mines = 32*24*10 // 100
        if self.mines >=grid_size[0]*grid_size[1]:
            print("Invalid game configuration")
        self.mines = mines 
        self.mines_list = []
        self.num_exposed = 0
        self.create_grid(grid_size)
    
    def create_grid(self, grid_size):

        # create random indexes for mines
        area = grid_size[0]*grid_size[1]
        self.mat = [[Cell(j,i) for i in range(grid_size[1])] for j in range(grid_size[0])]

        self.mines_list = random.sample([m for row in self.mat for m in row], self.mines)

        for mine in self.mines_list:
            mine.is_bomb = True 
        
        for i in range(grid_size[0]):
            for j in range(grid_size[1]):
                if not self.mat[i][j].is_bomb:
                    cnt=0
                    for (m,n) in (i+1,j),(i,j+1),(i-1,j),(i,j-1), (i+1,j+1), (i-1,j-1), (i+1,j-1), (i-1,j+1):
                        if m<grid_size[0] and m>=0 and n>=0 and n<grid_size[1] and self.mat[m][n].is_bomb:
                            cnt+=1
                    self.mat[i][j].number = cnt
    
    def print_grid(self):

        for row in self.mat:
            for i in range(len(row)):
                if row[i].is_bomb:
                    print("M", end=" ")
                else:
                    print(row[i].number, end=" ")
            print("")



