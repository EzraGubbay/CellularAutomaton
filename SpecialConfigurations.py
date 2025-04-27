def create_diagonal_grid(block, grid_size=50):
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
    "blinker2": [
        [0, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ],
    "blinker3": [
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0]
    ],
    "blinker4": [
    [0, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 0]
    ]
    ,
    "blinker5": [
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
    "glider2": [
        [1, 1],
        [1, 1]
    ],
    "glider3": [
        [1]
    ]
}
traffic_lights = {  
    "traffic1": [
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]
    ],
    "traffic2": [
        [1, 1],
        [1, 1]
    ],
    "traffic3": [
        [1]
    ]
}

diagonal_blinkers = {name: create_diagonal_grid(pattern) for name, pattern in blinkers.items()}
diagonal_gliders = {name: create_diagonal_grid(pattern) for name, pattern in gliders.items()}
diagonal_traffic_lights = {name: create_diagonal_grid(pattern) for name, pattern in traffic_lights.items()}

