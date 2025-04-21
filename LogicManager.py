
### TODO - LogicManager
# TODO: Change hardcoded n value in initializer to received input n.
# TODO: Add wraparound boolean input in initializer.
# TODO: Build Red Matrix appropriately for wraparound mode.

from Cell import Cell
from Block import Block

class LogicManager:

    def __init__(self, dimension: int, wraparound: bool = False):

        # Hard-coded 10, in the future the size of the matrices
        # will be based on an input n.
        n = dimension
        self._generation = 1
        self.main_matrix = [[Cell() for i in range(n)] for j in range(n)]
        self.blue_matrix = self._blue_matrix_builder(n)
        self.red_matrix = self._red_matrix_builder(n)

    # Logic methods
    def update(self):
        generation_type: int = self._generation % 2
        if generation_type == 0: # Even generation, check blue blocks.
            for row in self.blue_matrix:
                for block in row:
                    block.update()
        else:
            for row in self.red_matrix:
                for block in row:
                    block.update()

    ### NOT USED ###
    def _generation_type(self):
        return "even" if self._generation % 2 == 0 else "odd"

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
        return [[self._block_builder(i, j) for i in range(1, n - 1)] for j in range(1, n - 1)]
