'''
Author:         David Wilson
Date:           Apr 15th 2018
Description:    python program to calculate the strange and wonderful path of Wally the Robot
'''
import sys
import helper
from robot import Robot

DEBUG = 0

def main(*args):
    '''
    main
    '''
    input_file_name = args[0]

    #read input file, this function returns set of obstacle coordinates and list of moves
    #we put coordinates in set because lookup of those is hashable
    try:
        (obstacles, moves) = helper.read_input_file(input_file_name)
    except FileNotFoundError as err:
        print("Error - Cannot open input file {}".format(input_file_name))
        print(err)
        exit(-1)

    robot = Robot("wally")
    robot.set_obstacles(obstacles)
    robot.set_location((0, 0))
    robot.set_direction("N")
    if DEBUG:
        robot.set_debug_mode()

    idx = 0
    for move in moves:
        if DEBUG:
            print("main: move: {}: {}".format(idx, move))
        robot.make_move(move)
        idx += 1

    print(robot)
    print("max distance = {:.2f}".format(robot.max_distance()))

# when this is called on own, invoke main
if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SyntaxError("Incorrect usage - call {} filename".format(sys.argv[0]))
    else:
        main(sys.argv[1])
