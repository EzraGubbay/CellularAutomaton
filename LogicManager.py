
### TODO - LogicManager
# TODO: Change hardcoded n value in initializer to received input n. DONE
# TODO: Add wraparound boolean input in initializer. DONE
# TODO: Build Red Matrix appropriately for wraparound mode.

from Cell import Cell
from Block import Block

class LogicManager:

    def __init__(self, dimension: int, wraparound: bool = False):

        # Hard-coded 10, in the future the size of the matrices
        # will be based on an input n.
        n = dimension
        self.wraparound = wraparound
        self.iteration = 1
        self.main_matrix = [[Cell() for i in range(n)] for j in range(n)]
        self.blue_matrix = self._blue_matrix_builder(n)
        self.red_matrix = self._red_matrix_builder(n)

    # Logic methods
    # def update(self):
    #     # Determine generation type
    #     generation_type: int = self.generation % 2
    #
    #     # If the generation is odd, update according to logic on blue's blocks, otherwise on red's.
    #     matrix = self.blue_matrix if generation_type == 1 else self.red_matrix
    #     is_red = int(not generation_type)
    #     for i, row in enumerate(matrix):
    #         for j, block in enumerate(row):
    #
    #             # DEBUG #
    #             print("--- LogicManager ---")
    #             print("Indexes | I: ", i, "| J:", j)
    #             print("2I + 1: ", 2*i + 1, "| 2J + 1: ", 2*j + 1)
    #
    #             block.update()
    #
    #             # Update references to cells, in case a rotation occurred in-block.
    #             x = 2 * i + is_red
    #             y = 2 * j + is_red
    #             self.main_matrix[x][y] = block.cells[0]
    #             self.main_matrix[x][y + 1] = block.cells[1]
    #             self.main_matrix[x + 1][y] = block.cells[2]
    #             self.main_matrix[x + 1][y + 1] = block.cells[3]
    #
    #     # At the end of the update, increment the generation number.
    #     print("Generation Type: ", generation_type)
    #     print("Is Red: ", is_red)
    #     print("--- LogicManager --- END UPDATE")
    #     self.generation += 1

    def update(self):
        generation_type = 1 if self.iteration % 2 == 1 else 0
        if generation_type == 1:
            self._update_blue()
        else:
            self._update_red()
        self.iteration += 1

    def _update_blue(self):
        for i in range(0, len(self.main_matrix), 2):
            for j in range(0, len(self.main_matrix), 2):
                self.update_block(i, j)

    def _update_red(self):
        print("updating red")
        for i in range(1, len(self.main_matrix) - 1, 2):
            for j in range(1, len(self.main_matrix) - 1, 2):
                self.update_block(i, j)

    def update_block(self, i, j):
        block_state = (
                self.main_matrix[i][j].get_state() +
                self.main_matrix[i][j + 1].get_state() +
                self.main_matrix[i + 1][j].get_state() +
                self.main_matrix[i + 1][j + 1].get_state()
        )

        if block_state != 2:
            # Flip states
            self.main_matrix[i][j].set_state(1 if self.main_matrix[i][j].get_state() == 0 else 0)
            self.main_matrix[i][j + 1].set_state(1 if self.main_matrix[i][j + 1].get_state() == 0 else 0)
            self.main_matrix[i + 1][j].set_state(1 if self.main_matrix[i + 1][j].get_state() == 0 else 0)
            self.main_matrix[i + 1][j + 1].set_state(1 if self.main_matrix[i][j + 1].get_state() == 0 else 0)

            if block_state == 3:
                temp = self.main_matrix[i][j]
                self.main_matrix[i][j] = self.main_matrix[i + 1][j + 1]
                self.main_matrix[i + 1][j + 1] = temp
                temp = self.main_matrix[i][j + 1]
                self.main_matrix[i][j + 1] = self.main_matrix[i + 1][j]
                self.main_matrix[i + 1][j] = temp

    ### NOT USED ###
    def _generation_type(self):
        return "even" if self.iteration % 2 == 0 else "odd"

    # Auxiliary methods - for code readability and modularity.
    def _block_builder(self, i: int, j: int):
        first = self.main_matrix[i][j]
        second = self.main_matrix[i][j + 1]
        third = self.main_matrix[i + 1][j]
        fourth = self.main_matrix[i + 1][j + 1]

        return Block(first, second, third, fourth)

    def _blue_matrix_builder(self, n: int):
        return [[self._block_builder(i, j) for j in range(0, n, 2)] for i in range(0, n, 2)]

    def _red_matrix_builder(self, n: int):
        return [[self._block_builder(i, j) for i in range(1, n - 1, 2)] for j in range(1, n - 1, 2)]
