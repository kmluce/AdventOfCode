import fileinput

class PlaneSeating():
    def __init__(self):
        self.seatMap = []
        self.newSeatMap = []
        self.adjacentSeatMap = []

    def read_seat_map(self):
        curr_line = 0
        for line in fileinput.input():
            line = line.rstrip()
            self.seatMap.append([])
            self.adjacentSeatMap.append([])
            for element in line:
                self.seatMap[curr_line].append(element)
                self.adjacentSeatMap[curr_line].append(0)
            curr_line += 1

    def print_seat_map(self):
        print("Current Seat Map:")
        for i in range(0,len(self.seatMap)):
            print(self.seatMap[i])

    def print_new_seat_map(self):
        print("New Seat Map:")
        for i in range(0,len(self.newSeatMap)):
            print(self.newSeatMap[i])

    def print_old_new_seat_map(self):
        for i in range(0,len(self.seatMap)):
            print(self.seatMap[i], "     ", self.newSeatMap[i])

    def print_adjacency_map(self):
        print("Adjacency Maps:")
        for i in range(0,len(self.seatMap)):
            print(self.seatMap[i], "    ", self.newSeatMap[i], "    ", self.adjacentSeatMap[i])


    def init_new_seat_map(self):
        #self.newSeatMap = [['.' for col in range(len(self.seatMap[0]))] for col in range(len(self.seatMap))]
        for y in range(len(self.seatMap)):
            self.newSeatMap.append([])
            for x in range(len(self.seatMap[y])):
                self.newSeatMap[y].append('.')
        #self.newSeatMap = ['.' * len(self.seatMap[0]) for col in range(len(self.seatMap))]

    def check_surrounding_seats(self, col, row):
        seatInventory = [0, 0]
        #print("starting to check surrounding seats for", row, col, "character is ", self.seatMap[row][col])
        for surround_row in range(row - 1, row + 2, 1):
            for surround_col in range(col - 1, col + 2, 1):
                #print("  testing position ", surround_col, surround_row, "for validity")
                if surround_row >= 0 and surround_row < len(self.seatMap):
                    if surround_col >= 0 and surround_col < len(self.seatMap[surround_row]):
                        if not (surround_col == col and surround_row == row):
                            #print(" checking position", surround_row, surround_col)
                            if self.seatMap[surround_row][surround_col] == 'L':
                                seatInventory[0] += 1
                            elif self.seatMap[surround_row][surround_col] == '#':
                                seatInventory[1] += 1
                            elif self.seatMap[surround_row][surround_col] == '.':
                                # check further seats in that direction
                                row_differential = surround_row - row
                                col_differential = surround_col - col
                                print(" checking seats:  checking past empty seats for ", row, ",", col)
                                print("    at ", surround_row, ",", surround_col, " with differential of",
                                      row_differential, ",", col_differential)
        #print(self.seatMap)
        self.adjacentSeatMap[row][col] = seatInventory[1]
        #print("the seat at ", row, ",", col, " has ", seatInventory[0], " empty seats and ", seatInventory[1], "full seats")
        return(seatInventory)

    def seat_change_step(self):
        #print("Size of seat map is", len(self.seatMap), ", ", len(self.seatMap[0]))
        for row in range(len(self.seatMap)):
            for col in range(len(self.seatMap[0])):
                #print("starting to check surrounding seats for", row, col, "character is ", self.seatMap[row][col])
                if self.seatMap[row][col] == 'L':
                    #print("  position ", row, ",", col, "is empty (L)", "so adding up seats.")
                    nearSeatCount = self.check_surrounding_seats(col, row)
                    #print("  Seat count for ", row, ",", col, "is",  nearSeatCount[0],",", nearSeatCount[1])
                    if nearSeatCount[1] == 0:
                        self.newSeatMap[row][col] = '#'
                    else:
                        self.newSeatMap[row][col] = 'L'
                elif self.seatMap[row][col] == '#':
                    #print("  position ", row, ",", col, "is occupied (#)", "so adding up seats.")
                    nearSeatCount = self.check_surrounding_seats(col, row)
                    #print("  Seat count for ", row, ",", col, "is",  nearSeatCount[0],",", nearSeatCount[1])
                    if nearSeatCount[1] >= 4:
                        self.newSeatMap[row][col] = 'L'
                    else:
                        self.newSeatMap[row][col] = '#'


    def compare_seat_maps(self):
        if self.seatMap == self.newSeatMap:
            print ("seat maps are the same!")
            return True
        else:
            print ("seat maps are not the same!")
            return False

    def promote_new_seat_map(self):
        #self.seatMap = self.newSeatMap
        #self.init_new_seat_map()
        for row in range(len(self.seatMap)):
            for col in range(len(self.seatMap[0])):
                self.seatMap[row][col] = self.newSeatMap[row][col]
                self.newSeatMap[row][col] = '.'

    def run_seat_map_iteration(self):
        loopCount = 1
        print("Executing first iteration.")
        self.seat_change_step()
        while (not self.compare_seat_maps()):
            print("Executing iteration ", loopCount)
            self.print_adjacency_map()
            self.promote_new_seat_map()
            self.seat_change_step()
            loopCount += 1

    def count_filled_seats(self):
        totalOccupiedSeats = 0
        for row in range(len(self.seatMap)):
            for col in range(len(self.seatMap[0])):
                if self.seatMap[row][col] == '#':
                    totalOccupiedSeats += 1
        print("Occupied seats is:", totalOccupiedSeats)




if __name__ == '__main__':
    smallPlane = PlaneSeating()

    smallPlane.read_seat_map()
    smallPlane.print_seat_map()
    smallPlane.init_new_seat_map()
    smallPlane.print_new_seat_map()

    # smallPlane.seat_change_step()
    # smallPlane.print_seat_map()
    # smallPlane.print_new_seat_map()
    # smallPlane.print_adjacency_map()
    # smallPlane.compare_seat_maps()
    # smallPlane.promote_new_seat_map()
    # smallPlane.print_adjacency_map()

    smallPlane.run_seat_map_iteration()
    smallPlane.count_filled_seats()


