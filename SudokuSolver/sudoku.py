#### Grace Hadiyanto
#### Assignment 9
#### E-mail: ifoundparis@gmail.com
#### CS 223P

import sys
import queue
import random

CHOICES = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

class Cell:
    __slots__ = {'_symbol', '_myrow', '_mycolumn', '_mysubboard', '_choices', '_past_choices'}
    
    def __init__(self, symbol):
        self._symbol = symbol
        self._past_choices = set()
        self._choices = set()

    def __str__(self):
        return self._symbol

    def __repr__(self):
        return 'Cell: {}'.format(self._symbol)

    @property
    def pastchoices(self):
        return self._past_choices
    @pastchoices.setter
    def pastchoices(self, choice_set):
        self._past_choices = choice_set

    @property
    def myrow(self):
        return self._myrow
    @myrow.setter
    def myrow(self, row):
        self._myrow = row

    @property
    def mycolumn(self):
        return self._mycolumn
    @mycolumn.setter
    def mycolumn(self, column):
        self._mycolumn = column

    @property
    def mysubboard(self):
        return self._mysubboard
    @mysubboard.setter
    def mysubboard(self, board):
        self._mysubboard = board

    @property
    def symbol(self):
        return self._symbol
    @symbol.setter
    def symbol(self, symbol):
        self._symbol = symbol

    def getChoices(self):
        choices = CHOICES - self.myrow.getSymbols().union(self.mycolumn.getSymbols(), self.mysubboard.getSymbols())
        return choices #- self.pastchoices
    
    def choices(self):
        """Recalculates the possible choices for an unknown cell, and returns
        the number of choices possible."""
        self._choices = self.getChoices()
        return len(self._choices)

    def setChoice(self, symbol):
        self.symbol = symbol

class BaseBoardClass:
    """A base class for the row, column, and subboard."""
    def getSymbols(self):
        symbols = set()
        for cell in self._cells:
            symbols.add(cell.symbol)
        return symbols

    def getSymbolList(self):
        symbols = []
        for cell in self._cells:
            if cell.symbol != '.':
                symbols.append(cell.symbol)
        return symbols

    @property
    def cells(self):
        return self._cells
    
    def __str__(self):
        s = ''
        for cell in self._cells:
            s += str(cell)
        s += '\n'
        return s

class Row(BaseBoardClass):
    def __init__(self, seq_of_cells):
        self._cells = set(seq_of_cells)
        for cell in self._cells:
            cell.myrow = self

class Column(BaseBoardClass):
    def __init__(self, seq_of_cells):
        self._cells = set(seq_of_cells)
        for cell in self._cells:
            cell.mycolumn = self

class SubBoard(BaseBoardClass):
    def __init__(self, seq_of_cells):
        self._myrows = set()
        self._mycolumns = set()
        self._cells = set(seq_of_cells)
        for cell in self._cells:
            cell.mysubboard = self
            self._myrows.add(cell.myrow)
            self._mycolumns.add(cell.mycolumn)

class Board:
    __slots__ = {'_cells', '_rows', '_columns','_iterIndex', '_sub_boards'}
    
    def __init__(self, puzzle):
        self._cells = [ Cell(x) for x in puzzle ]
        self._rows = [ Row(self._cells[x : x+9]) for x in range(0, 81, 9) ]
        
        self._columns = []
        for col in range(9):
            thiscolumn = []
            for elementindex in range(col, 81, 9):
                thiscolumn.append(self._cells[elementindex])
            self._columns.append(Column(thiscolumn))
        
        temp_boards = [ set() for x in range(9) ]
        x = 0
        cellIndex = 0
        for board in range(9):
            for i in range(3):
                temp_boards[x].add(self._cells[cellIndex])
                temp_boards[x].add(self._cells[cellIndex+9])
                temp_boards[x].add(self._cells[cellIndex+18])
                cellIndex += 1
            x += 1
            if x == 3:
                cellIndex = 27
            if x == 6:
                cellIndex = 54
        self._sub_boards = []
        for board in temp_boards:
            self._sub_boards.append(SubBoard(board))

    @property
    def cells(self):
        return self._cells

    def __iter__(self):
        iterIndex = 0
        while True:
            yield self._cells[iterIndex]
            iterIndex += 1
            if iterIndex == 81:
                raise StopIteration()

    def __str__(self):
        s = ''
        for cell in self._cells:
            s+= str(cell)
        s += '\n'
        return s

def writeSolution(solutions):
    dotIndex = sys.argv[1].find('.')
    with open('{}-solution.txt'.format(sys.argv[1][:dotIndex]), 'w') as filehandler:
        filehandler.write(solutions)
    
def writePuzzle(puzzle):
    with open(sys.argv[1],'w') as filehandler:
        filehandler.write(puzzle)

def reinit(s, board):
    s = s.rstrip()
    for index, char in enumerate(s):
        board.cells[index].symbol = char

def guessChoice(cell_tuple, board):
    index = cell_tuple[1]
    choices = board.cells[index].getChoices()
    if len(choices) == 0:
        return None, index
    else:
        return choices, index

def rollBack(states, board):
    last_safe_state = states.pop()
    reinit(last_safe_state[1], board)
    return last_safe_state[0], last_safe_state[2], last_safe_state[3]

def checkCompletion(board):
    rv = True
    for index, cell in enumerate(board):
        if cell.symbol == '.':
            rv = False
    return rv
        
def makeGuess(choice, index, board):
    board.cells[index].setChoice(choice)

def recalculateQueue(q, board):
    new_queue = queue.PriorityQueue()
    for index, cell in enumerate(board):
        if cell.symbol == '.':
            cell_info = cell.choices(), index
            new_queue.put(cell_info)
    return new_queue

# Checks if a cell's symbol is correct by taking the intersection of the symbols
# in its row, column, and subboard to see that the symbols 1-9 occur once on
# all of them.
def perfect(board, index):
    if CHOICES == board.cells[index].myrow.getSymbols().intersection(board.cells[index].mycolumn.getSymbols(), board.cells[index].mycolumn.getSymbols()):
        return True

# Re-initializes the cells' symbols back to the last safest state
def safeRollBack(states, board):
    if len(states) == 1:
        last_correct_state = states[0]
    else:
        last_correct_state = states.pop()
    reinit(last_correct_state, board)


def selectRandom(set_of_choices):
    choices = list(set_of_choices)
    return random.choice(choices)

def solver(board):
    q = queue.PriorityQueue()
    states = []
    correct_states = [ str(board) ]
    changed_cells = set()
    # Goes through each unknown cell in the board. If there is only one possible
    # choice for their symbol, change their symbol to that choice. Else, put
    # the cell along with the number of possible symbols into a priority queue.
    for index, cell in enumerate(board):
        if cell.symbol == '.':
            if cell.choices() == 1:
                choice = cell.getChoices().pop()
                cell.setChoice(choice)
                cell.pastchoices.add(choice)
            else:
                cell_info = cell.choices(), index
                q.put(cell_info)

    # The first safe, correct, state of the board.
    correct_states.append(str(board))

    # Check for completion of the board.
    complete = checkCompletion(board)
    while not complete:
        # Recalculate the priority queue and go through the unknown cells,
        # making guesses, while saving the state each time a guess is made.
        q = recalculateQueue(q, board)  
        choices, index = guessChoice(q.get(), board)
        if choices != None:
            choice = selectRandom(choices)
            states.append((choice, str(board), q, index))
            makeGuess(choice, index, board)
            # board.cells[index].pastchoices.add(choice)
            if perfect(board, index) == True:
                correct_states.append(str(board))
        else:
            safeRollBack(correct_states, board)
           # board.cells[index].pastchoices = set()
        

        # v Uncomment the line below to see the board at each step!
        # print(board)
        complete = checkCompletion(board)

def main():
    random.seed()
    solutions = ''
    with open(sys.argv[1]) as filehandler:
        count = 0
        for line in filehandler:
            count += 1
            puzzle = line.rstrip()
            print('{}:\n{}'.format(count, puzzle))
            b = Board(puzzle)
            solver(b)
            solutions += str(b)
            print(b)
    writeSolution(solutions)

if __name__ == '__main__':
    import timeit
    totalTime = timeit.timeit("main()", setup="from __main__ import main", number=1)
    print('It took a total of {} seconds to run.'.format(totalTime))
    
