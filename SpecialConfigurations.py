def create_diagonal_grid(block, grid_size=64):
    # Create a grid filled with zeros
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    block_size = len(block)

    # Place the block along the diagonal
    for start in range(0, grid_size, block_size):
        for i in range(block_size):
            for j in range(block_size):
                if start + i < grid_size and start + j < grid_size:
                    grid[start + i][start + j] = block[i][j]
    return grid


blinkers = {
    "blinker1": [
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 0, 0, 0]
    ],
    "blinker2": [  # intersting with wraparound
        [0, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ],
    "blinker3": [  # intersting with wraparound
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0]
    ],
    "blinker4": [  # intersting with wraparound
        [0, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1],
        [0, 1, 1, 1, 1, 0]
    ]
    ,
    "blinker5": [  # intersting with wraparound, repetitive every 12 gen
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [1, 1, 0, 0],
    ]
}
gliders = {
    "glider1": [
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 1, 1],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ],
    "glider2": [  # intersting with wraparound, repetitive every 4 gen
        [1, 1],
        [1, 1]
    ],
    "glider3": [  # intersting with wraparound, repetitive every 8 gen
        [1]
    ]
}
traffic_lights = {
    "traffic1": [  # intersting with wraparound, somthing starts climbing on thre bottom left
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]
    ],
    "traffic2": [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [0, 0, 0, 0],
    ],
    "traffic3": [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0],

    ]
}

diagonal_blinkers = {name: create_diagonal_grid(pattern) for name, pattern in blinkers.items()}
diagonal_gliders = {name: create_diagonal_grid(pattern) for name, pattern in gliders.items()}
diagonal_traffic_lights = {name: create_diagonal_grid(pattern) for name, pattern in traffic_lights.items()}
