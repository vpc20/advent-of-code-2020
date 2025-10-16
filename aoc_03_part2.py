from aoc_tools import read_input_to_grid

if __name__ == '__main__':
    # grid = read_input_to_grid('aoc_03_testdata1.txt')
    grid = read_input_to_grid('aoc_03_data1.txt')
    nrows = len(grid)
    ncols = len(grid[0])

    for e in grid:
        print(e)
        # print(''.join(row))
    print(nrows, ncols)

    tree_prod = 1
    for row_delta, col_delta in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
        row = 0
        col = 0
        tree_ctr = 0
        while True:
            row += row_delta
            col += col_delta
            if row > nrows - 1 :
                break
            if col > ncols - 1:
                col = col % ncols  # wrap around
            if grid[row][col] == '#':
                tree_ctr += 1
        print(tree_ctr)
        tree_prod *= tree_ctr
    print(tree_prod)
