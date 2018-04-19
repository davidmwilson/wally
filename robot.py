'''
this file contains the definition of the Robot class, used by main program
'''
import math

class Robot(object):
    '''
    this is class for Robot
    '''
    # this dictionary uses lookup by movement direction
    # to get new direction bsed on L/R turns, and x/y offsets based on direction
    _directions = {'N': {'L' : 'W', 'R' : 'E', 'x_offset' : 0, 'y_offset' : 1},
                   'E': {'L' : 'N', 'R' : 'S', 'x_offset' : 1, 'y_offset' : 0},
                   'W': {'L' : 'S', 'R' : 'N', 'x_offset' : -1, 'y_offset' : 0},
                   'S': {'L' : 'E', 'R' : 'W', 'x_offset' : 0, 'y_offset' : -1}}

    def __init__(self, name):
        # constructor
        self._name = name
        self._x = 0
        self._y = 0
        self._direction = "N"
        self._obstacles = set()
        self._moves = []
        self._distance = 0
        self._max_distance = 0
        self._turn_count = 0
        self._move_count = 0
        self._move_distance = 0
        self._block_count = 0
        self._total_move_count = 0
        self._debug = 0

    def __iter__(self):
    	''' implement iterator '''
    	for move in self._moves:
    		  yield move

    def set_debug_mode(self):
        ''' enable debug mode '''
        self._debug = 1

    def debug(self):
        ''' are we in debug mode? '''
        return self._debug == 1

    def set_location(self, coords):
        ''' update coordinates'''
        (self._x, self._y) = coords

    def set_direction(self, direction):
        ''' set new direction'''
        self._direction = direction

    def set_obstacles(self, obstacles_set):
        ''' set obstacles for robot to look out for '''
        self._obstacles = obstacles_set

    def set_moves(self, moves_list):
        ''' set list of moves '''
        self._moves = moves_list

    def calculate_distance(self):
        ''' now update euclidean distance and max if appropriate '''
        self._distance = math.sqrt((abs(self._x)**2)+(abs(self._y)**2))
        # is this > prior max distance?
        self._max_distance = max(self._distance, self._max_distance)

    def make_move(self, my_move):
        ''' make move for robot, either a left/right turn or actual distance move '''
        if my_move in ('L', 'R'):
            self.turn(my_move)
        else:
            # this is a move command
            self.move(my_move)

    def turn(self, turn_direction):
        ''' turn left or right '''
        if self.debug():
            print("get_new_direction: current dir: {}, move: {}".\
                format(self._direction, turn_direction))
        # lookup new direction from dictionary
        self.set_direction(self._directions[self._direction][turn_direction])

        if self.debug():
            print("get_new_direction: new direction: {}".format(self._direction))

        self._turn_count += 1
        self._total_move_count += 1

    def move(self, number_of_moves):
        ''' move in current direction, taking account of any obstacles in path '''
        # lookup x/y offsets based on current direction
        x_offset = self._directions[self._direction]['x_offset']
        y_offset = self._directions[self._direction]['y_offset']
        if self.debug():
            print("robot.move: dir: {}, start at: ({},{}) x_offset:{}, y_offset:{}". \
                format(self._direction, self._x, self._y, x_offset, y_offset))
        self._move_count += 1
        self._total_move_count += 1

        for move_idx in range(0, number_of_moves):
            new_x = self._x+x_offset
            new_y = self._y+y_offset
            new_coords = (new_x, new_y)
            if not new_coords in self._obstacles:
            # we made a move, update x and y and move onto next
                if self.debug():
                    print("robot.move: made a move, coords now {}".format(new_coords))
                self.set_location(new_coords)
                self._move_distance += 1
            else:
                # if moving this way is blocked, will always be blocked from now on
                # e.g. if need to move 100 and blocked after 2, no need to do this another 98 times
                self._block_count += number_of_moves - move_idx
                if self.debug():
                    print("robot.move: {} is an obstacle, no move".format(new_coords))
                break
        self.calculate_distance()

    def max_distance(self):
        ''' return max distance from home '''
        return self._max_distance

    def current_location(self):
        ''' return current location pair as a set '''
        return (self._x, self._y)

    def moves(self):
        ''' return moves list '''
        return self._moves

    def __repr__(self):
        '''
        override built in print behavior
        '''
        return "{} has moved {} times, ({} turns, {} moves), been blocked {} times, blocks moved {}, current distance={:.2f}, max distance={:.2f}". \
            format(self._name, self._total_move_count, self._turn_count, self._move_count, self._block_count, self._move_distance, self._distance, self._max_distance)
