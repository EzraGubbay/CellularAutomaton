
### TODO - LogicManager
# TODO: Change hardcoded n value in initializer to received input n. DONE
# TODO: Add wraparound boolean input in initializer. DONE
# TODO: Build Red Matrix appropriately for wraparound mode.

from Cell import Cell
from Block import Block

class LogicManager:

    def __init__(self, dimension: int, wraparound: bool = False, config: str = None):

        # Hard-coded 10, in the future the size of the matrices
        # will be based on an input n.
        self.dimension = dimension
        self.wraparound = wraparound
        self.iteration = 1

        self.main_matrix = [[Cell() for i in range(self.dimension)] for j in range(self.dimension)]
        if config is not None:
            for i in range(self.dimension):
                for j in range(self.dimension):
                    self.main_matrix[i][j].set_state(config[i][j])

        self.blue_matrix = self._blue_matrix_builder(self.dimension)
        self.red_matrix = self._red_matrix_builder(self.dimension)

    def update(self):
        generation_type = 1 if self.iteration % 2 == 1 else 0
        if generation_type == 1:
            self._update_blue()
        else:
            self._update_red()
        self.iteration += 1

    # Blue and red essentially do the same thing, except use different indexes.
    # Red also may have wraparound.
    #
    def _update_blue(self):
        for i in range(0, len(self.main_matrix), 2):
            for j in range(0, len(self.main_matrix), 2):
                self.update_block(i, j)

    def _update_red(self):
        print("updating red")
        for i in range(1, len(self.main_matrix) - 1, 2):
            for j in range(1, len(self.main_matrix) - 1, 2):
                self.update_block(i, j)

        if self.wraparound:
            self._update_frame_blocks()

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
            self.main_matrix[i + 1][j + 1].set_state(1 if self.main_matrix[i + 1][j + 1].get_state() == 0 else 0)

            if block_state == 3:
                temp = self.main_matrix[i][j]
                self.main_matrix[i][j] = self.main_matrix[i + 1][j + 1]
                self.main_matrix[i + 1][j + 1] = temp
                temp = self.main_matrix[i][j + 1]
                self.main_matrix[i][j + 1] = self.main_matrix[i + 1][j]
                self.main_matrix[i + 1][j] = temp

    def _update_frame_blocks(self):
        # Check the corner block
        block_state = (
            self.main_matrix[0][0].get_state() +
            self.main_matrix[0][self.dimension - 1].get_state() +
            self.main_matrix[self.dimension - 1][0].get_state() +
            self.main_matrix[self.dimension - 1][self.dimension - 1].get_state()
        )

        if block_state != 2:
            self.main_matrix[0][0].set_state(1 if self.main_matrix[0][0].get_state() == 0 else 0)
            self.main_matrix[0][self.dimension - 1].set_state(1 if self.main_matrix[0][self.dimension - 1].get_state() == 0 else 0)
            self.main_matrix[self.dimension - 1][0].set_state(1 if self.main_matrix[self.dimension - 1][0].get_state() == 0 else 0)
            self.main_matrix[self.dimension - 1][self.dimension - 1].set_state(1 if self.main_matrix[self.dimension - 1][self.dimension - 1].get_state() == 0 else 0)

            if block_state == 3:
                temp = self.main_matrix[0][0]
                self.main_matrix[0][0] = self.main_matrix[self.dimension - 1][self.dimension - 1]
                self.main_matrix[self.dimension - 1][self.dimension - 1] = temp
                temp = self.main_matrix[0][self.dimension - 1]
                self.main_matrix[0][self.dimension - 1] = self.main_matrix[self.dimension - 1][0]
                self.main_matrix[self.dimension - 1][0] = temp

        # Check for non-corner frame blocks - vertical
        for i in range(1, self.dimension - 1, 2):
            block_state_vertical = (
                self.main_matrix[i][0].get_state() +
                self.main_matrix[i][self.dimension - 1].get_state() +
                self.main_matrix[i + 1][0].get_state() +
                self.main_matrix[i + 1][self.dimension - 1].get_state()
            )

            block_state_horizontal = (
                    self.main_matrix[0][i].get_state() +
                    self.main_matrix[self.dimension - 1][i].get_state() +
                    self.main_matrix[0][i + 1].get_state() +
                    self.main_matrix[self.dimension - 1][i + 1].get_state()
            )

            if block_state_vertical != 2:
                self.main_matrix[i][0].set_state(1 if self.main_matrix[i][0].get_state() == 0 else 0)
                self.main_matrix[i][self.dimension - 1].set_state(
                    1 if self.main_matrix[i][self.dimension - 1].get_state() == 0 else 0)
                self.main_matrix[i + 1][0].set_state(
                    1 if self.main_matrix[i + 1][0].get_state() == 0 else 0)
                self.main_matrix[i + 1][self.dimension - 1].set_state(
                    1 if self.main_matrix[i + 1][self.dimension - 1].get_state() == 0 else 0)

                if block_state_vertical == 3:
                    temp = self.main_matrix[i][0]
                    self.main_matrix[i][0] = self.main_matrix[i + 1][self.dimension - 1]
                    self.main_matrix[i + 1][self.dimension - 1] = temp
                    temp = self.main_matrix[i][self.dimension - 1]
                    self.main_matrix[i][self.dimension - 1] = self.main_matrix[i + 1][0]
                    self.main_matrix[i + 1][0] = temp

            if block_state_horizontal != 2:
                self.main_matrix[0][i].set_state(1 if self.main_matrix[0][i].get_state() == 0 else 0)
                self.main_matrix[self.dimension - 1][i].set_state(1 if self.main_matrix[self.dimension - 1][i].get_state() == 0 else 0)
                self.main_matrix[0][i + 1].set_state(1 if self.main_matrix[0][i + 1].get_state() == 0 else 0)
                self.main_matrix[self.dimension - 1][i + 1].set_state(1 if self.main_matrix[self.dimension - 1][i + 1].get_state() == 0 else 0)

                if block_state_horizontal == 3:
                    temp = self.main_matrix[0][i]
                    self.main_matrix[0][i] = self.main_matrix[self.dimension - 1][i + 1]
                    self.main_matrix[self.dimension - 1][i + 1] = temp
                    temp = self.main_matrix[0][i + 1]
                    self.main_matrix[0][i + 1] = self.main_matrix[self.dimension - 1][i]
                    self.main_matrix[self.dimension - 1][i] = temp


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
