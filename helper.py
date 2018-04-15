'''
helper functions
'''

DEBUG = 0

def read_input_file(input_file_name):
    '''
    read input file with following format:
    first line: num_obstacles num_moves
    second to 1+num_obstacles: x y obstacle coordinates
    num_obstacles to end of file: turn / move commands. either L/R or M n

    this routine assumes the file is valid from line count perspective
    that number of obstacles is correct and that number of moves is correct
    and all inputs are well formed
    '''
    obstacles = set()
    moves = list()
    num_obstacles = 0
    num_moves = 0
    line_count = 0

    with open(input_file_name, 'r') as input_file:
        for line in input_file:
            if line_count == 0:
                # first line has number of coordinates and number of obstacles
                (num_obstacles, num_moves) = line.split()
                num_obstacles = int(num_obstacles)
                num_moves = int(num_moves)
                if DEBUG:
                    print("\tDEBUG: line: {}: HEADER: {} obstacles, {} moves in file". \
                    	format(line_count, num_obstacles, num_moves))
            elif line_count <= num_obstacles:
                # after first line, this line has obstacle coordinates
                (x_coord, y_coord) = line.split()
                x_coord = int(x_coord)
                y_coord = int(y_coord)
                obstacles.add((x_coord, y_coord))
                if DEBUG:
                    print("\tDEBUG: line: {}: OBSTACLE: at ({},{}) ". \
                    	format(line_count, x_coord, y_coord))
            else:
                # we are after obstacles, so this line has move command. either turn (L,R) or M n
                fields = line.split()
                if len(fields) == 1:
                    # one field means directional move (L,R)
                    moves.append(fields[0])
                    if DEBUG:
                        print("\tDEBUG: line: {}: TURN: Direction: {}". \
                        	format(line_count, fields[0]))
                else:
                    # two fields means move and N squares. append N
                    move_count = int(fields[1])
                    moves.append(move_count)
                    if DEBUG:
                        print("\tDEBUG: line: {}: MOVE: Count: {}". \
                        	format(line_count, move_count))
            line_count += 1
    if DEBUG:
        print("{} obstacles, {} moves read from {} in {} lines". \
        	format(num_obstacles, input_file_name, num_moves, line_count))
    return (obstacles, moves)
