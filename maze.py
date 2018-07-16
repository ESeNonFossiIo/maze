import random
import numpy as np
import matplotlib.pyplot as plt

class Maze(object):

    def __init__(self, width = 10, height = 5):
        self.width  = 2*width  + 1
        self.height = 2*height + 1
        self.start  = None
        self.end    = None
        self.n_el   = self.width * self.height
        self.grid   = [' ']*(self.n_el)
        for i in range(len(self.grid)):
            if (i // self.width)%2 == 0 and i%2 == 0:
                self.grid[i] = u"\u2588"
            elif i%2 == 1:
                self.grid[i] = ' '
        self.solutions = []
        self.solution  = None
        self.max_length = self.n_el

    def set_start(self, position):
        self.grid[position] = 'S'
        self.start = position

    def set_end(self, position):
        self.grid[position] = 'E'
        self.end = position

    def __str__(self):
        grid_as_text = ''.join(self.grid)
        ret = ''
        for s in [grid_as_text[i*self.width:(i+1)*self.width] for i in range(self.height)]:
            ret += s + "\n"
        return ret

    def move(self, cell, direction, step = 1):
        new_cell = cell + step * direction[0] + step * self.width*direction[1]
        if 0 <= new_cell < self.n_el and self.grid[new_cell] != '#':
            return new_cell
        else:
            return None

    def make_maze(self, percentage = 50):
        n_elements = int(percentage * self.n_el / 100)
        for i in range(n_elements):
            p = int((self.n_el//2) * random.random())
            self.grid[2*p+1] = u"\u2588"

    def next_move(self, position, length, solution=[]):
        if length > self.max_length:
            return

        grid_copy = self.grid[:]
        sol       = solution[:]
        sol.append(position)

        for d in [[-1, 0], [1,0], [0,-1], [0,1]]:
            new_cell = self.move(position, d, 1)
            if new_cell != None and new_cell not in sol:
                if self.grid[new_cell] == 'E':
                    if len(sol) < self.max_length:
                        self.max_length = len(sol)
                    self.solutions.append(sol)
                    return
                elif self.grid[new_cell] == ' ':
                    self.next_move(new_cell, length+1, sol)

    def show_solution(self):
        if len(self.solutions) == 0:
            return
        self.solution = self.solutions[0]
        for s in self.solutions:
            if len(s) < len(self.solution):
                self.solution = s
        for p in self.solution:
            if p!= self.start and p != self.end:
                self.grid[p] = '.'

    def solve(self):
        self.next_move(self.start, 0)
        self.show_solution()

    def plot(self):
        d = {'E': 0, 'S':1, u"\u2588": 3, ' ':2, '.': 2}
        data = [d[i] for i in self.grid]
        data = np.array( data )
        data = data.reshape((self.width, self.height))

        plt.pcolormesh(data)
        plt.axes().set_aspect('equal')
        plt.xticks([])
        plt.yticks([])
        plt.axes().invert_yaxis()

        if self.solution != None:
            X = [i // self.width + 0.5 for i in self.solution]
            Y = [i % self.width + 0.5 for i in self.solution]
            plt.scatter(Y, X)

        plt.show()


n, m = 15, 15

maze = Maze(n, m)
maze.make_maze(25)

maze.set_start(((2*n + 1)*(2*m + 1))-2-(2*m + 1))
maze.set_end(((2*n + 1)*(2*m + 1))//2+1)

maze.plot()

maze.solve()

maze.plot()
