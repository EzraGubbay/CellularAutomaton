def create_diagonal_grid(block, grid_size=100, spacing=2, start_offset=3):
    # Create a grid filled with zeros
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    block_size = len(block)

    # Step between blocks (block size + spacing)
    step = block_size + spacing

    # Place blocks starting at (start_offset, start_offset)
    for k in range(0, grid_size, step):
        i_offset = start_offset + k
        j_offset = start_offset + k

        for i in range(block_size):
            for j in range(block_size):
                x, y = i_offset + i, j_offset + j
                if x < grid_size and y < grid_size:
                    grid[x][y] = block[i][j]

    return grid



blinkers = {


     "blinker1": [  # move to blinkers
        [1, 1],
        [1, 1]
    ],
    "blinker2": [ 
        [1],
    ],
}
gliders = {
        "glider1": [  # intersting with wraparound, 
        #can put it also in gliders since little gliders start moving all arounf the screen
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0]
    ],
   "glider2": [  # move to gliders screen
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [1, 1, 0, 0],
    ],
           "glider3": [  # move to glders
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ],
   
}
traffic_lights = {

            "traffic1": [  # move to traffic, repetitive every 8 gen
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
    ],
                    "traffic2": [ #move to trafic, repititive after 13 gen
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 0, 0, 0]
    ],
}

diagonal_blinkers = {name: create_diagonal_grid(pattern) for name, pattern in blinkers.items()}
diagonal_gliders = {name: create_diagonal_grid(pattern) for name, pattern in gliders.items()}
diagonal_traffic_lights = {name: create_diagonal_grid(pattern) for name, pattern in traffic_lights.items()}
