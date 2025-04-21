from Cell import Cell


class Block:

    def __init__(self, first_cell: Cell, second_cell: Cell, third_cell: Cell, fourth_cell: Cell):

        # Cells are lined up such that:
        # Cell at (0,0) of this block is cells[0]
        # Cell at (0,1) of this block is cells[1]
        # Cell at (1,0) of this block is cells[2]
        # Cell at (1,1) of this block is cells[3]
        self.cells: [Cell] = [first_cell, second_cell, third_cell, fourth_cell]

        # Compute initial block state.
        # Block state is the sum of all cell states.
        # Useful since logic is based on number of active
        # cells with cell state 1, and sum is exact number
        # of cells with cell state 1.
        self.state: int = 0
        for cell in self.cells:
            self.state += cell.get_state()

    def get_current_state(self):
        current_state = 0
        for cell in self.cells:
            current_state += cell.get_state()
        self.state = current_state # TODO: May be superfluous
        return self.state

    def update(self):

        # Rule 1 - If block state has 0, 1, 3 or 4 live cells -
        # flip cell states.
        self.get_current_state()
        if self.state != 2:
            self._flip_states()

            # if block state was 3 - rotate the block as well.
            if self.state == 3:
                temp = self.cells[0]
                self.cells[0] = self.cells[3]
                self.cells[3] = temp
                temp = self.cells[1]
                self.cells[1] = self.cells[2]
                self.cells[2] = temp

    def _flip_states(self):
        for cell in self.cells:
            cell_state = cell.get_state()
            cell.set_state(0 if cell_state == 1 else 1)
