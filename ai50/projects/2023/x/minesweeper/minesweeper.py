import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        # Base case: if count is equal to the number of cells, all cells are mines
        if (len(self.cells) == self.count):
            return self.cells
        # Return empty set if no mines are known
        return set()
        
    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        # Base case: if count is 0, all cells are safe
        if (self.count == 0):
            return self.cells
        return set()

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        # If we know that a cell is a mine and the count is 1, we know that all other cells are safe
        # We set the rest of the cells to be safe
        if (cell in self.cells and count == 1):            
            for others in self.cells:
                if (cell != others):
                    self.mark_safe(cell)

        
    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        # Remove cell from sentence if it is safe
        if (cell in self.cells):
            self.cells.remove(cell)

class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        # 1) mark the cell as a move that has been made
        self.moves_made.add(cell)
        
        # 2) mark the cell as safe
        self.mark_safe(cell)
        
        # 3) add a new sentence to the AI's knowledge base based on the value of `cell` and `count`
        cells = set()
        
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue
                if (i >= 0 and i < self.height and j >= 0 and j < self.width):
                    cells.add((i, j))
                    

                
        # 4) mark any additional cells as safe or as mines if it can be concluded based on the AI's knowledge base
        if (len(cells) > 0):
            self.knowledge.append(Sentence(cells, count))
            
            # Maybe not needed
            # for sentence in self.knowledge:
            #     if (sentence.known_mines()):
            #         for cell in sentence.known_mines():
            #             self.mark_mine(cell)
            #     if (sentence.known_safes()):
            #         for cell in sentence.known_safes():
            #             self.mark_safe(cell)
        
        # 5) add any new sentences to the AI's knowledge base if they can be inferred from existing knowledge
        if (count == 0):
            [self.mark_safe(cell) for cell in cells]
        if (count == len(cells)):
            [self.mark_mine(cell) for cell in cells]

        self.knowledge.append(Sentence(self.safes, 0))
        self.knowledge.append(Sentence(self.mines, len(self.mines)))
               
         
        for sentence in self.knowledge:
            for subset in self.knowledge:
                # If the sentence is a subset of the new sentence, remove the cells from the new sentence
                if (sentence.cells.issubset(subset.cells)):
                    # Update the old sentence with the new information
                    # Combine the safe cells together
                    if (sentence.count == 0 and subset.count == 0):
                        # Union of the two sets and remove the old sentences
                        newSentence = sentence.cells.union(subset.cells)
                        newCount = 0
                        knowledge.remove(sentence)
                        knowledge.remove(subset)
                    else:
                        newSentence = subset.cells - sentence.cells
                        newCount = subset.count - sentence.count
                    nSentence = Sentence(newSentence, newCount)
                    if (len(newSentence) > 0 and not nSentence in self.knowledge):
                        self.knowledge.append(Sentence(newSentence, newCount))
        # Purge empty sentences
        self.knowledge = [sentence for sentence in self.knowledge if sentence.cells]
                
    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
    
        for sentence in self.knowledge:
            for cell in sentence.known_safes():
                if (cell not in self.moves_made):
                    return cell
        return None # If no safe move can be guaranteed, return None.
        
    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        x, y = random.randrange(self.height), random.randrange(self.width)
        if (x, y) not in self.moves_made and (x, y) not in self.mines:
            return (x, y)
        else:
            make_random_move(self)



# AI = MinesweeperAI()
# MineSweeper = Minesweeper()
# move = AI.make_random_move()
# print(move)
# print(MineSweeper.nearby_mines(move))

# MineSweeper.print()
# AI.add_knowledge(move, MineSweeper.nearby_mines(move))
    