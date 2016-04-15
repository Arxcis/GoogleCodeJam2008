"""
    problem B: Always turn left maze.

    session 00:00 - 03:22
    Completed: - Run from start to end.
    Left to do: - Run from end to start.
                - Convert [0,0,0,0] pattern
                   to hex-pattern. 
"""

from turtle import Screen
import os


class MazeState:
    def __init__(self):
        # Direction is set to backwards-direction
        self.direction = 0
        self.heading = 'South'
        self.col = 0
        self.row = 0
        self.maze = [[[1,0,0,0]]]

    def check_heading(self):
        if self.direction == 0:
            self.heading = 'South'
        if self.direction == 1:
            self.heading = 'North'
        if self.direction == 2:
            self.heading = 'East'
        if self.direction == 3: 
            self.heading = 'West'

    def inverse_direction(self, direction):
        if direction == 0:
            return 1
        if direction == 1:
            return 0
        if direction == 2:
            return 3
        if direction == 3:
            return 2

    def update_block(self, switch):
        if switch == 0:
            self.maze[self.row][self.col][self.inverse_direction(self.direction)] = 1
        if switch == 1:
            self.maze[self.row][self.col][self.direction] = 1



    def take_action(self, action):
        """ Direction:
            north = 0
            south = 1
            west  = 2
            east  = 3
        """
        direction = self.direction

        if action == 'R':
            if direction == 0:
                self.direction = 3
            elif direction == 1:
                self.direction = 2
            elif direction == 2: 
                self.direction = 0
            elif direction == 3:
                self.direction = 1

            self.check_heading()
            print("Heading = ", self.heading)

        if action == 'L':
            if direction == 0:
                self.direction = 2
            elif direction == 1:
                self.direction = 3
            elif direction == 2: 
                self.direction = 1
            elif direction == 3:
                self.direction = 0

            self.check_heading()
            print("Heading = ", self.heading)

        if action == 'W':
            if direction == 0:
                self.update_block(0)
                self.row += 1
            if direction == 1:
                self.update_block(0)
                self.row -= 1
            if direction == 2:
                self.update_block(0)
                self.col += 1
            if direction == 3:
                self.update_block(0)
                self.col -= 1

            print("Row = ", self.row, "Column = ", self.col)
            self.expand_maze()


    def expand_maze(self):

        # Expand left
        if self.col < 0:
            for row in range(len(self.maze)):
                (self.maze[row]).insert(0, [0,0,0,0])
            self.col = 0
            self.update_block(1)
            self.print_maze()

        # Expand downwards
        else:
            try: 
                self.maze[self.row]

            except IndexError:
                new_row = []
                for i in range(len(self.maze[self.row-1])):
                    new_row.append([0,0,0,0])

                (self.maze).append(new_row)
                self.update_block(1)
                self.print_maze()
                return 0


            try: 
                self.maze[self.row][self.col]

            except IndexError:
                for row in range(len(self.maze)):
                    (self.maze[row]).append([0,0,0,0])
                self.update_block(1)
                self.print_maze()
                return 0

            self.update_block(1)
            self.print_maze()



    def print_maze(self):
        for row in self.maze:
            print(row)
        input()
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_current(self):
        print(self.maze[self.row][self.col])


state = MazeState()
print("Heading = ", state.heading)
state.print_maze()



 # Hard-input test-loop

input_string = "WRWWLWWLWWLWLWRRWRWWWRWWRWLW"
for i in range(len(input_string)):

    char = input_string[i]
    state.take_action(char)


""" # Turtle screen test-loop

s = Screen()

s.onkey(lambda: state.take_action('R'), 'Right')
s.onkey(lambda: state.take_action('L'), 'Left')
s.onkey(lambda: state.take_action('W'), 'Up')
s.onkey(state.print_current, "space")
s.listen()
s.mainloop()
"""