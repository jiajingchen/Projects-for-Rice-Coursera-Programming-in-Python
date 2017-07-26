grid_width=5

grid_height=8
cells = [ [0 for dummy_col in range(grid_width)] for dummy_row in range(grid_height)]

print cells
cells[2][4]=999
print cells
