import fileinput

class Ferry():
    def __init__(self):
        self.ferryDirection = 'E'
        self.northSouth = 0
        self.eastWest = 0

    def move(self, direction, magnitude):
        if direction == 'N':
            self.northSouth += magnitude
        elif direction == 'S':
            self.northSouth -= magnitude
        elif direction == 'E':
            self.eastWest += magnitude
        elif direction == 'W':
            self.eastWest -= magnitude

    def turn_right(self):
        if self.ferryDirection == 'N':
            self.ferryDirection = 'E'
        elif self.ferryDirection == 'E':
            self.ferryDirection = 'S'
        elif self.ferryDirection == 'S':
            self.ferryDirection = 'W'
        elif self.ferryDirection == 'W':
            self.ferryDirection = 'N'

    def turn_left(self):
        if self.ferryDirection == 'N':
            self.ferryDirection = 'W'
        elif self.ferryDirection == 'W':
            self.ferryDirection = 'S'
        elif self.ferryDirection == 'S':
            self.ferryDirection = 'E'
        elif self.ferryDirection == 'E':
            self.ferryDirection = 'N'

    def turn(self, direction, magnitude):
        if direction == 'R':
            while magnitude > 0:
                self.turn_right()
                magnitude -= 90
        elif direction == 'L':
            while magnitude > 0:
                self.turn_left()
                magnitude -= 90

    def print_loc(self):
        print("    Current direction: ", self.ferryDirection, " current north:", self.northSouth,
              "current east:", self.eastWest)

    def print_distance(self):
        print("Distance from start is: ", abs(self.northSouth) + abs(self.eastWest))

    def process_directions(self):
        for line in fileinput.input():
            line = line.rstrip()
            print(line)
            command = line[0]
            magnitude = int(line[1:])
            print("  command is:", command, " magnitude is:", magnitude)
            if command == 'N' or command == 'S' or command == 'E' or command == 'W':
                self.move(command, magnitude)
            elif command == 'F':
                self.move(self.ferryDirection, magnitude)
            elif command == 'R' or command == 'L':
                self.turn(command, magnitude)
            self.print_loc()
        self.print_distance()


if __name__ == '__main__':
    myFerry = Ferry()

    myFerry.process_directions()